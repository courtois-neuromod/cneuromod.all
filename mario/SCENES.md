# Mario scenes 

The 22 *Super Mario Bros.* levels used in the [`mario`](./README.md) dataset are partitioned into 313 short **scenes** (≈ 15 per level), each annotated with a set of game design patterns. Scenes act as atomic units of gameplay and are intended as the unit of analysis for behavioral and neural studies of mario gameplay.

Scene partitioning, design-pattern annotations, and accompanying assets are released as a standalone, citable resource on Zenodo:

> Harel Y., Delhaye H., Pinsard B., Bellec P. *Super Mario Bros. Scenes and Annotations.*  
> Zenodo, v0.6 (2025-06-03). DOI: [10.5281/zenodo.15586709](https://doi.org/10.5281/zenodo.15586709). License: CC-BY-4.0.

The companion code repository — including tooling to align scenes with `mario` behavioral data and generate per-scene clips — lives in the [`mario.scenes`](https://github.com/courtois-neuromod/mario.scenes) submodule.

## Scope
- **Levels covered.** All 22 levels included in `mario`. Underwater levels and castle (boss) levels are excluded because their mechanics differ markedly from the other levels and would not be annotated meaningfully under the same pattern vocabulary.
- **Scenes.** 313 in total, defined by entry/exit X-coordinates within their level.
- **Annotations.** Binary indicators (0 = absent, 1 = present) for 29 design patterns per scene — 23 atomic gameplay patterns from Dahlskog & Togelius (2012), plus 6 contextual labels added for this dataset.
- **Caveat.** Bonus zones and waterworld sections are *flagged* with a contextual label but their internal structure is not exhaustively pattern-annotated.

## Methodology
1. Reference level maps were obtained from [NesMaps](https://nesmaps.com/).
2. X-coordinates of scene boundaries were extracted using the [stable-retro](https://github.com/Farama-Foundation/stable-retro) GUI.
3. A human annotator identified which design patterns were present in each scene by inspection.
4. All annotations were aggregated in the `scenes_mastersheet` files.

## Design patterns

Twenty-three core patterns from Dahlskog & Togelius (2012):

| Family | Patterns |
|--------|----------|
| Enemy  | Enemy · 2-Horde · 3-Horde · 4-Horde · Roof |
| Gap    | Gap · Multiple gaps · Variable gaps · Gap enemy · Pillar gap |
| Valley | Valley · Pipe valley · Empty valley · Enemy valley · Roof valley |
| Path   | 2-Path · 3-Path · Risk/Reward |
| Stair  | Stair up · Stair down · Empty stair valley · Enemy stair valley · Gap stair valley |

Six additional contextual patterns added for this dataset:

`Reward` · `Moving platform` · `Flagpole` · `Beginning` · `Bonus zone` · `Waterworld`

## Data files (Zenodo)

| File | Format | Content |
|------|--------|---------|
| `scenes_mastersheet.csv` | CSV | One row per scene: world, level, scene number, entry/exit X-coordinates, and binary columns for each design pattern. |
| `scenes_mastersheet.json` | JSON | Same content as the CSV in JSON form. |
| `mario_scenes_manual_annotation.pdf` | PDF | Annotated level maps showing each scene division. |
| `level_backgrounds.tar.gz` | tar.gz | Full-level static visual backgrounds. |
| `scene_backgrounds.tar.gz` | tar.gz | Per-scene static visual backgrounds. |

Mastersheet columns:

- `World` — 1–8.
- `Level` — 1–3 within a world.
- `Scene` — sequential scene index within the level.
- `Entry point` — X-coordinate of the scene start.
- `Exit point` — X-coordinate of the scene end.
- One binary column per design pattern (0 = absent, 1 = present).

## Tooling
The [`mario.scenes`](https://github.com/courtois-neuromod/mario.scenes) submodule provides code to (a) cross-reference `mario` behavioral data with the scene partition, (b) generate per-scene clips from gameplay replays, and (c) export per-attempt artefacts as metadata (`.json`), video (`.gif` / `.mp4` / `.webp`), and memory or game-variable dumps (`.npz`).

## References
- Dahlskog, S., & Togelius, J. (2012). *Patterns and procedural content generation: Revisiting Mario in world 1 level 1.* Workshop on Design Patterns in Games (DPG '12).
