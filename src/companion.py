"""What the Farline companion plugin offers, read from its own files.

`src/companion/` holds two files copied verbatim from the plugin's release
(github.com/david-digitis/Farline-companion, tag v0.1.0, MIT, see LICENSE there):

    schema.json   every command a key may send and every value the game pushes
                  (the game's `companion/schema.json`, copied by the plugin)
    icons.ts      the plugin's pictogram for each command, field and tab

They are never edited here: updating to a new plugin release = copying both again
(docs/MISE-A-JOUR.md).
"""
import json
import os
import re

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "companion")

PLUGIN_UUID = "com.david-digitis.farline-companion"
COMMAND_UUID = f"{PLUGIN_UUID}.command"
VALUE_UUID = f"{PLUGIN_UUID}.value"
PLUGIN_VERSION = "0.1.0.0"          # as the plugin's own master profiles write it
PLUGIN_RELEASE = "v0.1.0"
MIN_GAME = "0.68.0"                  # the release notes of v0.1.0
MIN_SOFTWARE = "7.1"                 # the plugin's manifest

with open(os.path.join(HERE, "schema.json"), encoding="utf-8") as _fh:
    SCHEMA = json.load(_fh)

COMMANDS = {c["id"]: c for c in SCHEMA["commands"]}
FIELDS = {f["id"]: f for f in SCHEMA["fields"]}

# Kinds a key can press in protocol cv 1. "hold" (the axes, boost, fire, eject...) is
# refused by the game; "set" needs a value chosen by the player.
KEY_KINDS = ("press", "delta")


def pressable(command_id):
    c = COMMANDS.get(command_id)
    return c is not None and c["kind"] in KEY_KINDS and not c.get("deprecated", False)


def label(command_id):
    return COMMANDS[command_id]["label_fr"]


def field_label(field_id):
    f = FIELDS[field_id]
    return f.get("label_fr") or f.get("label_en") or field_id


def default_key(command_id):
    return COMMANDS[command_id].get("default_key") or None


def _icons():
    """Parse icons.ts: `id: line("symbol")` / `id: full("symbol")`, table by table."""
    with open(os.path.join(HERE, "icons.ts"), encoding="utf-8") as fh:
        src = fh.read()
    tables = {}
    for name, body in re.findall(r"export const (\w+_ICONS)[^=]*=\s*\{(.*?)\n\};", src, re.S):
        tables[name] = {k.strip(): (sym, kind == "full") for k, kind, sym in
                        re.findall(r'"?([\w ]+?)"?:\s*(line|full)\("(\w+)"\)', body)}
    label_only = set(re.findall(r'"(\w+)"', re.search(r"LABEL_ONLY = new Set\(\[(.*?)\]\)",
                                                       src).group(1)))
    return tables, label_only


_TABLES, LABEL_ONLY = _icons()
COMMAND_ICONS = _TABLES["COMMAND_ICONS"]
FIELD_ICONS = _TABLES["FIELD_ICONS"]
TAB_ICONS = _TABLES["TAB_ICONS"]
NAV_ICONS = _TABLES["NAV_ICONS"]


def command_icon(command_id):
    """(symbol, filled) as the plugin draws the command, or None for a label alone."""
    return None if command_id in LABEL_ONLY else COMMAND_ICONS.get(command_id)
