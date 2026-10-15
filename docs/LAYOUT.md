# Plan des pages — Stream Deck 15 touches (MK.2 / origine) (5 × 3)

Généré par `src/build.py`. `·` = touche volontairement vide.

## Accueil

| col 1          | col 2         | col 3             | col 4         | col 5            |
|----------------|---------------|-------------------|---------------|------------------|
| 📁 Combat       | 📁 Ciblage     | 📁 Vol             | 📁 Vaisseau    | 📁 Tablette       |
| `tri_weapons`  | `tri_engine`  | `tri_shield`      | `tri_neutral` | 📁 Vues & système |
| `target_front` | `target_next` | `target_attacker` | Leurres `5`   | Missile `4`      |

## Combat

| col 1               | col 2              | col 3            | col 4             | col 5            |
|---------------------|--------------------|------------------|-------------------|------------------|
| ↩ Retour            | Tir groupe 1 `1`   | Tir groupe 2 `2` | Missile `4`       | Leurres `5`      |
| `tri_weapons`       | `tri_engine`       | `tri_shield`     | `tri_neutral`     | `capacitor_mode` |
| Trappe missiles `6` | `convergence_down` | `convergence_up` | `crosshair_color` | 📁 Urgences       |

## Combat › Urgences

| col 1    | col 2               | col 3 | col 4           | col 5 |
|----------|---------------------|---|-----------------|---|
| ↩ Retour | ·                   | · | ·               | · |
| ·        | S'éjecter `RET.ARR` | · | `self_destruct` | · |
| ·        | ·                   | · | ·               | · |

## Ciblage

| col 1          | col 2              | col 3              | col 4               | col 5               |
|----------------|--------------------|--------------------|---------------------|---------------------|
| ↩ Retour       | `target_front`     | `target_attacker`  | `target_prev`       | `target_next`       |
| `target_clear` | `target_subsystem` | `target_of_target` | `target_squad_prev` | `target_squad_next` |
| `target_mark`  | `duel`             | `free_look`        | `zoom_toggle`       | `view_toggle`       |

## Commandes de vol

| col 1             | col 2                 | col 3                | col 4                 | col 5               |
|-------------------|-----------------------|----------------------|-----------------------|---------------------|
| ↩ Retour          | Roulis gauche `Q`     | Nez en haut `HAUT`   | Roulis droite `E`     | Boost `MAJ`         |
| Poussée avant `W` | Lacet gauche `GAUCHE` | Nez en bas `BAS`     | Lacet droite `DROITE` | Poussée arrière `S` |
| Strafe gauche `A` | Strafe droite `D`     | Strafe haut `ESPACE` | Strafe bas `CTRL`     | 📊 Vitesse           |

## Commandes vaisseau

| col 1               | col 2           | col 3         | col 4         | col 5          |
|---------------------|-----------------|---------------|---------------|----------------|
| ↩ Retour            | `engine_toggle` | `headlights`  | `cabin_light` | `landing_gear` |
| Trappe missiles `6` | `station_menu`  | `turret_seat` | `exit_ship`   | `interact`     |
| `practice_panel`    | ·               | ·             | ·             | 📊 Coque        |

## Tablette

| col 1          | col 2         | col 3           | col 4          | col 5             |
|----------------|---------------|-----------------|----------------|-------------------|
| ↩ Retour       | ·             | `tablet_up`     | ·              | `tablet_tab_prev` |
| `tablet_focus` | `tablet_left` | `tablet_select` | `tablet_right` | `tablet_tab_next` |
| `tablet_back`  | ·             | `tablet_down`   | ·              | ·                 |

## Vues & système

| col 1        | col 2           | col 3         | col 4           | col 5         |
|--------------|-----------------|---------------|-----------------|---------------|
| ↩ Retour     | `view_toggle`   | `free_look`   | `zoom_toggle`   | `zoom_closer` |
| `zoom_wider` | `head_toggle`   | `head_center` | `input_overlay` | `fps_display` |
| `marker`     | `record_toggle` | `chat_open`   | 📁 Course        | 📁 Photo       |

## Vues › Course

| col 1    | col 2          | col 3          | col 4             | col 5 |
|----------|----------------|----------------|-------------------|---|
| ↩ Retour | `race_restart` | `race_abandon` | `race_trace_gate` | · |
| ·        | ·              | ·              | ·                 | · |
| ·        | ·              | ·              | ·                 | · |

## Vues › Photo

| col 1        | col 2        | col 3           | col 4           | col 5            |
|--------------|--------------|-----------------|-----------------|------------------|
| ↩ Retour     | `photo_mode` | `photo_capture` | `photo_hide_ui` | `photo_time`     |
| `photo_slow` | `photo_home` | `photo_horizon` | `photo_lock`    | 📁 Réglages photo |
| ·            | ·            | ·               | ·               | ·                |

## Vues › Photo › Réglages

| col 1    | col 2               | col 3               | col 4              | col 5              |
|----------|---------------------|---------------------|--------------------|--------------------|
| ↩ Retour | `photo_smooth_less` | `photo_smooth_more` | `photo_speed_down` | `photo_speed_up`   |
| ·        | `photo_blur_less`   | `photo_blur_more`   | `photo_depth_less` | `photo_depth_more` |
| ·        | ·                   | ·                   | ·                  | ·                  |

---

`identifiant` = touche du plugin (son libellé vient du jeu) · `TOUCHE` = touche clavier native · 📊 = valeur affichée.
