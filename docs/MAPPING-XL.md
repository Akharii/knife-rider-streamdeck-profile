# Table de correspondance — Stream Deck XL (32 touches)

Profil « Knife Rider - XL » v2.0.0 — généré par `src/build.py`. Jeu : Knife Rider 0.68.0 ou plus récent, schéma du companion v0.1.0.

- **plugin** : la touche passe par le plugin Farline companion. Elle marche quelle
  que soit la touche clavier que vous avez choisie dans le jeu.
- **touche clavier** : la touche Stream Deck tape la touche **par défaut** du jeu.
  Seulement pour ce que le plugin ne sait pas faire : les actions à maintenir
  (vol, boost, tir, éjection) et missile / leurres / trappe, absents de son schéma.

| Page | Bouton | Libellé | Commande | Par | Touche |
|---|---|---|---|---|---|
| XL · Accueil | col 1 / ligne 1 | Énergie vers les armes | `tri_weapons` | plugin | — |
| XL · Accueil | col 2 / ligne 1 | Énergie vers le moteur | `tri_engine` | plugin | — |
| XL · Accueil | col 3 / ligne 1 | Énergie vers le bouclier | `tri_shield` | plugin | — |
| XL · Accueil | col 4 / ligne 1 | Énergie au neutre | `tri_neutral` | plugin | — |
| XL · Accueil | col 5 / ligne 1 | Capaciteur : mode plein / par crans | `capacitor_mode` | plugin | — |
| XL · Accueil | col 6 / ligne 1 | Convergence plus près (un cran) | `convergence_down` | plugin | — |
| XL · Accueil | col 7 / ligne 1 | Convergence plus loin (un cran) | `convergence_up` | plugin | — |
| XL · Accueil | col 8 / ligne 1 | Coque | `hull` (valeur) | plugin | — |
| XL · Accueil | col 1 / ligne 2 | Tir groupe 1 | `fire_group_1` | touche clavier | `1` |
| XL · Accueil | col 2 / ligne 2 | Tir groupe 2 | `fire_group_2` | touche clavier | `2` |
| XL · Accueil | col 3 / ligne 2 | Missile | `missile` | touche clavier | `4` |
| XL · Accueil | col 4 / ligne 2 | Leurres | `flares` | touche clavier | `5` |
| XL · Accueil | col 5 / ligne 2 | Trappe missiles | `missile_hatch` | touche clavier | `6` |
| XL · Accueil | col 6 / ligne 2 | Contact : la roue sur la cible (duel, ami, squad), accepter, revanche (en ligne) | `duel` | plugin | — |
| XL · Accueil | col 7 / ligne 2 | Couleur du viseur | `crosshair_color` | plugin | — |
| XL · Accueil | col 8 / ligne 2 | Vitesse | `speed` (valeur) | plugin | — |
| XL · Accueil | col 1 / ligne 3 | Cible en face (la plus proche du viseur) | `target_front` | plugin | — |
| XL · Accueil | col 2 / ligne 3 | Attaquant le plus proche, puis le suivant | `target_attacker` | plugin | — |
| XL · Accueil | col 3 / ligne 3 | Cible précédente | `target_prev` | plugin | — |
| XL · Accueil | col 4 / ligne 3 | Cible suivante | `target_next` | plugin | — |
| XL · Accueil | col 5 / ligne 3 | Cibler un sous-système | `target_subsystem` | plugin | — |
| XL · Accueil | col 6 / ligne 3 | Cible de la cible | `target_of_target` | plugin | — |
| XL · Accueil | col 7 / ligne 3 | Effacer la cible | `target_clear` | plugin | — |
| XL · Accueil | col 8 / ligne 3 | Marquer la cible pour la squad | `target_mark` | plugin | — |
| XL · Accueil | col 1 / ligne 4 | Équipier précédent | `target_squad_prev` | plugin | — |
| XL · Accueil | col 2 / ligne 4 | Équipier suivant | `target_squad_next` | plugin | — |
| XL · Accueil | col 3 / ligne 4 | Train d'atterrissage sorti / rentré | `landing_gear` | plugin | — |
| XL · Commandes de vol | col 3 / ligne 1 | Roulis gauche | `roll_left` | touche clavier | `Q` |
| XL · Commandes de vol | col 4 / ligne 1 | Nez en haut | `pitch_up` | touche clavier | `HAUT` |
| XL · Commandes de vol | col 5 / ligne 1 | Roulis droite | `roll_right` | touche clavier | `E` |
| XL · Commandes de vol | col 7 / ligne 1 | Strafe haut | `strafe_up` | touche clavier | `ESPACE` |
| XL · Commandes de vol | col 1 / ligne 2 | Poussée avant | `thrust_fwd` | touche clavier | `W` |
| XL · Commandes de vol | col 2 / ligne 2 | Boost | `boost` | touche clavier | `MAJ` |
| XL · Commandes de vol | col 3 / ligne 2 | Lacet gauche | `yaw_left` | touche clavier | `GAUCHE` |
| XL · Commandes de vol | col 4 / ligne 2 | Nez en bas | `pitch_down` | touche clavier | `BAS` |
| XL · Commandes de vol | col 5 / ligne 2 | Lacet droite | `yaw_right` | touche clavier | `DROITE` |
| XL · Commandes de vol | col 6 / ligne 2 | Strafe gauche | `strafe_left` | touche clavier | `A` |
| XL · Commandes de vol | col 7 / ligne 2 | Strafe bas | `strafe_down` | touche clavier | `CTRL` |
| XL · Commandes de vol | col 8 / ligne 2 | Strafe droite | `strafe_right` | touche clavier | `D` |
| XL · Commandes de vol | col 1 / ligne 3 | Poussée arrière | `thrust_back` | touche clavier | `S` |
| XL · Commandes de vol | col 1 / ligne 4 | Vitesse | `speed` (valeur) | plugin | — |
| XL · Commandes de vol | col 2 / ligne 4 | Gaz | `throttle` (valeur) | plugin | — |
| XL · Commandes de vol | col 3 / ligne 4 | Facteur de charge (g) | `g` (valeur) | plugin | — |
| XL · Commandes de vol | col 4 / ligne 4 | Boost | `boost` (valeur) | plugin | — |
| XL · Commandes vaisseau | col 2 / ligne 1 | Électronique, puis moteurs (et retour : moteurs, puis électronique) | `engine_toggle` | plugin | — |
| XL · Commandes vaisseau | col 3 / ligne 1 | Phares allumés / éteints | `headlights` | plugin | — |
| XL · Commandes vaisseau | col 4 / ligne 1 | Éclairage du cockpit allumé / éteint | `cabin_light` | plugin | — |
| XL · Commandes vaisseau | col 5 / ligne 1 | Train d'atterrissage sorti / rentré | `landing_gear` | plugin | — |
| XL · Commandes vaisseau | col 1 / ligne 2 | Sortir du vaisseau (arrêté, dans un hangar) | `exit_ship` | plugin | — |
| XL · Commandes vaisseau | col 2 / ligne 2 | À pied : prendre le vaisseau, la console ou la boutique regardés | `interact` | plugin | — |
| XL · Commandes vaisseau | col 3 / ligne 2 | Ouvrir la station de maintenance (arrêté dans sa baie) | `station_menu` | plugin | — |
| XL · Commandes vaisseau | col 4 / ligne 2 | Tourelle habitée : y aller / revenir au poste de pilotage | `turret_seat` | plugin | — |
| XL · Commandes vaisseau | col 5 / ligne 2 | Console d'équipe : réglages, Armurerie, banc d'essai | `practice_panel` | plugin | — |
| XL · Commandes vaisseau | col 1 / ligne 4 | Coque | `hull` (valeur) | plugin | — |
| XL · Commandes vaisseau | col 2 / ligne 4 | Énergie armes | `energy_weapons` (valeur) | plugin | — |
| XL · Commandes vaisseau | col 3 / ligne 4 | Énergie moteur | `energy_engine` (valeur) | plugin | — |
| XL · Commandes vaisseau | col 4 / ligne 4 | Bouclier | `energy_shield` (valeur) | plugin | — |
| XL · Tablette | col 2 / ligne 1 | Tablette : prendre / rendre la main | `tablet_focus` | plugin | — |
| XL · Tablette | col 3 / ligne 1 | Tablette : retour | `tablet_back` | plugin | — |
| XL · Tablette | col 6 / ligne 2 | Tablette : haut | `tablet_up` | plugin | — |
| XL · Tablette | col 1 / ligne 3 | Visière : onglet précédent | `tablet_tab_prev` | plugin | — |
| XL · Tablette | col 2 / ligne 3 | Visière : onglet suivant | `tablet_tab_next` | plugin | — |
| XL · Tablette | col 5 / ligne 3 | Tablette : gauche (onglet précédent) | `tablet_left` | plugin | — |
| XL · Tablette | col 6 / ligne 3 | Tablette : valider | `tablet_select` | plugin | — |
| XL · Tablette | col 7 / ligne 3 | Tablette : droite (onglet suivant) | `tablet_right` | plugin | — |
| XL · Tablette | col 6 / ligne 4 | Tablette : bas | `tablet_down` | plugin | — |
| XL · Vues & système | col 2 / ligne 1 | Vue cockpit / extérieure (à pied : 1re / 3e personne) | `view_toggle` | plugin | — |
| XL · Vues & système | col 3 / ligne 1 | Vue libre : la souris tourne la vue, plus le vaisseau | `free_look` | plugin | — |
| XL · Vues & système | col 4 / ligne 1 | Zoom avant / arrière | `zoom_toggle` | plugin | — |
| XL · Vues & système | col 5 / ligne 1 | Zoom : plus près | `zoom_closer` | plugin | — |
| XL · Vues & système | col 6 / ligne 1 | Zoom : plus loin | `zoom_wider` | plugin | — |
| XL · Vues & système | col 7 / ligne 1 | Suivi de tête activé / coupé | `head_toggle` | plugin | — |
| XL · Vues & système | col 8 / ligne 1 | Recentrer le suivi de tête | `head_center` | plugin | — |
| XL · Vues & système | col 1 / ligne 2 | Overlay des commandes affiché / caché (manches, pour le stream) | `input_overlay` | plugin | — |
| XL · Vues & système | col 2 / ligne 2 | Affichage des FPS (client, serveur, les deux, rien) | `fps_display` | plugin | — |
| XL · Vues & système | col 3 / ligne 2 | Marquer cet instant (enregistreur de vol) | `marker` | plugin | — |
| XL · Vues & système | col 4 / ligne 2 | Enregistrement (combat ou manœuvre) : démarrer / arrêter (équipe) | `record_toggle` | plugin | — |
| XL · Vues & système | col 5 / ligne 2 | Écrire dans le chat | `chat_open` | plugin | — |
| XL · Vues & système | col 1 / ligne 3 | Course : repartir avant la ligne de départ (solo) | `race_restart` | plugin | — |
| XL · Vues & système | col 2 / ligne 3 | Course : abandonner la course | `race_abandon` | plugin | — |
| XL · Vues & système | col 3 / ligne 3 | Traceur : départ et portes de course (solo, équipe) | `race_trace_gate` | plugin | — |
| XL · Vues › Photo | col 2 / ligne 1 | Mode photo : entrer / sortir (Échap en sort aussi) | `photo_mode` | plugin | — |
| XL · Vues › Photo | col 3 / ligne 1 | Photo : prendre la photo (sans interface) | `photo_capture` | plugin | — |
| XL · Vues › Photo | col 4 / ligne 1 | Photo : cacher / montrer toute l'interface | `photo_hide_ui` | plugin | — |
| XL · Vues › Photo | col 5 / ligne 1 | Photo : figer / relancer le temps (solo) | `photo_time` | plugin | — |
| XL · Vues › Photo | col 6 / ligne 1 | Photo : lent (maintenir) | `photo_slow` | plugin | — |
| XL · Vues › Photo | col 7 / ligne 1 | Photo : revenir derrière votre vaisseau | `photo_home` | plugin | — |
| XL · Vues › Photo | col 8 / ligne 1 | Photo : horizon verrouillé / libre | `photo_horizon` | plugin | — |
| XL · Vues › Photo | col 2 / ligne 2 | Photo : verrouiller sur le vaisseau devant / caméra libre | `photo_lock` | plugin | — |
| XL · Vues › Photo | col 1 / ligne 3 | Photo : mouvements plus vifs (moins de lissage) | `photo_smooth_less` | plugin | — |
| XL · Vues › Photo | col 2 / ligne 3 | Photo : mouvements plus doux (plus de lissage) | `photo_smooth_more` | plugin | — |
| XL · Vues › Photo | col 3 / ligne 3 | Photo : vitesse max plus basse | `photo_speed_down` | plugin | — |
| XL · Vues › Photo | col 4 / ligne 3 | Photo : vitesse max plus haute | `photo_speed_up` | plugin | — |
| XL · Vues › Photo | col 5 / ligne 3 | Photo : moins de flou (profondeur de champ, verrouillé sur une cible) | `photo_blur_less` | plugin | — |
| XL · Vues › Photo | col 6 / ligne 3 | Photo : plus de flou | `photo_blur_more` | plugin | — |
| XL · Vues › Photo | col 7 / ligne 3 | Photo : zone nette moins profonde | `photo_depth_less` | plugin | — |
| XL · Vues › Photo | col 8 / ligne 3 | Photo : zone nette plus profonde | `photo_depth_more` | plugin | — |
| XL · Urgences | col 3 / ligne 2 | S'éjecter | `eject` | touche clavier | `RET.ARR` |
| XL · Urgences | col 6 / ligne 2 | Autodestruction (appuyer de nouveau pour annuler) | `self_destruct` | plugin | — |

## Commandes sans bouton

| Commande | Libellé | Pourquoi |
|---|---|---|
| `fire` | Tir tout | à maintenir et sans touche par défaut (clic gauche souris) |
| `call_dismiss` | Écarter l'appel (ce que fait le maintien de Contact) | aucune touche par défaut, le plugin la refuserait (`unbound`) |
| `convergence` | Distance de convergence | demande une distance choisie : à régler soi-même dans le plugin |

## Touches réservées par le jeu

| Touche | Rôle |
|---|---|
| `TAB` | Ouvre la page Commandes |
| `ECHAP` | Menu pause / retour |
