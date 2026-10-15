#!/usr/bin/env python3
"""Fetch the Material Symbols Sharp glyphs the profile draws into src/symbols/.

    python3 src/sync_symbols.py

Same family, weight and version as the Farline companion plugin (and the game's own
screens): npm package @material-symbols/svg-400 0.48.0, Apache License 2.0, by Google.
Only the glyphs layout.py names are kept; the files are committed, so a build never
needs the network. Run it again after adding a pictogram to layout.py.
"""
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import layout as L      # noqa: E402
import tactical as T    # noqa: E402

PACKAGE = "@material-symbols/svg-400@0.48.0"
URL = "https://unpkg.com/{package}/sharp/{name}.svg"


def main():
    os.makedirs(T.SYMBOLS, exist_ok=True)
    wanted = L.symbols()
    fetched = 0
    for symbol, filled in wanted:
        path = T.symbol_file(symbol, filled)
        if os.path.exists(path):
            continue
        name = f"{symbol}-fill" if filled else symbol
        with urllib.request.urlopen(URL.format(package=PACKAGE, name=name), timeout=20) as r:
            data = r.read()
        if b'd="' not in data:
            raise SystemExit(f"{name}: not a Material Symbols file")
        with open(path, "wb") as fh:
            fh.write(data)
        fetched += 1
    keep = {os.path.basename(T.symbol_file(s, f)) for s, f in wanted}
    stale = [f for f in os.listdir(T.SYMBOLS) if f.endswith(".svg") and f not in keep]
    for f in stale:
        os.remove(os.path.join(T.SYMBOLS, f))
    print(f"{len(wanted)} pictos ({fetched} téléchargés, {len(stale)} retirés) -> src/symbols/")


if __name__ == "__main__":
    main()
