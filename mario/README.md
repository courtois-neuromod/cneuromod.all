# mario

## Overview
The `mario` dataset contains in-scanner gameplay of *Super Mario Bros.* (Nintendo, 1985) for five CNeuroMod participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`). Participants played 22 of the original game's levels across two phases — a structured **discovery** phase followed by a longer **practice** phase of randomly selected levels.

Prior gameplay experience varied across participants: `sub-01` and `sub-06` had previously played SMB; `sub-01` and `sub-02` were regular videogame players; `sub-03` reported no prior videogame experience.

## Game environment
Participants used the CNeuroMod fiber-optic MRI controller described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158). The game ran on a console emulator via OpenAI's [gym-retro](https://github.com/openai/retro), recorded at 60 Hz. Because the game is fully deterministic, only player inputs were stored; the `.bk2` replay files allow exact reconstruction of every play.

## Run design
We use **run** for a single fMRI acquisition and **repetition** for a single play of a level — from start to either completion or losing all three lives. Each repetition corresponds to exactly one `.bk2` replay file. Each repetition began with no power-up and three lives; after death, the player resumed from the level start or from a checkpoint when one was available in the original level design.

The experiment was structured in two phases:

- **Discovery** — every level was played in order, with unlimited attempts per level until at least one successful completion before moving to the next.
- **Practice** — the remaining sessions used randomly selected levels for each repetition.

## Levels
22 of the 32 original SMB levels were used. Water levels and boss levels were excluded because their mechanics differ substantially from the rest of the game.

## Post-run questionnaire
At the end of each run, participants completed a short questionnaire including the items of the **Flow Short Scale 2 (FSS-2)**, plus two additional items aimed at evaluating player fatigue and frustration. These two extra items were introduced after data collection had begun and are therefore absent from the earliest runs.

## Per-subject summary

| Subject   | Repetitions (Discovery) | Repetitions (Practice) | Duration (Discovery) | Duration (Practice) | Success rate (Discovery) | Success rate (Practice) | Repetitions (Total) | Success rate (Total) | Duration (Total) |
|-----------|------------------------:|-----------------------:|---------------------:|--------------------:|-------------------------:|------------------------:|--------------------:|---------------------:|-----------------:|
| sub-01    | 230  | 567  | 03:54:27 | 09:47:11 | 0.578 | 0.781 | 797  | 0.723 | 13:41:38 |
| sub-02    | 227  | 487  | 04:57:35 | 12:30:24 | 0.401 | 0.671 | 714  | 0.585 | 17:27:59 |
| sub-03    | 176  | 451  | 04:49:38 | 11:57:19 | 0.432 | 0.698 | 627  | 0.624 | 16:46:57 |
| sub-05    | 177  | 457  | 05:30:04 | 12:27:44 | 0.367 | 0.582 | 634  | 0.522 | 17:57:48 |
| sub-06    | 134  | 468  | 04:25:41 | 13:37:40 | 0.627 | 0.857 | 602  | 0.806 | 18:03:22 |
| **Total** | **944** | **2430** | **23:37:27** | **60:20:19** | **0.481** | **0.718** | **3374** | **0.652** | **83:57:47** |

## Event files and annotations
For each run, a `_events.tsv` file lists the timing of each repetition. A richer `_desc-annotated_events.tsv` file provides three categories of events:

- **button presses** — every controller input;
- **in-game events** — game-state annotations derived from RAM (kills, deaths, power-ups, etc.);
- **replay events** — one entry per repetition with `trial_type` `gym-retro_game`, indicating which `.bk2` replay was played at which onset.

Companion `.bk2` replays, `.mp4` videos, `.json` summaries, mapped RAM variables, and low-level visual features are provided alongside the events files.

In addition, the 22 levels are split into 313 short **scenes** annotated with 29 design patterns (23 from Dahlskog & Togelius, 2012, plus 6 contextual ones). See [`SCENES.md`](./SCENES.md) and the [`mario.scenes`](https://github.com/courtois-neuromod/mario.scenes) submodule for details and tooling to generate clip-level metadata, video, and memory dumps for each scene attempt.

## Reference
A detailed description of the dataset and an associated modelling study are available in [Paugam et al., bioRxiv 2025](https://doi.org/10.1101/2025.11.28.691119).
