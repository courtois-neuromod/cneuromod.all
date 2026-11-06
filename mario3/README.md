# mario3

## Overview
The `mario3` dataset contains in-scanner gameplay of *Super Mario Bros. 3* (Nintendo, 1988) for five CNeuroMod participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`), acquired after the {doc}`mario </datasets/mario>` and {doc}`mariostars </datasets/mariostars>` datasets. Participants played 80 levels across the game's eight worlds, first in game order (**discovery** phase), then in pseudo-random order (**practice** phase).

Compared with `mario`, the game keeps the same character and core controls but adds new mechanics — suits with new abilities (Raccoon flight, Tanooki, Frog and Hammer suits, Kuribo's Shoe), P-Switches, auto-scrolling levels — as well as longer, more varied levels and boss fights. The dataset therefore tests how brain and behavioural models generalize to new game mechanics and more complex levels.

:::{important}
Part of `mario3` is held out as the test set of the [Algonauts Project 2027 Challenge](https://algonautsproject.com/): fMRI responses for a subset of levels/runs are withheld, while the corresponding game logs and replays are part of the dataset. The withheld fMRI data will be released once the challenge ends.
:::

## Game environment
Participants used the CNeuroMod fiber-optic MRI controller described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158). The game ran on a console emulator via OpenAI's [gym-retro](https://github.com/openai/retro) (`SuperMarioBros3-Nes`), recorded at 60 Hz. Each level was loaded directly, skipping the world map. Because the game is fully deterministic, only player inputs were stored; the `.bk2` replay files allow exact reconstruction of every play.

## Run design
We use **run** for a single fMRI acquisition, **life** for a single play of a level until completion or death, and **repetition** for a set of up to three consecutive lives on the same level, ending when the level is completed or the third life is lost. Every life restarted from the beginning of the level as small Mario: power-ups did not carry over from one life to the next.

The experiment was structured in two phases:

- **Discovery** — every level was played once, in game order, with one repetition per level: the participant moved on to the next level after the repetition, whether or not the level was completed.
- **Practice** — the remaining sessions used levels in pseudo-random order, so that every level is played once before any level is repeated.

A few deviations from this design are visible in the data. During discovery, `sub-03` replayed the first 13 levels (1-1 to 2-4) in their second session before resuming where they had stopped, and `sub-05` replayed in one run the 7 levels of the previous run (World 5 Airship to 6-5). During practice, the level order was occasionally restarted, for instance after an interrupted session, so some levels were repeated before the full cycle of 80 was completed: five times for `sub-01` and twice for `sub-05`.

### Lives, not repetitions, are the unit of the files
Unlike `mario` and `mariostars`, where one `.bk2` file holds one three-life repetition, in `mario3` **each life is stored as its own `.bk2` file** and has its own `gym-retro_game` row in the events files. Nothing in the files groups lives into repetitions: the `rep-` index in file names counts the lives played on a level within a session. To recover repetitions, group consecutive `gym-retro_game` rows of the same run on the same level; a new repetition starts after a completed level or after a third life. See [mario3#95](https://github.com/courtois-neuromod/mario3/issues/95).

## Levels
80 levels, identified as `level-w<world>l<level>` in file names, with names for special stages (`Fortress`, `Tower`, `Airship`, `PiranhaPlant`, numbered when a world has several):

| World | Levels |
|-------|--------|
| 1 | 1–6, Fortress, Airship |
| 2 | 1–5, Fortress, Airship |
| 3 | 1–9, Fortress 1–2, Airship |
| 4 | 1–6, Fortress 1–2, Airship |
| 5 | 1–9, Fortress 1–2, Tower, Airship |
| 6 | 1–10, Fortress 1–3, Airship |
| 7 | 1–9, Fortress 1–2, Piranha Plant 1–2, Airship |
| 8 | 1–2, Fortress |

Unlike `mario`, fortresses and airships are included, with their boss fights. World 8's tank, battleship and airship stages and Bowser's castle were not used.

## Post-run questionnaire
At the end of each run, participants completed the same questionnaire as in `mario`: the items of the **Flow Short Scale 2 (FSS-2)**, plus two items evaluating player fatigue and frustration.

## Missing behavioural files
Some `.bk2` files were lost during acquisition, which explains part of the differences in the number of lives across participants; quality control of the behavioural files is ongoing. In the events files, a lost replay is marked by `Missing file` in `stim_file`, with no events inside its window.

## Per-subject summary
Repetitions are reconstructed from consecutive lives as described above. The discovery phase ends with the first play of the last level in game order (World 8 Fortress). A repetition counts as a success when the level is completed in any of its lives. Durations sum the available lives.

| Subject   | Repetitions (Discovery) | Repetitions (Practice) | Duration (Discovery) | Duration (Practice) | Success rate (Discovery) | Success rate (Practice) | Repetitions (Total) | Lives (Total) | Success rate (Total) | Duration (Total) |
|-----------|------------------------:|-----------------------:|---------------------:|--------------------:|-------------------------:|------------------------:|--------------------:|--------------:|---------------------:|-----------------:|
| sub-01    | 80  | 210  | 01:56:57 | 06:24:37 | 0.188 | 0.281 | 290  | 662  | 0.255 | 08:21:34 |
| sub-02    | 80  | 314  | 01:33:35 | 06:46:41 | 0.025 | 0.118 | 394  | 986  | 0.099 | 08:20:16 |
| sub-03    | 93  | 277  | 02:04:03 | 06:38:32 | 0.065 | 0.090 | 370  | 976  | 0.084 | 08:42:35 |
| sub-05    | 87  | 265  | 02:07:42 | 06:29:03 | 0.034 | 0.140 | 352  | 995  | 0.114 | 08:36:44 |
| sub-06    | 80  | 144  | 02:33:42 | 04:35:47 | 0.275 | 0.326 | 224  | 444  | 0.308 | 07:09:29 |
| **Total** | **420** | **1210** | **10:15:59** | **30:54:40** | **0.114** | **0.169** | **1630** | **4063** | **0.155** | **41:10:39** |

## Event files and annotations
For each run, a `_events.tsv` file lists the timing of each life. A richer `_desc-annotated_events.tsv` file provides three categories of events, using the vocabulary shared by the CNeuroMod videogame datasets, extended with events specific to *Super Mario Bros. 3* (suits and flight, P-Switches, goal cards, auto-scrolling; see `task-mario3_events.json`):

- **button presses** — every controller input;
- **in-game events** — game-state annotations derived from RAM (kills, deaths, power-ups, etc.);
- **replay events** — one entry per life with `trial_type` `gym-retro_game`, indicating which `.bk2` replay was played at which onset.

Companion `.bk2` replays, `.mp4` videos, `.json` summaries, mapped RAM variables, and low-level visual and audio features are provided alongside the events files in each session's `gamelogs/` folder.
