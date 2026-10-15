"""Page layouts of the Knife Rider Stream Deck profiles: 15 keys (5 x 3) and XL (8 x 4).

Each profile is a dict of LAYOUTS (bottom of this file). Every key is declared as
(col, row) -> Button. Four kinds of keys:

    cmd(id)        a key of the Farline companion plugin: it sends the game's command
                   over the companion link and the plugin draws its face (label, pictogram,
                   and the state it changes: gear lit when down, energy share, convergence).
    value(field)   a plugin key that shows one value of the HUD (speed, hull...).
    hotkey(id)     a native Stream Deck Hotkey, ONLY for what the plugin cannot press:
                   the actions the game wants held (kind "hold" in its schema: flight axes,
                   boost, fire groups, eject) and the three actions the schema does not list.
    folder / back  navigation, drawn by this profile in the plugin's style.

Labels and pictograms of plugin keys come from the plugin itself; nothing is written
by hand here for them.
"""
import companion as C
import keymap as K


def B(**kw):
    return kw


def cmd(action):
    assert C.pressable(action), f"{action}: not a command the plugin can press"
    return B(kind="command", action=action, label=C.label(action))


def value(field):
    assert field in C.FIELDS, f"{field}: not a field the game pushes"
    return B(kind="value", field=field, label=C.field_label(field))


def hotkey(action, label, symbol=None, filled=False, tag=None, anim=None):
    """A native Hotkey. Its key is the game's default one (keymap.py); its pictogram
    the plugin's for that command when it has one, so a held key looks like its tapped
    neighbours."""
    assert not C.pressable(action), f"{action}: the plugin can press it, use cmd()"
    a = K.BY_ID[action]
    assert a[2] is not None, f"{action} has no default key - it must not get a button"
    if symbol is None:
        symbol, filled = C.command_icon(action)
    return B(kind="hotkey", action=action, label=label, symbol=symbol, filled=filled,
             tag=tag, anim=anim, key=K.key_label(a[2]))


def folder(page, label, symbol, anim=None):
    return B(kind="folder", page=page, label=label, symbol=symbol, anim=anim)


def back():
    return B(kind="back", label="Retour", symbol=C.NAV_ICONS["back"][0])


HOLD = "MAINTENIR"

PAGES = {}          # 15 keys

# ---------------------------------------------------------------------------
# ROOT
# ---------------------------------------------------------------------------
PAGES["root"] = {
    "name": "Knife Rider",
    "keys": {
        (0, 0): folder("combat", "Combat", "my_location", anim="pulse"),
        (1, 0): folder("ciblage", "Ciblage", "filter_center_focus", anim="radar"),
        (2, 0): folder("vol", "Vol", "flight", anim="thrust"),
        (3, 0): folder("vaisseau", "Vaisseau", "rocket", anim="turbine"),
        (4, 0): folder("tablette", "Tablette", "visibility", anim="scan"),

        (0, 1): cmd("tri_weapons"),
        (1, 1): cmd("tri_engine"),
        (2, 1): cmd("tri_shield"),
        (3, 1): cmd("tri_neutral"),
        (4, 1): folder("vues", "Vues & système", "settings"),

        (0, 2): cmd("target_front"),
        (1, 2): cmd("target_next"),
        (2, 2): cmd("target_attacker"),
        (3, 2): hotkey("flares", "Leurres", "flare", anim="flares"),
        (4, 2): hotkey("missile", "Missile", "rocket", filled=True),
    },
}

# ---------------------------------------------------------------------------
# COMBAT
# ---------------------------------------------------------------------------
PAGES["combat"] = {
    "name": "Combat",
    "keys": {
        (0, 0): back(),
        (1, 0): hotkey("fire_group_1", "Tir groupe 1"),
        (2, 0): hotkey("fire_group_2", "Tir groupe 2"),
        (3, 0): hotkey("missile", "Missile", "rocket", filled=True),
        (4, 0): hotkey("flares", "Leurres", "flare"),

        (0, 1): cmd("tri_weapons"),
        (1, 1): cmd("tri_engine"),
        (2, 1): cmd("tri_shield"),
        (3, 1): cmd("tri_neutral"),
        (4, 1): cmd("capacitor_mode"),

        (0, 2): hotkey("missile_hatch", "Trappe missiles", "garage_door"),
        (1, 2): cmd("convergence_down"),
        (2, 2): cmd("convergence_up"),
        (3, 2): cmd("crosshair_color"),
        (4, 2): folder("urgence", "Urgences", "emergency_home"),
    },
}

PAGES["urgence"] = {
    "name": "Urgences",
    "keys": {
        (0, 0): back(),
        (1, 1): hotkey("eject", "S'éjecter", tag=HOLD),
        (3, 1): cmd("self_destruct"),
    },
}

# ---------------------------------------------------------------------------
# CIBLAGE - every targeting command is its own key: no long press any more
# ---------------------------------------------------------------------------
PAGES["ciblage"] = {
    "name": "Ciblage",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("target_front"),
        (2, 0): cmd("target_attacker"),
        (3, 0): cmd("target_prev"),
        (4, 0): cmd("target_next"),

        (0, 1): cmd("target_clear"),
        (1, 1): cmd("target_subsystem"),
        (2, 1): cmd("target_of_target"),
        (3, 1): cmd("target_squad_prev"),
        (4, 1): cmd("target_squad_next"),

        (0, 2): cmd("target_mark"),
        (1, 2): cmd("duel"),
        (2, 2): cmd("free_look"),
        (3, 2): cmd("zoom_toggle"),
        (4, 2): cmd("view_toggle"),
    },
}

# ---------------------------------------------------------------------------
# VOL - the game wants every flight input held: native hotkeys
# ---------------------------------------------------------------------------
PAGES["vol"] = {
    "name": "Commandes de vol",
    "keys": {
        (0, 0): back(),
        (1, 0): hotkey("roll_left", "Roulis gauche"),
        (2, 0): hotkey("pitch_up", "Nez en haut"),
        (3, 0): hotkey("roll_right", "Roulis droite"),
        (4, 0): hotkey("boost", "Boost"),

        (0, 1): hotkey("thrust_fwd", "Poussée avant"),
        (1, 1): hotkey("yaw_left", "Lacet gauche"),
        (2, 1): hotkey("pitch_down", "Nez en bas"),
        (3, 1): hotkey("yaw_right", "Lacet droite"),
        (4, 1): hotkey("thrust_back", "Poussée arrière"),

        (0, 2): hotkey("strafe_left", "Strafe gauche"),
        (1, 2): hotkey("strafe_right", "Strafe droite"),
        (2, 2): hotkey("strafe_up", "Strafe haut"),
        (3, 2): hotkey("strafe_down", "Strafe bas"),
        (4, 2): value("speed"),
    },
}

# ---------------------------------------------------------------------------
# VAISSEAU
# ---------------------------------------------------------------------------
PAGES["vaisseau"] = {
    "name": "Commandes vaisseau",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("engine_toggle"),
        (2, 0): cmd("headlights"),
        (3, 0): cmd("cabin_light"),
        (4, 0): cmd("landing_gear"),

        (0, 1): hotkey("missile_hatch", "Trappe missiles", "garage_door"),
        (1, 1): cmd("station_menu"),
        (2, 1): cmd("turret_seat"),
        (3, 1): cmd("exit_ship"),
        (4, 1): cmd("interact"),

        (0, 2): cmd("practice_panel"),
        (4, 2): value("hull"),
    },
}

# ---------------------------------------------------------------------------
# TABLETTE
# ---------------------------------------------------------------------------
PAGES["tablette"] = {
    "name": "Tablette",
    "keys": {
        (0, 0): back(),
        (2, 0): cmd("tablet_up"),
        (4, 0): cmd("tablet_tab_prev"),

        (0, 1): cmd("tablet_focus"),
        (1, 1): cmd("tablet_left"),
        (2, 1): cmd("tablet_select"),
        (3, 1): cmd("tablet_right"),
        (4, 1): cmd("tablet_tab_next"),

        (0, 2): cmd("tablet_back"),
        (2, 2): cmd("tablet_down"),
    },
}

# ---------------------------------------------------------------------------
# VUES & SYSTEME
# ---------------------------------------------------------------------------
PAGES["vues"] = {
    "name": "Vues & système",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("view_toggle"),
        (2, 0): cmd("free_look"),
        (3, 0): cmd("zoom_toggle"),
        (4, 0): cmd("zoom_closer"),

        (0, 1): cmd("zoom_wider"),
        (1, 1): cmd("head_toggle"),
        (2, 1): cmd("head_center"),
        (3, 1): cmd("input_overlay"),
        (4, 1): cmd("fps_display"),

        (0, 2): cmd("marker"),
        (1, 2): cmd("record_toggle"),
        (2, 2): cmd("chat_open"),
        (3, 2): folder("course", "Course", "sports_score"),
        (4, 2): folder("photo", "Photo", "photo_camera"),
    },
}

PAGES["course"] = {
    "name": "Course",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("race_restart"),
        (2, 0): cmd("race_abandon"),
        (3, 0): cmd("race_trace_gate"),
    },
}

# ---------------------------------------------------------------------------
# PHOTO (new in the game's 0.68) - the adjustments in their own folder
# ---------------------------------------------------------------------------
PAGES["photo"] = {
    "name": "Photo",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("photo_mode"),
        (2, 0): cmd("photo_capture"),
        (3, 0): cmd("photo_hide_ui"),
        (4, 0): cmd("photo_time"),

        (0, 1): cmd("photo_slow"),
        (1, 1): cmd("photo_home"),
        (2, 1): cmd("photo_horizon"),
        (3, 1): cmd("photo_lock"),
        (4, 1): folder("photo_reglages", "Réglages photo", "tune"),
    },
}

PAGES["photo_reglages"] = {
    "name": "Réglages photo",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("photo_smooth_less"),
        (2, 0): cmd("photo_smooth_more"),
        (3, 0): cmd("photo_speed_down"),
        (4, 0): cmd("photo_speed_up"),

        (1, 1): cmd("photo_blur_less"),
        (2, 1): cmd("photo_blur_more"),
        (3, 1): cmd("photo_depth_less"),
        (4, 1): cmd("photo_depth_more"),
    },
}


# ===========================================================================
# STREAM DECK XL (32 keys, 8 x 4)
# The whole fight on the home page, one row per job; folders for the rest.
# ===========================================================================
XL = {}

XL["root"] = {
    "name": "Knife Rider",
    "keys": {
        # energy and weapon settings
        (0, 0): cmd("tri_weapons"),
        (1, 0): cmd("tri_engine"),
        (2, 0): cmd("tri_shield"),
        (3, 0): cmd("tri_neutral"),
        (4, 0): cmd("capacitor_mode"),
        (5, 0): cmd("convergence_down"),
        (6, 0): cmd("convergence_up"),
        (7, 0): value("hull"),
        # weapons
        (0, 1): hotkey("fire_group_1", "Tir groupe 1"),
        (1, 1): hotkey("fire_group_2", "Tir groupe 2"),
        (2, 1): hotkey("missile", "Missile", "rocket", filled=True),
        (3, 1): hotkey("flares", "Leurres", "flare", anim="flares"),
        (4, 1): hotkey("missile_hatch", "Trappe missiles", "garage_door"),
        (5, 1): cmd("duel"),
        (6, 1): cmd("crosshair_color"),
        (7, 1): value("speed"),
        # targeting: find a target, then act on it
        (0, 2): cmd("target_front"),
        (1, 2): cmd("target_attacker"),
        (2, 2): cmd("target_prev"),
        (3, 2): cmd("target_next"),
        (4, 2): cmd("target_subsystem"),
        (5, 2): cmd("target_of_target"),
        (6, 2): cmd("target_clear"),
        (7, 2): cmd("target_mark"),
        # squad, gear, folders
        (0, 3): cmd("target_squad_prev"),
        (1, 3): cmd("target_squad_next"),
        (2, 3): cmd("landing_gear"),
        (3, 3): folder("vol", "Vol", "flight", anim="thrust"),
        (4, 3): folder("vaisseau", "Vaisseau", "rocket", anim="turbine"),
        (5, 3): folder("tablette", "Tablette", "visibility", anim="scan"),
        (6, 3): folder("vues", "Vues & système", "settings"),
        (7, 3): folder("urgence", "Urgences", "emergency_home", anim="pulse"),
    },
}

XL["vol"] = {
    "name": "Commandes de vol",
    "keys": {
        (0, 0): back(),
        # attitude: pitch in the middle, roll above on the sides, yaw below
        (2, 0): hotkey("roll_left", "Roulis gauche"),
        (3, 0): hotkey("pitch_up", "Nez en haut"),
        (4, 0): hotkey("roll_right", "Roulis droite"),
        (2, 1): hotkey("yaw_left", "Lacet gauche"),
        (3, 1): hotkey("pitch_down", "Nez en bas"),
        (4, 1): hotkey("yaw_right", "Lacet droite"),
        # strafe: an inverted T, like the arrow keys
        (6, 0): hotkey("strafe_up", "Strafe haut"),
        (5, 1): hotkey("strafe_left", "Strafe gauche"),
        (6, 1): hotkey("strafe_down", "Strafe bas"),
        (7, 1): hotkey("strafe_right", "Strafe droite"),
        # throttle column
        (0, 1): hotkey("thrust_fwd", "Poussée avant"),
        (1, 1): hotkey("boost", "Boost"),
        (0, 2): hotkey("thrust_back", "Poussée arrière"),
        # what the HUD says
        (0, 3): value("speed"),
        (1, 3): value("throttle"),
        (2, 3): value("g"),
        (3, 3): value("boost"),
    },
}

XL["vaisseau"] = {
    "name": "Commandes vaisseau",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("engine_toggle"),
        (2, 0): cmd("headlights"),
        (3, 0): cmd("cabin_light"),
        (4, 0): cmd("landing_gear"),

        (0, 1): cmd("exit_ship"),
        (1, 1): cmd("interact"),
        (2, 1): cmd("station_menu"),
        (3, 1): cmd("turret_seat"),
        (4, 1): cmd("practice_panel"),

        (0, 3): value("hull"),
        (1, 3): value("energy_weapons"),
        (2, 3): value("energy_engine"),
        (3, 3): value("energy_shield"),
    },
}

XL["tablette"] = {
    "name": "Tablette",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("tablet_focus"),
        (2, 0): cmd("tablet_back"),
        (0, 2): cmd("tablet_tab_prev"),
        (1, 2): cmd("tablet_tab_next"),
        # a d-pad, select in the middle
        (5, 1): cmd("tablet_up"),
        (4, 2): cmd("tablet_left"),
        (5, 2): cmd("tablet_select"),
        (6, 2): cmd("tablet_right"),
        (5, 3): cmd("tablet_down"),
    },
}

XL["vues"] = {
    "name": "Vues & système",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("view_toggle"),
        (2, 0): cmd("free_look"),
        (3, 0): cmd("zoom_toggle"),
        (4, 0): cmd("zoom_closer"),
        (5, 0): cmd("zoom_wider"),
        (6, 0): cmd("head_toggle"),
        (7, 0): cmd("head_center"),

        (0, 1): cmd("input_overlay"),
        (1, 1): cmd("fps_display"),
        (2, 1): cmd("marker"),
        (3, 1): cmd("record_toggle"),
        (4, 1): cmd("chat_open"),

        (0, 2): cmd("race_restart"),
        (1, 2): cmd("race_abandon"),
        (2, 2): cmd("race_trace_gate"),

        (7, 3): folder("photo", "Photo", "photo_camera"),
    },
}

XL["photo"] = {
    "name": "Photo",
    "keys": {
        (0, 0): back(),
        (1, 0): cmd("photo_mode"),
        (2, 0): cmd("photo_capture"),
        (3, 0): cmd("photo_hide_ui"),
        (4, 0): cmd("photo_time"),
        (5, 0): cmd("photo_slow"),
        (6, 0): cmd("photo_home"),
        (7, 0): cmd("photo_horizon"),

        (1, 1): cmd("photo_lock"),
        # adjustments, less / more side by side
        (0, 2): cmd("photo_smooth_less"),
        (1, 2): cmd("photo_smooth_more"),
        (2, 2): cmd("photo_speed_down"),
        (3, 2): cmd("photo_speed_up"),
        (4, 2): cmd("photo_blur_less"),
        (5, 2): cmd("photo_blur_more"),
        (6, 2): cmd("photo_depth_less"),
        (7, 2): cmd("photo_depth_more"),
    },
}

XL["urgence"] = {
    "name": "Urgences",
    "keys": {
        (0, 0): back(),
        (2, 1): hotkey("eject", "S'éjecter", tag=HOLD),
        (5, 1): cmd("self_destruct"),
    },
}


# ===========================================================================
# THE PROFILES
# `seeds` feed every uuid5 of a profile. The 15-key one has none, as in v1: its ids
# must never change (re-importing updates the profile instead of doubling it).
# ===========================================================================
LAYOUTS = [
    {
        "key": "15", "name": "Knife Rider - 15 Key", "model": "20GBA9901",
        "device": "Stream Deck 15 touches (MK.2 / origine)",
        "archive": "KnifeRider-15-touches.streamDeckProfile",
        "cols": 5, "rows": 3, "seeds": (), "slug": "",
        "pages": PAGES, "root": "root",
        "order": ["root", "combat", "urgence", "ciblage", "vol", "vaisseau", "tablette",
                  "vues", "course", "photo", "photo_reglages"],
        "parent": {"combat": "root", "ciblage": "root", "vol": "root", "vaisseau": "root",
                   "tablette": "root", "vues": "root", "urgence": "combat", "course": "vues",
                   "photo": "vues", "photo_reglages": "photo"},
        "titles": {"root": "Accueil", "combat": "Combat", "urgence": "Combat › Urgences",
                   "ciblage": "Ciblage", "vol": "Commandes de vol",
                   "vaisseau": "Commandes vaisseau", "tablette": "Tablette",
                   "vues": "Vues & système", "course": "Vues › Course",
                   "photo": "Vues › Photo", "photo_reglages": "Vues › Photo › Réglages"},
    },
    {
        "key": "xl", "name": "Knife Rider - XL", "model": "20GAT9901",
        "device": "Stream Deck XL (32 touches)",
        "archive": "KnifeRider-XL-32-touches.streamDeckProfile",
        "cols": 8, "rows": 4, "seeds": ("Knife Rider - XL",), "slug": "xl_",
        "pages": XL, "root": "root",
        "order": ["root", "vol", "vaisseau", "tablette", "vues", "photo", "urgence"],
        "parent": {"vol": "root", "vaisseau": "root", "tablette": "root", "vues": "root",
                   "urgence": "root", "photo": "vues"},
        "titles": {"root": "XL · Accueil", "vol": "XL · Commandes de vol",
                   "vaisseau": "XL · Commandes vaisseau", "tablette": "XL · Tablette",
                   "vues": "XL · Vues & système", "photo": "XL · Vues › Photo",
                   "urgence": "XL · Urgences"},
    },
]


def symbols():
    """Every (symbol, filled) the profiles draw themselves or preview: what
    sync_symbols.py fetches into src/symbols/."""
    out = set()
    for page in [p for lay in LAYOUTS for p in lay["pages"].values()]:
        for btn in page["keys"].values():
            if btn.get("symbol"):
                out.add((btn["symbol"], btn.get("filled", False)))
            elif btn["kind"] == "command" and C.command_icon(btn["action"]):
                out.add(C.command_icon(btn["action"]))
            elif btn["kind"] == "value" and btn["field"] in C.FIELD_ICONS:
                out.add(C.FIELD_ICONS[btn["field"]])
    return sorted(out)
