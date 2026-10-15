# Polices nécessaires au rendu des touches

Les `.ttf` de ce dossier **ne sont pas versionnés** : ils pèsent lourd pour rien, et
autant pointer vers leur source d'origine.

Depuis la v2, seules deux polices servent (celles que le plugin Farline companion
demande pour ses touches). À déposer ici avec **exactement ces noms** :

| Fichier attendu | Où le prendre | Sert à |
|---|---|---|
| `chakra_petch_bold.ttf` | [Chakra Petch](https://fonts.google.com/specimen/Chakra+Petch) — Bold (700) | titres des planches, chiffres |
| `dm_mono_regular.ttf` | [DM Mono](https://fonts.google.com/specimen/DM+Mono) — Regular (400) | libellés des touches |

Licence : **SIL Open Font License 1.1**. Elles ne servent qu'à générer les images ; le
profil distribué ne contient aucune police.

Les pictogrammes ne viennent plus d'une police : ce sont les fichiers SVG de
`src/symbols/` (Material Symbols Sharp, Apache 2.0), récupérés par
`src/sync_symbols.py`. Les autres `.ttf` éventuellement présents ici (Chakra Petch
SemiBold, DM Mono Medium, Material Symbols) ne sont plus utilisés.
