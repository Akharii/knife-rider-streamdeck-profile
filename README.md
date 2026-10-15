# Knife Rider — profils Stream Deck

Deux profils Stream Deck prêts à importer pour **Knife Rider** :

| Fichier | Appareil |
|---|---|
| [`KnifeRider-15-touches.streamDeckProfile`](KnifeRider-15-touches.streamDeckProfile) | Stream Deck 15 touches (MK.2 ou modèle d'origine) |
| [`KnifeRider-XL-32-touches.streamDeckProfile`](KnifeRider-XL-32-touches.streamDeckProfile) | Stream Deck XL (32 touches) |

> **Ces profils s'appuient sur le plugin
> [Farline companion](https://github.com/david-digitis/Farline-companion).** C'est
> lui qui relie le Stream Deck au jeu : les touches envoient les commandes directement
> à Knife Rider et affichent ce que montre le HUD (train sorti, phares, part
> d'énergie, convergence, vitesse, coque…). Ces profils en sont une disposition,
> pensée pour 15 et 32 touches.

## Il faut

- **Knife Rider 0.68.0** ou plus récent
- Le logiciel **Stream Deck 7.1** ou plus récent, sous Windows
- Le plugin **Farline companion** :
  [page des releases](https://github.com/david-digitis/Farline-companion/releases)

## Installation

1. **Le plugin** : dans les [releases du companion](https://github.com/david-digitis/Farline-companion/releases),
   télécharger `com.david-digitis.farline-companion.streamDeckPlugin`, double-cliquer
   dessus, puis *Installer*.
2. **Le profil** : télécharger celui de votre appareil (cliquer sur le fichier
   ci-dessus, puis sur le bouton de téléchargement), double-cliquer dessus.
3. En haut de la fenêtre Stream Deck, choisir **Knife Rider - 15 Key** ou
   **Knife Rider - XL**.
4. **Appairer**, une seule fois :
   - dans le jeu : *Commandes › Companion*, cocher **Activer le companion**, puis
     **Appairer un appareil** : un code à 6 chiffres s'affiche, valable 2 minutes ;
   - dans Stream Deck : cliquer sur une touche qui passe par le plugin (une touche
     d'énergie par exemple), taper le code dans **Code affiché dans le jeu**, puis
     **Appairer**.

**Conseillé** : dans *Préférences › Profils*, associer le profil à `KNIFE-RIDER.exe`,
pour qu'il ne s'affiche que quand le jeu est au premier plan.

Vous aviez la première version du profil 15 touches ? Réimporter la remplace, sans
créer de doublon.

## Ce qu'il y a dedans

**15 touches** — 11 pages. L'accueil donne les familles en dossiers et le combat
immédiat :

```
COMBAT      CIBLAGE     VOL         VAISSEAU    TABLETTE
ÉN. ARMES   ÉN. MOTEUR  ÉN. BOUCL.  ÉN. NEUTRE  VUES & SYSTÈME
CIBLE FACE  CIBLE SUIV. ATTAQUANT   LEURRES     MISSILE
```

Dossiers : Combat (+ Urgences), Ciblage, Vol, Vaisseau, Tablette, Vues & système
(+ Course, + Photo et ses réglages).

**XL (32 touches)** — 7 pages. Tout le combat tient sur l'accueil :

```
ÉN.ARMES   ÉN.MOTEUR  ÉN.BOUCL.  ÉN.NEUTRE  CAPACIT.   CONV −     CONV +     COQUE
TIR G1     TIR G2     MISSILE    LEURRES    TRAPPE     DUEL       VISEUR     VITESSE
CIBLE FACE ATTAQUANT  CIBLE PRÉC CIBLE SUIV SOUS-SYST. CIBLE/CIB. EFFACER    MARQUER
ÉQUIP.PRÉC ÉQUIP.SUIV TRAIN      VOL        VAISSEAU   TABLETTE   VUES       URGENCES
```

Dossiers : Vol (commandes groupées comme au clavier, avec vitesse, gaz, g et boost
affichés), Vaisseau (avec les jauges de coque et d'énergie), Tablette (en croix),
Vues & système (+ course, + Photo), Urgences.

## Deux sortes de touches

La plupart des touches **passent par le plugin** : elles marchent même si vous avez
changé vos touches dans le jeu, ne font rien hors du jeu, et s'allument selon l'état
du jeu. Une touche qui passe un instant en corail : le jeu a refusé la commande, la
raison est écrite dessus.

Quelques touches **tapent une touche clavier**, parce que le plugin ne peut pas les
envoyer : celles qu'on **maintient** (poussée, strafe, roulis, tangage, lacet, boost,
tir groupe 1 et 2, éjection) et missile / leurres / trappe à missiles. Elles tapent
les touches **par défaut** du jeu (la touche est écrite en haut à droite) : si vous
les avez changées dans le jeu, celles-là ne suivront pas. Elles envoient aussi leur
touche à la fenêtre active hors du jeu, d'où le conseil d'associer le profil à
`KNIFE-RIDER.exe`.

## Bon à savoir

- **S'éjecter** : maintenir la touche, comme dans le jeu.
- **Tir tout** et **Écarter l'appel** n'ont pas de bouton : ils n'ont aucune touche
  par défaut dans le jeu.
- Les animations des dossiers (radar, turbine, balayage…) sont décoratives. L'état
  réel du jeu, ce sont les touches du plugin qui l'affichent.
- **Première version sur le plugin** : si une touche ne fait pas ce qu'elle annonce
  (missile, leurres et trappe en particulier), ouvrez une *issue* ici.

## Crédits

- **[Farline companion](https://github.com/david-digitis/Farline-companion)**
  (licence MIT) : le plugin, la liste des commandes du jeu et le style des touches,
  que ces profils reprennent.
- Pictogrammes : Material Symbols Sharp, Google (Apache License 2.0).
- Polices des libellés : Chakra Petch et DM Mono (SIL Open Font License 1.1).

---

## English

Two ready-to-import Stream Deck profiles for **Knife Rider**: 15 keys
(`KnifeRider-15-touches.streamDeckProfile`) and XL, 32 keys
(`KnifeRider-XL-32-touches.streamDeckProfile`). Folder names and hotkey labels are in
French; the plugin's keys follow your Stream Deck language.

They are built on the **[Farline companion](https://github.com/david-digitis/Farline-companion)
plugin**, which links the Stream Deck to the game: keys send commands straight to
Knife Rider and show what the HUD shows. These profiles are a layout on top of it.

Needs Knife Rider 0.68.0+, Stream Deck software 7.1+ on Windows, and the plugin
([releases](https://github.com/david-digitis/Farline-companion/releases)). Install
the plugin, double-click the profile for your device, then pair once: in the game,
*Controls › Companion › Enable the companion › Pair a device*, and type the six-digit
code in any plugin key's settings in Stream Deck.

Keys the game wants held (flight, boost, fire groups, eject) and missile / flares /
missile hatch are native hotkeys with the game's **default** keys, since the plugin
cannot send them.
