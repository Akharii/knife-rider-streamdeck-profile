# Journal des versions

## 2.0.0 — 2026-10-15

Le profil passe sur le **plugin Farline companion** (v0.1.0). Il faut
désormais le jeu en **0.68.0** ou plus et le logiciel Stream Deck **7.1** ou plus.

- **Nouveau profil Stream Deck XL (32 touches)**, `Knife Rider - XL` : tout le
  combat sur la page d'accueil (énergie, armes, les dix commandes de ciblage, train),
  et 6 dossiers qui profitent de la place (Vol en grappes avec 4 valeurs, Vaisseau
  avec les jauges, Tablette en croix, Vues avec la course, Photo sur une page,
  Urgences). Son propre identifiant : il ne touche pas au profil 15 touches.
- Les deux profils sont à la racine du dépôt :
  `KnifeRider-15-touches.streamDeckProfile` et `KnifeRider-XL-32-touches.streamDeckProfile`.

Profil 15 touches :

- **79 touches passent par le plugin** : elles envoient la commande au jeu par sa
  connexion locale, au lieu de taper une touche clavier.
  - Elles marchent même si vous avez changé vos touches dans le jeu.
  - Hors du jeu, elles ne tapent rien : plus de `Suppr` dans l'explorateur de
    fichiers pour *Autodestruction*.
  - Elles **affichent l'état** qu'elles changent : train sorti, phares, moteurs,
    part d'énergie, capaciteur, convergence, suivi de tête, vue.
- **Ciblage sans appui long** : les dix commandes de ciblage ont chacune leur touche,
  en appui simple. Fini les cadres en pointillés et la pastille `LONG`.
- **Convergence** : les deux touches passent sur `convergence_up` / `_down` du
  plugin et affichent la distance.
- **Nouveau dossier Photo** (Vues › Photo, + Réglages) : les 16 commandes du mode
  photo de la 0.68.
- **Deux valeurs affichées** : vitesse (page Vol) et coque (page Vaisseau).
- **Style du plugin partout** : dossiers, Retour et touches clavier sont redessinés
  dans le style Tactical du plugin (pictogramme Material Symbols Sharp, encre, coins
  nets, sans lueur). Les 6 animations restent, redessinées à plat et **en encre
  seulement** : la menthe est la couleur « actif » du plugin, une animation ne doit
  jamais passer pour un état.
- **Restent en touches clavier** (le plugin ne sait pas les envoyer) : les actions à
  maintenir (vol, boost, tir groupe 1 / 2, éjection) et missile / leurres / trappe à
  missiles, absents du schéma du companion.
- Format d'archive Stream Deck 7 (`package.json` qui exige le plugin : l'import
  propose de l'installer). Identifiant de profil inchangé : réimporter **remplace**
  la v1.
- `src/validate.py` : 1 664 contrôles sur les deux profils, dont chaque commande
  vérifiée contre le schéma du jeu.

### Reste à faire

- Vérifier en 0.68 que **missile (`4`), leurres (`5`) et trappe (`6`)** existent
  toujours : ils ne sont plus dans le schéma du companion.
- Import réel dans le logiciel Stream Deck, appairage, test des touches en jeu.

## 1.0.0 — 2026-10-14

Première version.

- Profil Stream Deck 15 touches (5 × 3, modèle `20GBA9901`), format de profil 3.0.
- 9 pages : accueil + Combat (+ Urgences), Ciblage, Vol, Vaisseau, Tablette,
  Vues & système (+ Course).
- 101 boutons, **72 des 74 actions** de Knife Rider ayant une touche par défaut.
  `fire` et `call_dismiss` n'en ont pas dans le jeu : aucun bouton, aucune touche
  inventée.
- Touches par défaut du jeu (alpha 0.65.0, build 20261012-144104), recoupées avec
  l'écran Commandes du jeu.
- Icônes générées aux couleurs, aux coins biseautés et avec les polices du jeu ;
  6 icônes animées (WebP 144 px, copies GIF dans `assets/icons/`).
- Aucun plugin tiers, aucun chemin absolu, aucun numéro de série d'appareil.
- `src/validate.py` : 924 contrôles structurels.
