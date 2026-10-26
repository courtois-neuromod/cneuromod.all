# mariostars

## Overview
The `mariostars` dataset contains in-scanner gameplay of the *Super Mario Bros.* remake included in *Super Mario All-Stars* (Nintendo, 1993) for five CNeuroMod participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`). Participants played the same 22 levels as in the {doc}`mario </datasets/mario>` dataset, which they had completed beforehand. The level layouts are essentially unchanged while the graphics and sound are entirely redone, so the dataset tests how brain and behavioural models generalize across visual and auditory renderings of the same game.

`mariostars` is currently withheld for the Algonauts Project 2027 Challenge.

## Game environment
Participants used the CNeuroMod fiber-optic MRI controller described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158). The game ran on a Super Nintendo emulator via OpenAI's [gym-retro](https://github.com/openai/retro) (`SuperMarioAllStars-Snes`), recorded at 60 Hz. Because the game is fully deterministic, only player inputs were stored; the `.bk2` replay files allow exact reconstruction of every play.

## Differences from the NES original
- **Graphics.** Sprites and tiles are redrawn for the SNES, with detailed backgrounds and parallax scrolling instead of the original flat colours.
- **Sound.** The music is re-arranged and most sound effects are taken from *Super Mario World*. When little time remains, a warning plays and the music speeds up.
- **Gameplay.** Level layouts, enemies and items are the same. Small changes include Mario briefly rising after breaking a brick, the upper half of Piranha Plants hurting Mario, and the removal of some glitches (such as the Minus World).
- **Controls.** The SNES pad has extra buttons (such as L and R) with no documented function in this game; presses are logged as `Action/Other`, with the raw button in the `button` column.

## Run design
We use **run** for a single fMRI acquisition and **repetition** for a single play of a level — from start to either completion or losing all three lives. Each repetition corresponds to exactly one `.bk2` replay file. Each repetition began with no power-up and three lives; after death, the player resumed from the level start or from a checkpoint when one was available in the original level design.

There is no discovery phase: the initial learning of the levels was covered by `mario`. All sessions follow the `mario` practice phase, with levels presented in pseudo-random order so that every level is played once before any level is repeated.

## Levels
The 22 levels of `mario`: all levels of the eight worlds except the water levels (2-2, 7-2) and the castle (boss) levels (x-4). Levels are identified as `level-w<world>l<level>` in file names.

## Post-run questionnaire
At the end of each run, participants completed the same questionnaire as in `mario`: the items of the **Flow Short Scale 2 (FSS-2)**, plus two items evaluating player fatigue and frustration.

## Per-subject summary
A repetition counts as a success when the level is completed. Repetitions that left the level through a warp zone (84, on levels 1-2 and 4-2) are not counted as successes.

| Subject   | Repetitions | Success rate | Duration |
|-----------|------------:|-------------:|---------:|
| sub-01    | 253  | 0.771 | 04:26:28 |
| sub-02    | 229  | 0.690 | 05:27:42 |
| sub-03    | 225  | 0.653 | 06:12:09 |
| sub-05    | 251  | 0.649 | 07:06:26 |
| sub-06    | 274  | 0.803 | 07:53:52 |
| **Total** | **1232** | **0.717** | **31:06:36** |

## Event files and annotations
For each run, a `_events.tsv` file lists the timing of each repetition. A richer `_desc-annotated_events.tsv` file provides three categories of events, using the vocabulary shared by the CNeuroMod videogame datasets (see `task-mariostars_events.json`):

- **button presses** — every controller input;
- **in-game events** — game-state annotations derived from RAM (kills, deaths, power-ups, etc.);
- **replay events** — one entry per repetition with `trial_type` `gym-retro_game`, indicating which `.bk2` replay was played at which onset.

Companion `.bk2` replays, `.mp4` videos, `.json` summaries, mapped RAM variables, and low-level visual and audio features are provided alongside the events files in each session's `gamelogs/` folder.

Because the level layouts are the same as in `mario`, the scene partition described in {doc}`SCENES.md </contents/scenes>` applies in principle. The [`mario.scenes`](https://github.com/courtois-neuromod/mario.scenes) tooling has not been tested on `mariostars` and may need adjustments.
