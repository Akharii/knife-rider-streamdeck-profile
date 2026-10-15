# Reconstruire et mettre à jour les profils

Les deux `.streamDeckProfile` de la racine sont **générés** par les scripts de `src/`.
On ne les modifie jamais à la main : on change `src/layout.py` (ou les fichiers du
plugin), puis on reconstruit.

## Reconstruire

```bash
python3 -m venv .venv && . .venv/bin/activate     # Windows : .venv\Scripts\activate
pip install -r requirements.txt

# déposer les 2 polices dans src/fonts/ (voir src/fonts/OU-LES-TROUVER.md)

python3 src/build.py       # images + les deux profils + docs générées
python3 src/preview.py     # planches assets/preview/
python3 src/validate.py    # contrôles structurels : doit finir par « aucun échec »
```

| Fichier | Rôle |
|---|---|
| `src/layout.py` | Le plan des pages, 15 touches puis XL : `(colonne, ligne) → cmd() / value() / hotkey() / folder()`, et `LAYOUTS` qui décrit chaque profil |
| `src/companion/` | `schema.json` et `icons.ts` du plugin Farline companion, copiés tels quels (licence MIT, voir `LICENSE`) |
| `src/companion.py` | Lit ces deux fichiers : commandes, libellés, pictogrammes |
| `src/keymap.py` | Touches par défaut du jeu et leur encodage Stream Deck (touches clavier) |
| `src/tactical.py` | Rendu des touches dans le style du plugin, animations |
| `src/symbols/` | Pictogrammes Material Symbols Sharp (SVG), via `src/sync_symbols.py` |
| `src/build.py` | Assemblage des `.streamDeckProfile` + génération de `docs/` |
| `src/validate.py` | Contrôles structurels sur les profils produits |
| `src/preview.py` | Planches PNG de `assets/preview/` |

### Quatre sortes de touches

- `cmd("id")` — une touche du plugin : elle envoie la commande `id` du jeu et le plugin
  dessine elle-même son visage (libellé, pictogramme, état).
- `value("champ")` — une touche du plugin qui affiche une valeur du HUD.
- `hotkey("id", ...)` — une touche clavier native, **seulement** pour ce que le plugin
  ne sait pas envoyer : les actions à maintenir (`hold` dans le schéma) et celles
  absentes du schéma. `layout.py` refuse une touche clavier pour une commande que le
  plugin sait envoyer, et l'inverse.
- `folder(...)` / `back()` — la navigation.

`validate.py` vérifie, dans chaque profil, que chaque commande du schéma a son bouton,
que chaque touche clavier tape la touche que le schéma annonce, et qu'aucune touche
n'est inventée.

## Ne jamais changer l'identité d'un profil

Tous les identifiants d'un profil (profil, pages, boutons) sont dérivés de son nom par
`uuid5` : ils sont **déterministes**. Reconstruire produit le même profil, et
réimporter **met à jour** celui du joueur au lieu d'en créer un second.

> ⚠️ Ne jamais modifier `PROFILE_ID` dans `src/build.py`, ni le `name` et les
> `seeds` d'un profil dans `layout.LAYOUTS`. Le numéro de version vit dans `VERSION`.

## Nouvelle version du plugin

Dans la release du plugin Farline companion (ou son dépôt, au tag de la release),
reprendre **tels quels** :

| Fichier du plugin | Copie ici |
|---|---|
| `schema.json` | `src/companion/schema.json` |
| `src/icons.ts` | `src/companion/icons.ts` |

Puis, dans `src/companion.py`, mettre à jour `PLUGIN_RELEASE`, `PLUGIN_VERSION` (celle
du `manifest.json` du plugin), `MIN_GAME` et `MIN_SOFTWARE` (les notes de release).

```bash
python3 src/sync_symbols.py   # pictogrammes nouveaux ou retirés
python3 src/build.py && python3 src/validate.py
```

`validate.py` dit ce qui manque : une **nouvelle commande** sans bouton (à placer avec
`cmd("id")` dans `src/layout.py`, **dans les deux profils**), une commande devenue
**à maintenir** (à passer en `hotkey()`), ou l'inverse.

Si le style du plugin change (`src/render.ts`, `src/palette.ts`), reporter les
changements dans `src/tactical.py`, qui en est le portage.

## Nouvelle version du jeu

Les touches plugin ne bougent pas : elles nomment une commande par son identifiant,
que le jeu ne renomme jamais. Pour les touches clavier, `validate.py` compare
`src/keymap.py` au schéma du plugin. Seules les actions **hors schéma** (missile,
leurres, trappe) se vérifient à la main, dans l'écran *Commandes* du jeu.

## Publier

1. Monter `VERSION`.
2. Ajouter une entrée dans `CHANGELOG.md` (ce qui change pour les joueurs en premier).
3. `python3 src/build.py && python3 src/preview.py && python3 src/validate.py`.
4. Importer réellement les profils, appairer, appuyer sur quelques touches en jeu :
   `validate.py` ne contrôle que la structure.
5. Commiter et pousser.

| Changement | Version |
|---|---|
| Correction d'image, de libellé, de doc | `2.0.x` |
| Touches modifiées, boutons ajoutés ou déplacés, nouvelle version du plugin | `2.x.0` |
| Refonte de la disposition, nouveau modèle de Stream Deck, plugin remplacé | `x.0.0` |
