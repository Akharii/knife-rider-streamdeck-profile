# Table de correspondance — Stream Deck 15 touches (MK.2 / origine)

Profil « Knife Rider - 15 Key » v2.0.0 — généré par `src/build.py`. Jeu : Knife Rider 0.68.0 ou plus récent, schéma du companion v0.1.0.

- **plugin** : la touche passe par le plugin Farline companion. Elle marche quelle
  que soit la touche clavier que vous avez choisie dans le jeu.
- **touche clavier** : la touche Stream Deck tape la touche **par défaut** du jeu.
  Seulement pour ce que le plugin ne sait pas faire : les actions à maintenir
  (vol, boost, tir, éjection) et missile / leurres / trappe, absents de son schéma.

| Page | Bouton | Libellé | Commande | Par | Touche |
|---|---|---|---|---|---|
| Accueil | col 1 / ligne 2 | Énergie vers les armes | `tri_weapons` | plugin | — |
| Accueil | col 2 / ligne 2 | Énergie vers le moteur | `tri_engine` | plugin | — |
| Accueil | col 3 / ligne 2 | Énergie vers le bouclier | `tri_shield` | plugin | — |
| Accueil | col 4 / ligne 2 | Énergie au neutre | `tri_neutral` | plugin | — |
| Accueil | col 1 / ligne 3 | Cible en face (la plus proche du viseur) | `target_front` | plugin | — |
| Accueil | col 2 / ligne 3 | Cible suivante | `target_next` | plugin | — |
| Accueil | col 3 / ligne 3 | Attaquant le plus proche, puis le suivant | `target_attacker` | plugin | — |
| Accueil | col 4 / ligne 3 | Leurres | `flares` | touche clavier | `5` |
| Accueil | col 5 / ligne 3 | Missile | `missile` | touche clavier | `4` |
| Combat | col 2 / ligne 1 | Tir groupe 1 | `fire_group_1` | touche clavier | `1` |
| Combat | col 3 / ligne 1 | Tir groupe 2 | `fire_group_2` | touche clavier | `2` |
| Combat | col 4 / ligne 1 | Missile | `missile` | touche clavier | `4` |
| Combat | col 5 / ligne 1 | Leurres | `flares` | touche clavier | `5` |
| Combat | col 1 / ligne 2 | Énergie vers les armes | `tri_weapons` | plugin | — |
| Combat | col 2 / ligne 2 | Énergie vers le moteur | `tri_engine` | plugin | — |
| Combat | col 3 / ligne 2 | Énergie vers le bouclier | `tri_shield` | plugin | — |
| Combat | col 4 / ligne 2 | Énergie au neutre | `tri_neutral` | plugin | — |
| Combat | col 5 / ligne 2 | Capaciteur : mode plein / par crans | `capacitor_mode` | plugin | — |
| Combat | col 1 / ligne 3 | Trappe missiles | `missile_hatch` | touche clavier | `6` |
| Combat | col 2 / ligne 3 | Convergence plus près (un cran) | `convergence_down` | plugin | — |
| Combat | col 3 / ligne 3 | Convergence plus loin (un cran) | `convergence_up` | plugin | — |
| Combat | col 4 / ligne 3 | Couleur du viseur | `crosshair_color` | plugin | — |
| Combat › Urgences | col 2 / ligne 2 | S'éjecter | `eject` | touche clavier | `RET.ARR` |
| Combat › Urgences | col 4 / ligne 2 | Autodestruction (appuyer de nouveau pour annuler) | `self_destruct` | plugin | — |
| Ciblage | col 2 / ligne 1 | Cible en face (la plus proche du viseur) | `target_front` | plugin | — |
| Ciblage | col 3 / ligne 1 | Attaquant le plus proche, puis le suivant | `target_attacker` | plugin | — |
| Ciblage | col 4 / ligne 1 | Cible précédente | `target_prev` | plugin | — |
| Ciblage | col 5 / ligne 1 | Cible suivante | `target_next` | plugin | — |
| Ciblage | col 1 / ligne 2 | Effacer la cible | `target_clear` | plugin | — |
| Ciblage | col 2 / ligne 2 | Cibler un sous-système | `target_subsystem` | plugin | — |
| Ciblage | col 3 / ligne 2 | Cible de la cible | `target_of_target` | plugin | — |
| Ciblage | col 4 / ligne 2 | Équipier précédent | `target_squad_prev` | plugin | — |
| Ciblage | col 5 / ligne 2 | Équipier suivant | `target_squad_next` | plugin | — |
| Ciblage | col 1 / ligne 3 | Marquer la cible pour la squad | `target_mark` | plugin | — |
| Ciblage | col 2 / ligne 3 | Contact : la roue sur la cible (duel, ami, squad), accepter, revanche (en ligne) | `duel` | plugin | — |
| Ciblage | col 3 / ligne 3 | Vue libre : la souris tourne la vue, plus le vaisseau | `free_look` | plugin | — |
| Ciblage | col 4 / ligne 3 | Zoom avant / arrière | `zoom_toggle` | plugin | — |
| Ciblage | col 5 / ligne 3 | Vue cockpit / extérieure (à pied : 1re / 3e personne) | `view_toggle` | plugin | — |
| Commandes de vol | col 2 / ligne 1 | Roulis gauche | `roll_left` | touche clavier | `Q` |
| Commandes de vol | col 3 / ligne 1 | Nez en haut | `pitch_up` | touche clavier | `HAUT` |
| Commandes de vol | col 4 / ligne 1 | Roulis droite | `roll_right` | touche clavier | `E` |
| Commandes de vol | col 5 / ligne 1 | Boost | `boost` | touche clavier | `MAJ` |
| Commandes de vol | col 1 / ligne 2 | Poussée avant | `thrust_fwd` | touche clavier | `W` |
| Commandes de vol | col 2 / ligne 2 | Lacet gauche | `yaw_left` | touche clavier | `GAUCHE` |
| Commandes de vol | col 3 / ligne 2 | Nez en bas | `pitch_down` | touche clavier | `BAS` |
| Commandes de vol | col 4 / ligne 2 | Lacet droite | `yaw_right` | touche clavier | `DROITE` |
| Commandes de vol | col 5 / ligne 2 | Poussée arrière | `thrust_back` | touche clavier | `S` |
| Commandes de vol | col 1 / ligne 3 | Strafe gauche | `strafe_left` | touche clavier | `A` |
| Commandes de vol | col 2 / ligne 3 | Strafe droite | `strafe_right` | touche clavier | `D` |
| Commandes de vol | col 3 / ligne 3 | Strafe haut | `strafe_up` | touche clavier | `ESPACE` |
| Commandes de vol | col 4 / ligne 3 | Strafe bas | `strafe_down` | touche clavier | `CTRL` |
| Commandes de vol | col 5 / ligne 3 | Vitesse | `speed` (valeur) | plugin | — |
| Commandes vaisseau | col 2 / ligne 1 | Électronique, puis moteurs (et retour : moteurs, puis électronique) | `engine_toggle` | plugin | — |
| Commandes vaisseau | col 3 / ligne 1 | Phares allumés / éteints | `headlights` | plugin | — |
| Commandes vaisseau | col 4 / ligne 1 | Éclairage du cockpit allumé / éteint | `cabin_light` | plugin | — |
| Commandes vaisseau | col 5 / ligne 1 | Train d'atterrissage sorti / rentré | `landing_gear` | plugin | — |
| Commandes vaisseau | col 1 / ligne 2 | Trappe missiles | `missile_hatch` | touche clavier | `6` |
| Commandes vaisseau | col 2 / ligne 2 | Ouvrir la station de maintenance (arrêté dans sa baie) | `station_menu` | plugin | — |
| Commandes vaisseau | col 3 / ligne 2 | Tourelle habitée : y aller / revenir au poste de pilotage | `turret_seat` | plugin | — |
| Commandes vaisseau | col 4 / ligne 2 | Sortir du vaisseau (arrêté, dans un hangar) | `exit_ship` | plugin | — |
| Commandes vaisseau | col 5 / ligne 2 | À pied : prendre le vaisseau, la console ou la boutique regardés | `interact` | plugin | — |
| Commandes vaisseau | col 1 / ligne 3 | Console d'équipe : réglages, Armurerie, banc d'essai | `practice_panel` | plugin | — |
| Commandes vaisseau | col 5 / ligne 3 | Coque | `hull` (valeur) | plugin | — |
| Tablette | col 3 / ligne 1 | Tablette : haut | `tablet_up` | plugin | — |
| Tablette | col 5 / ligne 1 | Visière : onglet précédent | `tablet_tab_prev` | plugin | — |
| Tablette | col 1 / ligne 2 | Tablette : prendre / rendre la main | `tablet_focus` | plugin | — |
| Tablette | col 2 / ligne 2 | Tablette : gauche (onglet précédent) | `tablet_left` | plugin | — |
| Tablette | col 3 / ligne 2 | Tablette : valider | `tablet_select` | plugin | — |
| Tablette | col 4 / ligne 2 | Tablette : droite (onglet suivant) | `tablet_right` | plugin | — |
| Tablette | col 5 / ligne 2 | Visière : onglet suivant | `tablet_tab_next` | plugin | — |
| Tablette | col 1 / ligne 3 | Tablette : retour | `tablet_back` | plugin | — |
| Tablette | col 3 / ligne 3 | Tablette : bas | `tablet_down` | plugin | — |
| Vues & système | col 2 / ligne 1 | Vue cockpit / extérieure (à pied : 1re / 3e personne) | `view_toggle` | plugin | — |
| Vues & système | col 3 / ligne 1 | Vue libre : la souris tourne la vue, plus le vaisseau | `free_look` | plugin | — |
| Vues & système | col 4 / ligne 1 | Zoom avant / arrière | `zoom_toggle` | plugin | — |
| Vues & système | col 5 / ligne 1 | Zoom : plus près | `zoom_closer` | plugin | — |
| Vues & système | col 1 / ligne 2 | Zoom : plus loin | `zoom_wider` | plugin | — |
| Vues & système | col 2 / ligne 2 | Suivi de tête activé / coupé | `head_toggle` | plugin | — |
| Vues & système | col 3 / ligne 2 | Recentrer le suivi de tête | `head_center` | plugin | — |
| Vues & système | col 4 / ligne 2 | Overlay des commandes affiché / caché (manches, pour le stream) | `input_overlay` | plugin | — |
| Vues & système | col 5 / ligne 2 | Affichage des FPS (client, serveur, les deux, rien) | `fps_display` | plugin | — |
| Vues & système | col 1 / ligne 3 | Marquer cet instant (enregistreur de vol) | `marker` | plugin | — |
| Vues & système | col 2 / ligne 3 | Enregistrement (combat ou manœuvre) : démarrer / arrêter (équipe) | `record_toggle` | plugin | — |
| Vues & système | col 3 / ligne 3 | Écrire dans le chat | `chat_open` | plugin | — |
| Vues › Course | col 2 / ligne 1 | Course : repartir avant la ligne de départ (solo) | `race_restart` | plugin | — |
| Vues › Course | col 3 / ligne 1 | Course : abandonner la course | `race_abandon` | plugin | — |
| Vues › Course | col 4 / ligne 1 | Traceur : départ et portes de course (solo, équipe) | `race_trace_gate` | plugin | — |
| Vues › Photo | col 2 / ligne 1 | Mode photo : entrer / sortir (Échap en sort aussi) | `photo_mode` | plugin | — |
| Vues › Photo | col 3 / ligne 1 | Photo : prendre la photo (sans interface) | `photo_capture` | plugin | — |
| Vues › Photo | col 4 / ligne 1 | Photo : cacher / montrer toute l'interface | `photo_hide_ui` | plugin | — |
| Vues › Photo | col 5 / ligne 1 | Photo : figer / relancer le temps (solo) | `photo_time` | plugin | — |
| Vues › Photo | col 1 / ligne 2 | Photo : lent (maintenir) | `photo_slow` | plugin | — |
| Vues › Photo | col 2 / ligne 2 | Photo : revenir derrière votre vaisseau | `photo_home` | plugin | — |
| Vues › Photo | col 3 / ligne 2 | Photo : horizon verrouillé / libre | `photo_horizon` | plugin | — |
| Vues › Photo | col 4 / ligne 2 | Photo : verrouiller sur le vaisseau devant / caméra libre | `photo_lock` | plugin | — |
| Vues › Photo › Réglages | col 2 / ligne 1 | Photo : mouvements plus vifs (moins de lissage) | `photo_smooth_less` | plugin | — |
| Vues › Photo › Réglages | col 3 / ligne 1 | Photo : mouvements plus doux (plus de lissage) | `photo_smooth_more` | plugin | — |
| Vues › Photo › Réglages | col 4 / ligne 1 | Photo : vitesse max plus basse | `photo_speed_down` | plugin | — |
| Vues › Photo › Réglages | col 5 / ligne 1 | Photo : vitesse max plus haute | `photo_speed_up` | plugin | — |
| Vues › Photo › Réglages | col 2 / ligne 2 | Photo : moins de flou (profondeur de champ, verrouillé sur une cible) | `photo_blur_less` | plugin | — |
| Vues › Photo › Réglages | col 3 / ligne 2 | Photo : plus de flou | `photo_blur_more` | plugin | — |
| Vues › Photo › Réglages | col 4 / ligne 2 | Photo : zone nette moins profonde | `photo_depth_less` | plugin | — |
| Vues › Photo › Réglages | col 5 / ligne 2 | Photo : zone nette plus profonde | `photo_depth_more` | plugin | — |

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
