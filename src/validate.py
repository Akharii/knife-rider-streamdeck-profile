#!/usr/bin/env python3
"""Static checks on the built Knife Rider profiles (15 keys and XL).

    python3 src/validate.py

These are structural checks only. They prove the archives are well formed, that every
plugin key names a command the game's companion schema lists, and that every native
key carries the key the game documents - they do NOT prove anything about the running
game: importing a profile, pairing the plugin and pressing the keys in Knife Rider is
still a manual step.
"""
import collections
import io
import json
import os
import re
import sys
import zipfile

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build as BLD     # noqa: E402
import companion as C   # noqa: E402
import keymap as K      # noqa: E402
import layout as L      # noqa: E402

OK, BAD = [], []

HOTKEY = "com.elgato.streamdeck.system.hotkey"
OPEN = "com.elgato.streamdeck.profile.openchild"
BACK = "com.elgato.streamdeck.profile.backtoparent"


def check(cond, msg):
    (OK if cond else BAD).append(msg)


def schema_key(name):
    """The schema writes keys as the game shows them ("Kp 8", "PageUp"); keymap.py as
    Godot names them (KP_8, PAGEUP)."""
    return re.sub(r"[\s_]", "", name).upper()


def needs_key(command_id):
    """A "press" is an action of the game's Controls page, pressed as its key would be:
    with no key, the game refuses it (`unbound`). A "delta" (convergence_up / _down)
    is the companion's own and has no key behind it."""
    return C.COMMANDS[command_id]["kind"] == "press"


def validate(lay):
    tag = lay["key"]
    archive = BLD.archive_path(lay)
    check(os.path.exists(archive), f"<{tag}> archive présente : {lay['archive']}")
    if not os.path.exists(archive):
        return

    z = zipfile.ZipFile(archive)
    names = z.namelist()
    check(not [n for n in names if n.startswith("/") or ".." in n or "\\" in n],
          f"<{tag}> aucun chemin absolu ni remontant dans l'archive")

    # --- package.json (Stream Deck 7 export) ---------------------------------
    pkg = json.loads(z.read("package.json"))
    check(pkg.get("RequiredPlugins") == [C.PLUGIN_UUID],
          f"<{tag}> package.json exige le plugin {C.PLUGIN_UUID}")
    check(pkg.get("DeviceModel") == lay["model"], f"<{tag}> package.json : modèle {lay['model']}")

    top = f"Profiles/{BLD.profile_uuid(lay)}.sdProfile"
    check({n.split("/")[0] for n in names} == {"package.json", "Profiles"},
          f"<{tag}> racine : package.json + Profiles/")
    check(all(n in ("package.json", "Profiles/") or n.startswith(top + "/") for n in names),
          f"<{tag}> un seul profil, {BLD.profile_uuid(lay)}")

    root = json.loads(z.read(f"{top}/manifest.json"))
    check(root["Version"] == "3.0", f"<{tag}> manifest racine en Version 3.0")
    check(root["Name"] == lay["name"], f"<{tag}> nom du profil « {lay['name']} »")
    check(root["Device"]["Model"] == lay["model"], f"<{tag}> modèle d'appareil {lay['model']}")
    check(root["Device"]["UUID"] == BLD.device_uuid(lay),
          f"<{tag}> identifiant d'appareil fixe, aucun numéro de série")
    check(root["Pages"]["Pages"] == [BLD.page_uuid(lay, lay["root"])],
          f"<{tag}> la page d'accueil est la seule page de premier niveau")
    check(root["Pages"]["Current"] == BLD.NONE_PAGE, f"<{tag}> pas de page courante imposée")

    page_dirs = {n.split("/")[3] for n in names
                 if n.startswith(f"{top}/Profiles/") and n.count("/") >= 4}
    declared = {BLD.page_uuid(lay, k).upper(): k for k in lay["pages"]}
    default = root["Pages"]["Default"].upper()
    check(page_dirs == set(declared) | {default},
          f"<{tag}> {len(page_dirs)} dossiers de pages = {len(lay['pages'])} pages + la page par défaut")
    empty = json.loads(z.read(f"{top}/Profiles/{default}/manifest.json"))
    check(empty["Controllers"][0]["Actions"] is None, f"<{tag}> page par défaut vide")

    # --- per page ---------------------------------------------------------------
    reachable = {BLD.page_uuid(lay, lay["root"]).upper()}
    parents = collections.defaultdict(list)
    action_total = 0
    pressed = collections.Counter()
    native = collections.Counter()

    for pdir in sorted(set(declared)):
        page_key = declared[pdir]
        base = f"{top}/Profiles/{pdir}"
        man = json.loads(z.read(f"{base}/manifest.json"))
        check(set(man) == {"Controllers", "Icon", "Name"}, f"<{tag}>[{page_key}] clés du manifeste")
        ctrls = man["Controllers"]
        check(len(ctrls) == 1 and ctrls[0]["Type"] == "Keypad", f"<{tag}>[{page_key}] un contrôleur Keypad")
        actions = ctrls[0]["Actions"]
        action_total += len(actions)
        images = {n.split("/")[-1] for n in names
                  if n.startswith(f"{base}/Images/") and not n.endswith("/")}
        used = set()
        keys_here = collections.defaultdict(list)
        backs = 0

        for pos, a in actions.items():
            col, row = (int(x) for x in pos.split(","))
            where = f"<{tag}>[{page_key}/{pos}]"
            check(0 <= col < lay["cols"] and 0 <= row < lay["rows"],
                  f"{where} dans la grille {lay['cols']}x{lay['rows']}")
            btn = lay["pages"][page_key]["keys"][(col, row)]
            st = a["States"][0]
            uuid = a["UUID"]

            if uuid in (C.COMMAND_UUID, C.VALUE_UUID):
                check(a["Plugin"] == {"Name": "Farline", "UUID": C.PLUGIN_UUID,
                                      "Version": C.PLUGIN_VERSION},
                      f"{where} bloc Plugin du companion")
                check("Image" not in st, f"{where} pas d'image : le plugin peint la touche")
                check(st["ShowTitle"] is False, f"{where} titre masqué (le plugin écrit le libellé)")
                if uuid == C.COMMAND_UUID:
                    cid = a["Settings"].get("id")
                    check(a["Settings"] == {"id": cid} and C.pressable(cid),
                          f"{where} commande `{cid}` que le plugin sait envoyer")
                    check(not needs_key(cid) or C.default_key(cid) is not None,
                          f"{where} `{cid}` a une touche par défaut (sinon refus `unbound`)")
                    pressed[cid] += 1
                else:
                    fid = a["Settings"].get("field")
                    check(a["Settings"] == {"field": fid} and fid in C.FIELDS,
                          f"{where} valeur `{fid}` que le jeu envoie")
                continue

            img = st.get("Image", "")
            check(img.startswith("Images/") and not re.match(r"^([A-Za-z]:|/|\\\\)", img),
                  f"{where} image en chemin relatif")
            fname = img.split("/")[-1]
            check(fname in images, f"{where} image présente : {fname}")
            used.add(fname)
            if fname in images:
                im = Image.open(io.BytesIO(z.read(f"{base}/Images/{fname}")))
                if fname.endswith(".gif"):
                    check(btn.get("anim") and getattr(im, "n_frames", 1) > 1 and im.size == (144, 144),
                          f"{where} animation GIF 144 px, {getattr(im, 'n_frames', 1)} images")
                else:
                    check(fname.endswith(".png") and im.size == (288, 288) and not btn.get("anim"),
                          f"{where} image fixe PNG 288 px")

            if uuid == HOTKEY:
                aid = btn["action"]
                slots = a["Settings"]["Hotkeys"]
                check(len(slots) == 4, f"{where} 4 emplacements de touche")
                first = slots[0]
                expected = K.KEYS[K.key_of(aid)]
                check(all(first[k] == v for k, v in expected.items()),
                      f"{where} encodage conforme pour {aid} -> {K.key_of(aid)}")
                check(all(s["NativeCode"] == 146 for s in slots[1:]), f"{where} emplacements 2-4 vides")
                check(not C.pressable(aid),
                      f"{where} `{aid}` en touche clavier seulement si le plugin ne sait pas l'envoyer")
                if aid in C.COMMANDS:
                    check(C.COMMANDS[aid]["kind"] == "hold",
                          f"{where} `{aid}` est une action à maintenir")
                    check(schema_key(C.default_key(aid) or "") == schema_key(K.key_of(aid)),
                          f"{where} `{aid}` : même touche dans keymap.py et le schéma du jeu")
                keys_here[K.key_of(aid)].append(aid)
                native[aid] += 1
            elif uuid == OPEN:
                target = a["Settings"]["ProfileUUID"].upper()
                check(target in declared, f"{where} dossier cible existant")
                reachable.add(target)
                parents[target].append(page_key)
            elif uuid == BACK:
                backs += 1
            else:
                check(False, f"{where} action inconnue {uuid}")

        check(images == used, f"<{tag}>[{page_key}] aucune image orpheline ({sorted(images - used)})")
        if page_key == lay["root"]:
            check(backs == 0, f"<{tag}>[root] pas de bouton Retour sur la page d'accueil")
        else:
            check(backs == 1 and "0,0" in actions and actions["0,0"]["UUID"] == BACK,
                  f"<{tag}>[{page_key}] un seul Retour, en haut à gauche")
        for key, acts in keys_here.items():
            check(len(acts) == 1,
                  f"<{tag}>[{page_key}] touche `{K.key_label(key)}` tapée par un seul bouton {acts}")

    check(action_total == sum(len(p["keys"]) for p in lay["pages"].values()),
          f"<{tag}> {action_total} actions écrites")

    # --- navigation -------------------------------------------------------------
    check(reachable == set(declared), f"<{tag}> toutes les pages sont atteignables")
    for child, ps in parents.items():
        check(len(ps) == 1 and lay["parent"][declared[child]] == ps[0],
              f"<{tag}>[{declared[child]}] un seul parent, {lay['parent'][declared[child]]}")

    # --- coverage of the game's commands -------------------------------------------
    want_plugin = {c for c in C.COMMANDS if C.pressable(c) and (C.default_key(c) or not needs_key(c))}
    check(not (want_plugin - set(pressed)),
          f"<{tag}> chaque commande du schéma a son bouton plugin "
          f"(manquantes : {sorted(want_plugin - set(pressed))})")
    want_hold = {c for c, v in C.COMMANDS.items() if v["kind"] == "hold" and C.default_key(c)
                 and c not in ("conv_far", "conv_near")}   # covered by convergence_up / _down
    check(not (want_hold - set(native)),
          f"<{tag}> chaque action à maintenir a sa touche clavier "
          f"(manquantes : {sorted(want_hold - set(native))})")
    outside = {a[0] for a in K.ACTIONS if a[0] not in C.COMMANDS}
    check(outside <= set(native),
          f"<{tag}> les actions hors schéma ({sorted(outside)}) gardent leur touche clavier")
    for cid in ("fire", "call_dismiss"):
        check(cid not in pressed and cid not in native,
              f"<{tag}> `{cid}` sans touche par défaut n'a pas reçu de bouton")


def main():
    for lay in L.LAYOUTS:
        validate(lay)
    ids = [BLD.profile_uuid(lay) for lay in L.LAYOUTS]
    check(len(set(ids)) == len(ids), "chaque profil a son propre identifiant")
    check(BLD.profile_uuid(L.LAYOUTS[0]) == "C3EB0303-7F58-5F2F-8C86-B1C6A837447B",
          "le profil 15 touches garde l'identifiant de la v1")
    pages = [BLD.page_uuid(lay, k) for lay in L.LAYOUTS for k in lay["pages"]]
    check(len(set(pages)) == len(pages), "aucune page partagée entre les deux profils")
    return report()


def report():
    print(f"{len(OK)} contrôles OK")
    if BAD:
        print(f"\n{len(BAD)} ÉCHECS :")
        for m in BAD:
            print("  ✗", m)
    else:
        print("aucun échec")
    print("\nRappel : ces contrôles sont statiques. L'import dans Stream Deck, l'appairage du "
          "plugin et le test des touches en jeu restent à faire manuellement.")
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main())
