#!/usr/bin/env python3
"""Build the Knife Rider Stream Deck profiles (15 keys and XL).

    python3 src/build.py

Writes, for each profile of layout.LAYOUTS:
    assets/icons/                      every key the profile draws itself (PNG / GIF)
    build/<key>/                       the profile tree, as it goes into the archive
    <archive>.streamDeckProfile        the importable archive, at the repository root
    docs/MAPPING*.md, docs/LAYOUT*.md  key / command tables

The archives have the layout Stream Deck 7 exports (package.json naming the required
plugin, then Profiles/<id>.sdProfile/ with one directory per page), the same as the
Farline companion's own master profiles: importing one offers to install the plugin
when it is missing.
"""
import hashlib
import json
import os
import shutil
import sys
import unicodedata
import uuid
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import companion as C      # noqa: E402
import keymap as K         # noqa: E402
import layout as L         # noqa: E402
import tactical as T       # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS = os.path.join(ROOT, "assets", "icons")
BUILD = os.path.join(ROOT, "build")
DOCS = os.path.join(ROOT, "docs")

with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as _fh:
    VERSION = _fh.read().strip()     # bump at each release, see docs/MISE-A-JOUR.md
GAME_BUILD = f"{C.MIN_GAME} ou plus récent, schéma du companion {C.PLUGIN_RELEASE}"

# PROFILE_ID is the 15-key profile's name AND the seed of all its ids (profile, pages,
# actions). Changing it makes Stream Deck see a NEW profile, so re-importing would leave
# players with two copies instead of updating the one they have since v1. It must stay
# byte-for-byte identical for the life of the project. The XL profile has its own name
# and its own seed (layout.LAYOUTS), so its ids never meet the 15-key ones.
PROFILE_ID = "Knife Rider - 15 Key"
assert L.LAYOUTS[0]["name"] == PROFILE_ID and L.LAYOUTS[0]["seeds"] == ()

NS = uuid.UUID("5a1d4f2c-9c3b-4b2e-9c7a-6b1f0d8e4c21")   # stable ids across rebuilds
NONE_PAGE = "00000000-0000-0000-0000-000000000000"
TITLE_COLOR = T.INK


def package(lay):
    """What Stream Deck 7 writes in an exported profile's package.json (read from the
    companion's master profiles, themselves read from exports of the software)."""
    return {"AppVersion": "7.4.0", "DeviceModel": lay["model"], "DeviceSettings": None,
            "FormatVersion": 1, "OSType": "Windows", "OSVersion": "10.0",
            "RequiredPlugins": [C.PLUGIN_UUID]}


def uid(*parts):
    return str(uuid.uuid5(NS, "|".join(str(p) for p in parts)))


def lid(lay, *parts):
    """An id inside one profile: the 15-key one has no seed, as in v1."""
    return uid(*lay["seeds"], *parts)


def profile_uuid(lay):
    return uid("profile", lay["name"]).upper()


def page_uuid(lay, page_key):
    return lid(lay, "page", page_key)


def default_page(lay):
    """The empty page Stream Deck 7 keeps as a profile's Default (as in its exports)."""
    return uid("default", lay["name"])


def device_uuid(lay):
    """Not a serial number: a fixed id, as the companion's own profiles write it."""
    return uid("device", lay["model"])


def slug(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    t = "".join(c if c.isalnum() else "_" for c in t.lower())
    while "__" in t:
        t = t.replace("__", "_")
    return t.strip("_")


def doc_name(lay, base):
    return f"{base}.md" if lay["key"] == "15" else f"{base}-{lay['key'].upper()}.md"


# ---------------------------------------------------------------------------
# key faces
# ---------------------------------------------------------------------------
def frames(btn):
    """The SVG frames of an animated key, or None for a still one."""
    anim = btn.get("anim")
    if not anim:
        return None
    ts = [i / T.FRAMES for i in range(T.FRAMES)]
    if anim == "flares":
        return [T.anim_flares(btn["symbol"], btn["label"], btn["key"], t) for t in ts]
    return [T.ANIMS[anim](btn["symbol"], btn["label"], t) for t in ts]


def face(btn):
    """The still face of a key as an SVG: what this profile draws, or for a plugin key
    what the plugin draws once paired (used by the preview only - the profile leaves
    plugin keys without an image, the plugin paints them)."""
    kind = btn["kind"]
    if btn.get("anim"):
        return frames(btn)[0]
    if kind == "hotkey":
        return T.hotkey_key(btn["label"], btn["symbol"], btn["key"], btn["filled"], btn["tag"])
    if kind == "folder":
        return T.nav_key(btn["symbol"], btn["label"], folder=True)
    if kind == "back":
        return T.nav_key(btn["symbol"])
    if kind == "command":
        icon = C.command_icon(btn["action"])
        return T.command_key(btn["label"], *(icon or (None, False)))
    if kind == "value":
        return T.value_key(btn["label"], *C.FIELD_ICONS.get(btn["field"], (None, False)))
    raise ValueError(kind)


def draws_itself(btn):
    return btn["kind"] in ("hotkey", "folder", "back")


def image_name(lay, page_key, pos, ext):
    """A file name shaped like the ones Stream Deck writes (25 hex + Z), stable."""
    h = hashlib.sha1(f"{lay['name']}|{page_key}|{pos}".encode()).hexdigest()[:25].upper()
    return f"{h}Z{ext}"


def render_button(lay, page_key, pos, btn):
    """Render a key this profile draws; returns (file name, path in assets/icons)."""
    f = frames(btn)
    ext = ".gif" if f else ".png"
    name = image_name(lay, page_key, pos, ext)
    readable = os.path.join(
        ICONS, f"{lay['slug']}{slug(page_key)}_{pos[0]}{pos[1]}_{slug(btn['label'])}{ext}")
    if f:
        T.save_gif(f, readable)
    else:
        T.save_png(face(btn), readable)
    return name, readable


# ---------------------------------------------------------------------------
# profile assembly
# ---------------------------------------------------------------------------
def state(title, image=None):
    out = {"FontSize": 11, "ShowTitle": False, "Title": title,
           "TitleAlignment": "bottom", "TitleColor": TITLE_COLOR}
    if image:
        out["Image"] = f"Images/{image}"
    return out


def action(lay, page_key, pos, btn, image):
    base = {"ActionID": lid(lay, "action", page_key, pos), "LinkedTitle": True,
            "Resources": None, "State": 0, "States": [state(btn["label"], image)]}
    kind = btn["kind"]
    plugin = {"Name": "Farline", "UUID": C.PLUGIN_UUID, "Version": C.PLUGIN_VERSION}
    if kind == "command":
        base.update(Name="Command", Settings={"id": btn["action"]}, UUID=C.COMMAND_UUID,
                    Plugin=plugin)
    elif kind == "value":
        base.update(Name="Value", Settings={"field": btn["field"]}, UUID=C.VALUE_UUID,
                    Plugin=plugin)
    elif kind == "hotkey":
        base.update(Name="Hotkey", Settings=K.hotkey_settings(K.key_of(btn["action"])),
                    Plugin={"Name": "Activate a Key Command",
                            "UUID": "com.elgato.streamdeck.system.hotkey", "Version": "1.0"},
                    UUID="com.elgato.streamdeck.system.hotkey")
    elif kind == "folder":
        base.update(Name="Create Folder", Settings={"ProfileUUID": page_uuid(lay, btn["page"])},
                    Plugin={"Name": "Create Folder",
                            "UUID": "com.elgato.streamdeck.profile.openchild", "Version": "1.0"},
                    UUID="com.elgato.streamdeck.profile.openchild")
    elif kind == "back":
        base.update(Name="Parent Folder", Settings={},
                    UUID="com.elgato.streamdeck.profile.backtoparent")
    else:
        raise ValueError(kind)
    return base


def write_json(path, value):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(value, fh, ensure_ascii=False, sort_keys=True)


def build_profile(lay):
    build_dir = os.path.join(BUILD, lay["key"])
    os.makedirs(build_dir, exist_ok=True)
    write_json(os.path.join(build_dir, "package.json"), package(lay))
    root_dir = os.path.join(build_dir, "Profiles", f"{profile_uuid(lay)}.sdProfile")
    os.makedirs(os.path.join(root_dir, "Profiles"), exist_ok=True)

    for page_key in lay["order"]:
        page = lay["pages"][page_key]
        pdir = os.path.join(root_dir, "Profiles", page_uuid(lay, page_key).upper())
        os.makedirs(os.path.join(pdir, "Images"), exist_ok=True)
        actions = {}
        for pos, btn in sorted(page["keys"].items()):
            assert 0 <= pos[0] < lay["cols"] and 0 <= pos[1] < lay["rows"], (page_key, pos)
            image = None
            if draws_itself(btn):
                image, readable = render_button(lay, page_key, pos, btn)
                shutil.copy(readable, os.path.join(pdir, "Images", image))
            actions[f"{pos[0]},{pos[1]}"] = action(lay, page_key, pos, btn, image)
        write_json(os.path.join(pdir, "manifest.json"),
                   {"Controllers": [{"Actions": actions, "Type": "Keypad"}], "Icon": "", "Name": ""})

    empty = os.path.join(root_dir, "Profiles", default_page(lay).upper())
    os.makedirs(os.path.join(empty, "Images"), exist_ok=True)
    write_json(os.path.join(empty, "manifest.json"),
               {"Controllers": [{"Actions": None, "Type": "Keypad"}], "Icon": "", "Name": ""})

    write_json(os.path.join(root_dir, "manifest.json"), {
        "Device": {"Model": lay["model"], "UUID": device_uuid(lay)},
        "Name": lay["name"],
        "Pages": {"Current": NONE_PAGE, "Default": default_page(lay),
                  "Pages": [page_uuid(lay, lay["root"])]},
        "Version": "3.0",
    })
    return build_dir


# Fixed stamp + explicit permissions: the source tree may live on a Windows
# mount where every file reads as 0777, and zipfile would copy that into the
# archive - handing anyone who unpacks it world-writable, executable PNGs.
ZIP_STAMP = (2026, 10, 15, 12, 0, 0)
ZIP_FILE_ATTR = (0o100644 << 16)
ZIP_DIR_ATTR = (0o040755 << 16) | 0x10


def _entry(name, is_dir=False):
    info = zipfile.ZipInfo(name + ("/" if is_dir else ""), date_time=ZIP_STAMP)
    info.external_attr = ZIP_DIR_ATTR if is_dir else ZIP_FILE_ATTR
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 0          # announce "Unix", consistently with the mode bits
    return info


def archive_path(lay):
    return os.path.join(ROOT, lay["archive"])


def zip_profile(lay, build_dir):
    out = archive_path(lay)
    if os.path.exists(out):
        os.remove(out)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        with open(os.path.join(build_dir, "package.json"), "rb") as fh:
            z.writestr(_entry("package.json"), fh.read())
        for dirpath, dirs, files in os.walk(os.path.join(build_dir, "Profiles")):
            dirs.sort()
            arc = os.path.relpath(dirpath, build_dir).replace(os.sep, "/")
            z.writestr(_entry(arc, is_dir=True), b"")
            for f in sorted(files):
                with open(os.path.join(dirpath, f), "rb") as fh:
                    z.writestr(_entry(f"{arc}/{f}"), fh.read())
    return out


# ---------------------------------------------------------------------------
# docs
# ---------------------------------------------------------------------------
def write_mapping(lay):
    rows = []
    for page_key in lay["order"]:
        page = lay["pages"][page_key]
        for pos, btn in sorted(page["keys"].items(), key=lambda kv: (kv[0][1], kv[0][0])):
            where = (lay["titles"][page_key], f"col {pos[0] + 1} / ligne {pos[1] + 1}")
            if btn["kind"] == "command":
                rows.append(where + (btn["label"], f"`{btn['action']}`", "plugin", "—"))
            elif btn["kind"] == "value":
                rows.append(where + (btn["label"], f"`{btn['field']}` (valeur)", "plugin", "—"))
            elif btn["kind"] == "hotkey":
                rows.append(where + (btn["label"], f"`{btn['action']}`", "touche clavier",
                                     f"`{btn['key']}`"))

    out = [
        f"# Table de correspondance — {lay['device']}",
        "",
        f"Profil « {lay['name']} » v{VERSION} — généré par `src/build.py`. "
        f"Jeu : Knife Rider {GAME_BUILD}.",
        "",
        "- **plugin** : la touche passe par le plugin Farline companion. Elle marche quelle",
        "  que soit la touche clavier que vous avez choisie dans le jeu.",
        "- **touche clavier** : la touche Stream Deck tape la touche **par défaut** du jeu.",
        "  Seulement pour ce que le plugin ne sait pas faire : les actions à maintenir",
        "  (vol, boost, tir, éjection) et missile / leurres / trappe, absents de son schéma.",
        "",
        "| Page | Bouton | Libellé | Commande | Par | Touche |",
        "|---|---|---|---|---|---|",
    ]
    out += [f"| {' | '.join(r)} |" for r in rows]

    out += ["", "## Commandes sans bouton", "",
            "| Commande | Libellé | Pourquoi |", "|---|---|---|"]
    for cid, why in (("fire", "à maintenir et sans touche par défaut (clic gauche souris)"),
                     ("call_dismiss", "aucune touche par défaut, le plugin la refuserait (`unbound`)"),
                     ("convergence", "demande une distance choisie : à régler soi-même dans le plugin")):
        out.append(f"| `{cid}` | {C.label(cid)} | {why} |")

    out += ["", "## Touches réservées par le jeu", "", "| Touche | Rôle |", "|---|---|"]
    out += [f"| `{K.key_label(k)}` | {v} |" for k, v in K.FIXED_KEYS]

    with open(os.path.join(DOCS, doc_name(lay, "MAPPING")), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return len(rows)


def write_layout(lay):
    """docs/LAYOUT*.md: one map per page, kept in sync with layout.py."""
    cols, rows_n = lay["cols"], lay["rows"]
    out = [f"# Plan des pages — {lay['device']} ({cols} × {rows_n})", "",
           "Généré par `src/build.py`. `·` = touche volontairement vide.", ""]
    for page_key in lay["order"]:
        page = lay["pages"][page_key]
        out += [f"## {lay['titles'][page_key]}", ""]
        grid = []
        for r in range(rows_n):
            row = []
            for c in range(cols):
                btn = page["keys"].get((c, r))
                if btn is None:
                    row.append("·")
                elif btn["kind"] == "folder":
                    row.append(f"📁 {btn['label']}")
                elif btn["kind"] == "back":
                    row.append("↩ Retour")
                elif btn["kind"] == "hotkey":
                    row.append(f"{btn['label']} `{btn['key']}`")
                elif btn["kind"] == "value":
                    row.append(f"📊 {btn['label']}")
                else:
                    row.append(f"`{btn['action']}`")
            grid.append(row)
        width = [max(len(grid[r][c]) for r in range(rows_n)) for c in range(cols)]
        out.append("| " + " | ".join(f"col {c + 1}".ljust(width[c]) for c in range(cols)) + " |")
        out.append("|" + "|".join("-" * (w + 2) for w in width) + "|")
        for row in grid:
            out.append("| " + " | ".join(row[c].ljust(width[c]) for c in range(cols)) + " |")
        out.append("")
    out += ["---", "",
            "`identifiant` = touche du plugin (son libellé vient du jeu) · "
            "`TOUCHE` = touche clavier native · 📊 = valeur affichée.", ""]
    with open(os.path.join(DOCS, doc_name(lay, "LAYOUT")), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))


# ---------------------------------------------------------------------------
def main():
    for d in (ICONS, BUILD):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d, exist_ok=True)
    os.makedirs(DOCS, exist_ok=True)

    print(f"version  : {VERSION}")
    for lay in L.LAYOUTS:
        archive = zip_profile(lay, build_profile(lay))
        n = write_mapping(lay)
        write_layout(lay)
        keys = [b for p in lay["pages"].values() for b in p["keys"].values()]
        count = {k: sum(1 for b in keys if b["kind"] == k)
                 for k in ("command", "value", "hotkey", "folder", "back")}
        print(f"\n[{lay['name']}]  profil {profile_uuid(lay)}")
        print(f"  pages    : {len(lay['pages'])}")
        print(f"  boutons  : {len(keys)}  {count}")
        print(f"  docs     : {n} lignes -> docs/{doc_name(lay, 'MAPPING')}, docs/{doc_name(lay, 'LAYOUT')}")
        print(f"  archive  : {lay['archive']} ({os.path.getsize(archive) / 1024:.0f} Ko)")


if __name__ == "__main__":
    main()
