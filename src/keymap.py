"""Knife Rider — default key bindings and Stream Deck hotkey encoding.

The game's default bindings (alpha 0.65.0, build 20261012-144104). Only the native
hotkeys use them: every action the companion schema also lists is checked against the
schema's default key by validate.py.

Nothing here is guessed: an action with no default key is recorded as None and gets no
button in the profile.
"""

# ---------------------------------------------------------------------------
# Stream Deck key encoding
# ---------------------------------------------------------------------------
# A Stream Deck "Hotkey" action stores up to four key slots. Each slot is
#   {NativeCode, QTKeyCode, VKeyCode, KeyModifiers, KeyCtrl, KeyShift, KeyOption, KeyCmd}
# On Windows NativeCode == VKeyCode for every key except the numeric keypad, where
# QTKeyCode drops back to the plain digit and KeyModifiers carries the keypad flag
# (0x4000). KeyModifiers bits for real modifiers: 1 Shift, 2 Ctrl, 4 Alt, 8 Win.
# Values below were cross-checked against hotkeys written by Stream Deck 6.x itself.

EMPTY_SLOT = {
    "KeyCmd": False, "KeyCtrl": False, "KeyModifiers": 0, "KeyOption": False,
    "KeyShift": False, "NativeCode": 146, "QTKeyCode": 33554431, "VKeyCode": -1,
}

_QT_SPECIAL = 0x01000000   # Qt::Key_Escape and the rest of the special block
_KEYPAD = 0x4000           # Qt::KeypadModifier as Stream Deck writes it


def _plain(vk, qt=None):
    return {"NativeCode": vk, "QTKeyCode": qt if qt is not None else vk, "VKeyCode": vk,
            "KeyModifiers": 0, "KeyCtrl": False, "KeyShift": False,
            "KeyOption": False, "KeyCmd": False}


def _keypad(vk, digit):
    return {"NativeCode": vk, "QTKeyCode": digit, "VKeyCode": vk,
            "KeyModifiers": _KEYPAD, "KeyCtrl": False, "KeyShift": False,
            "KeyOption": False, "KeyCmd": False}


def _modifier(bit, ctrl=False, shift=False, alt=False, cmd=False):
    return {"NativeCode": 146, "QTKeyCode": 33554431, "VKeyCode": -1,
            "KeyModifiers": bit, "KeyCtrl": ctrl, "KeyShift": shift,
            "KeyOption": alt, "KeyCmd": cmd}


# name -> hotkey slot.  `name` is the Godot Key constant without the KEY_ prefix.
KEYS = {}
for _c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    KEYS[_c] = _plain(ord(_c))
for _d in "0123456789":
    KEYS[_d] = _plain(ord(_d))
for _n in range(1, 13):                      # F1..F12
    KEYS[f"F{_n}"] = _plain(111 + _n, _QT_SPECIAL + 0x30 + _n - 1)
for _d in range(10):                         # Numpad 0..9
    KEYS[f"KP_{_d}"] = _keypad(96 + _d, 48 + _d)

KEYS.update({
    "SPACE":     _plain(32, 32),
    "BACKSPACE": _plain(8,  _QT_SPECIAL + 0x03),
    "TAB":       _plain(9,  _QT_SPECIAL + 0x01),
    "ENTER":     _plain(13, _QT_SPECIAL + 0x04),
    "INSERT":    _plain(45, _QT_SPECIAL + 0x06),
    "DELETE":    _plain(46, _QT_SPECIAL + 0x07),
    "HOME":      _plain(36, _QT_SPECIAL + 0x10),
    "END":       _plain(35, _QT_SPECIAL + 0x11),
    "LEFT":      _plain(37, _QT_SPECIAL + 0x12),
    "UP":        _plain(38, _QT_SPECIAL + 0x13),
    "RIGHT":     _plain(39, _QT_SPECIAL + 0x14),
    "DOWN":      _plain(40, _QT_SPECIAL + 0x15),
    "PAGEUP":    _plain(33, _QT_SPECIAL + 0x16),
    "PAGEDOWN":  _plain(34, _QT_SPECIAL + 0x17),
    "ESCAPE":    _plain(27, _QT_SPECIAL + 0x00),
    "SHIFT":     _modifier(1, shift=True),
    "CTRL":      _modifier(2, ctrl=True),
})

# How the key reads on a French (AZERTY) in-game binding screen / on a button badge.
KEY_LABEL_FR = {
    "SPACE": "ESPACE", "BACKSPACE": "RET.ARR", "ENTER": "ENTREE", "DELETE": "SUPPR",
    "INSERT": "INSER", "HOME": "DEBUT", "END": "FIN", "PAGEUP": "PG.PREC",
    "PAGEDOWN": "PG.SUIV", "LEFT": "GAUCHE", "RIGHT": "DROITE", "UP": "HAUT",
    "DOWN": "BAS", "SHIFT": "MAJ", "CTRL": "CTRL", "TAB": "TAB", "ESCAPE": "ECHAP",
    "KP_0": "PAV.0", "KP_1": "PAV.1", "KP_2": "PAV.2", "KP_3": "PAV.3", "KP_4": "PAV.4",
    "KP_5": "PAV.5", "KP_6": "PAV.6", "KP_7": "PAV.7", "KP_8": "PAV.8", "KP_9": "PAV.9",
}


def key_label(name):
    return KEY_LABEL_FR.get(name, name)


def hotkey_settings(*names):
    """Stream Deck `Settings` block for a Hotkey / Hotkey Switch action."""
    slots = [dict(KEYS[n]) for n in names]
    slots += [dict(EMPTY_SLOT) for _ in range(4 - len(slots))]
    return {"Coalesce": True, "Hotkeys": slots}


# ---------------------------------------------------------------------------
# Knife Rider actions
# ---------------------------------------------------------------------------
# (action id, category, default key or None, French label, trigger)
#   trigger: "press" fires on a tap, "long" fires only once the key is held
#            (Knife Rider pairs two targeting commands on one key, see TARGET_PAIRS),
#            "hold" is an action the game itself asks you to hold.
PRESS, LONG, HOLD = "press", "long", "hold"

ACTIONS = [
    # --- Commandes de vol -------------------------------------------------
    ("thrust_fwd",        "vol",     "W",          "Poussée avant",          PRESS),
    ("thrust_back",       "vol",     "S",          "Poussée arrière",        PRESS),
    ("strafe_left",       "vol",     "A",          "Strafe gauche",          PRESS),
    ("strafe_right",      "vol",     "D",          "Strafe droite",          PRESS),
    ("strafe_up",         "vol",     "SPACE",      "Strafe haut",            PRESS),
    ("strafe_down",       "vol",     "CTRL",       "Strafe bas",             PRESS),
    ("roll_left",         "vol",     "Q",          "Roulis gauche",          PRESS),
    ("roll_right",        "vol",     "E",          "Roulis droite",          PRESS),
    ("pitch_up",          "vol",     "UP",         "Tangage : nez en haut",  PRESS),
    ("pitch_down",        "vol",     "DOWN",       "Tangage : nez en bas",   PRESS),
    ("yaw_left",          "vol",     "LEFT",       "Lacet à gauche",         PRESS),
    ("yaw_right",         "vol",     "RIGHT",      "Lacet à droite",         PRESS),
    ("boost",             "vol",     "SHIFT",      "Boost",                  PRESS),
    # --- Combat -----------------------------------------------------------
    ("fire",              "combat",  None,         "Tir tout",               PRESS),
    ("fire_group_1",      "combat",  "1",          "Tir groupe 1",           PRESS),
    ("fire_group_2",      "combat",  "2",          "Tir groupe 2",           PRESS),
    ("tri_weapons",       "combat",  "I",          "Énergie armes",          PRESS),
    ("tri_engine",        "combat",  "J",          "Énergie moteur",         PRESS),
    ("tri_shield",        "combat",  "L",          "Énergie bouclier",       PRESS),
    ("tri_neutral",       "combat",  "K",          "Énergie neutre",         PRESS),
    ("capacitor_mode",    "combat",  "O",          "Capaciteur plein/crans", PRESS),
    ("crosshair_color",   "combat",  "R",          "Couleur du viseur",      PRESS),
    ("conv_far",          "combat",  "T",          "Convergence plus loin",  PRESS),
    ("conv_near",         "combat",  "G",          "Convergence plus près",  PRESS),
    ("eject",             "combat",  "BACKSPACE",  "S'éjecter",              HOLD),
    ("self_destruct",     "combat",  "DELETE",     "Autodestruction",        PRESS),
    ("duel",              "combat",  "3",          "Contact / duel",         PRESS),
    ("call_dismiss",      "combat",  None,         "Écarter l'appel",        PRESS),
    ("missile",           "combat",  "4",          "Missile",                PRESS),
    ("flares",            "combat",  "5",          "Leurres",                PRESS),
    ("missile_hatch",     "combat",  "6",          "Trappe à missiles",      PRESS),
    # --- Ciblage ----------------------------------------------------------
    ("target_front",      "ciblage", "KP_8",       "Cible en face",          PRESS),
    ("target_subsystem",  "ciblage", "KP_8",       "Cibler un sous-système", LONG),
    ("target_attacker",   "ciblage", "KP_2",       "Attaquant le + proche",  PRESS),
    ("target_of_target",  "ciblage", "KP_2",       "Cible de la cible",      LONG),
    ("target_prev",       "ciblage", "X",          "Cible précédente",       PRESS),
    ("target_squad_prev", "ciblage", "X",          "Équipier précédent",     LONG),
    ("target_next",       "ciblage", "C",          "Cible suivante",         PRESS),
    ("target_squad_next", "ciblage", "C",          "Équipier suivant",       LONG),
    ("target_clear",      "ciblage", "KP_5",       "Effacer la cible",       PRESS),
    ("target_mark",       "ciblage", "KP_5",       "Marquer la cible",       LONG),
    # --- Commandes vaisseau -----------------------------------------------
    ("engine_toggle",     "vaisseau", "P",         "Électronique / moteurs", PRESS),
    ("headlights",        "vaisseau", "H",         "Phares",                 PRESS),
    ("cabin_light",       "vaisseau", "N",         "Éclairage cockpit",      PRESS),
    ("landing_gear",      "vaisseau", "B",         "Train d'atterrissage",   PRESS),
    ("exit_ship",         "vaisseau", "Y",         "Sortir du vaisseau",     PRESS),
    ("interact",          "vaisseau", "E",         "Interagir (à pied)",     PRESS),
    ("station_menu",      "vaisseau", "F3",        "Station de maintenance", PRESS),
    ("turret_seat",       "vaisseau", "U",         "Tourelle habitée",       PRESS),
    # --- Tablette ---------------------------------------------------------
    ("tablet_focus",      "tablette", "M",         "Tablette : la main",     PRESS),
    ("tablet_up",         "tablette", "UP",        "Tablette : haut",        PRESS),
    ("tablet_down",       "tablette", "DOWN",      "Tablette : bas",         PRESS),
    ("tablet_left",       "tablette", "LEFT",      "Tablette : gauche",      PRESS),
    ("tablet_right",      "tablette", "RIGHT",     "Tablette : droite",      PRESS),
    ("tablet_select",     "tablette", "ENTER",     "Tablette : valider",     PRESS),
    ("tablet_back",       "tablette", "BACKSPACE", "Tablette : retour",      PRESS),
    ("tablet_tab_prev",   "tablette", "Q",         "Visière : onglet préc.", PRESS),
    ("tablet_tab_next",   "tablette", "E",         "Visière : onglet suiv.", PRESS),
    # --- Vues, système, course -------------------------------------------
    ("view_toggle",       "vues",    "V",          "Vue cockpit / ext.",     PRESS),
    ("free_look",         "vues",    "F",          "Vue libre",              PRESS),
    ("zoom_toggle",       "vues",    "Z",          "Zoom avant / arrière",   PRESS),
    ("zoom_closer",       "vues",    "PAGEUP",     "Zoom : plus près",       PRESS),
    ("zoom_wider",        "vues",    "PAGEDOWN",   "Zoom : plus loin",       PRESS),
    ("head_toggle",       "vues",    "F7",         "Suivi de tête",          PRESS),
    ("head_center",       "vues",    "F8",         "Recentrer le suivi",     PRESS),
    ("input_overlay",     "vues",    "F6",         "Overlay des commandes",  PRESS),
    ("fps_display",       "vues",    "F10",        "Affichage des FPS",      PRESS),
    ("marker",            "vues",    "F9",         "Marquer cet instant",    PRESS),
    ("record_toggle",     "vues",    "F11",        "Enregistrement",         PRESS),
    ("chat_open",         "vues",    "ENTER",      "Écrire dans le chat",    PRESS),
    ("practice_panel",    "vaisseau", "F2",        "Console d'équipe",       PRESS),
    ("race_restart",      "course",  "HOME",       "Course : relancer",      PRESS),
    ("race_abandon",      "course",  "END",        "Course : abandonner",    PRESS),
    ("race_trace_gate",   "course",  "INSERT",     "Traceur de course",      PRESS),
]

BY_ID = {a[0]: a for a in ACTIONS}

# Two targeting commands share one key; the second of each pair fires on a long press.
# (`TargetTriggers.default_trigger`, with the "double click" preference left off.)
TARGET_PAIRS = {
    "target_front": "target_subsystem",
    "target_attacker": "target_of_target",
    "target_prev": "target_squad_prev",
    "target_next": "target_squad_next",
    "target_clear": "target_mark",
}

# Keys the game reserves for its menus; never bound to anything else.
FIXED_KEYS = [("TAB", "Ouvre la page Commandes"), ("ESCAPE", "Menu pause / retour")]

UNBOUND = [a for a in ACTIONS if a[2] is None]


def key_of(action_id):
    return BY_ID[action_id][2]


def label_of(action_id):
    return BY_ID[action_id][3]
