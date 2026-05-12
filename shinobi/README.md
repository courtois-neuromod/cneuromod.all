# shinobi

## Overview
The `shinobi` dataset is structured in two phases of gameplay on *Shinobi III: Return of the Ninja Master* (Sega, 1993) for four CNeuroMod participants (`sub-01`, `sub-02`, `sub-04`, `sub-06`):

- **Training phase** — at-home, behavioral-only sessions with no fixed cadence (see [Training phase](#training-phase)). The recorded `.bk2` replays are published as the [`shinobi/training`](./training) submodule.
- **Scanning phase** — in-MRI gameplay with a fixed run structure (see [Scanning phase](#scanning-phase)). This is the main fMRI dataset.

Both phases use the same three levels, selected for the relative homogeneity of their core mechanics.

## Game environment
Participants used the CNeuroMod fiber-optic MRI controller described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158). The game ran on a console emulator via OpenAI's [gym-retro](https://github.com/openai/retro). Because the game is fully deterministic, only player inputs were recorded, allowing exact reconstruction of each play from the `.bk2` files.

## Training phase
Before any in-scanner session, participants trained at home on the same three levels with no imposed regimen — they chose freely which level to play and how often to schedule a training session. As an introduction, every participant first played Level-1 at least once: it gradually introduces the core mechanics (moving right, jumping, attacking and avoiding enemies) at an accessible difficulty. Beyond that, the data is intentionally heterogeneous across participants and well suited to studying learning trajectories or individual play styles, on its own or in conjunction with the scanning data. A training session is an unrestricted collection of `.bk2` replays (one per repetition).

## Scanning phase
We use **run** for a single fMRI acquisition and **repetition** for a single play of a level — from start to either completion or losing all health (one life). Each repetition corresponds to exactly one `.bk2` replay file (the same convention applies to the training phase). The corresponding concept in the `mario` dataset uses the same definition but with three lives instead of one.

Within a run, levels were played in a fixed cycle: 1 → 4 → 5 → 1 → … A new repetition started immediately after the previous one ended, with the level switching only on completion or death. A run ended when the next repetition would have started past the 10-minute mark, so run duration is variable but always ≥ 10 minutes. Each run contains 3–5 repetitions; because of the fixed cycle, Level-1 is over-represented relative to Levels 4 and 5.

## Levels
The three selected levels (see the [Sega game documentation](https://sega.fandom.com/wiki/Shinobi_III:_Return_of_the_Ninja_Master) for their position in the original game):

| Level | Source                                  | Boss / mini-boss     |
|-------|-----------------------------------------|----------------------|
| 1     | Round 1 — *Zeed's Resurrection*         | 1 mini-boss + 1 boss |
| 4     | Beginning of Round 4 — *Destruction*    | none                 |
| 5     | Beginning of Round 5 — *Electric demon* | 1 mini-boss, no boss |

## Per-subject summary

### Training phase (at-home)

| Subject   | Sessions | Reps (Level-1) | Success (Level-1) | Duration (Level-1) | Reps (Level-4) | Success (Level-4) | Duration (Level-4) | Reps (Level-5) | Success (Level-5) | Duration (Level-5) | Reps (Total) | Success (Total) | Duration (Total) |
|-----------|---------:|---------------:|------------------:|-------------------:|---------------:|------------------:|-------------------:|---------------:|------------------:|-------------------:|-------------:|----------------:|-----------------:|
| sub-01    | 53  | 164 | 0.616 | 07:31:27 | 108 | 0.361 | 03:01:36 | 116 | 0.741 | 05:00:33 | 388  | 0.582 | 15:33:36 |
| sub-02    | 110 | 263 | 0.802 | 12:56:27 | 288 | 0.188 | 10:39:10 | 51  | 0.314 | 02:58:27 | 602  | 0.467 | 26:34:04 |
| sub-04    | 24  | 57  | 0.702 | 03:56:13 | 98  | 0.378 | 05:33:00 | 57  | 0.456 | 03:13:23 | 212  | 0.486 | 12:42:37 |
| sub-06    | 15  | 34  | 0.500 | 02:26:04 | 54  | 0.093 | 02:33:39 | 36  | 0.250 | 01:54:04 | 124  | 0.250 | 06:53:46 |
| **Total** | **202** | **518** | **0.712** | **26:50:11** | **548** | **0.246** | **21:47:25** | **260** | **0.527** | **13:06:27** | **1326** | **0.483** | **61:44:04** |

### Scanning phase (in-MRI)

| Subject   | Sessions | Runs | Reps (Level-1) | Success (Level-1) | Duration (Level-1) | Reps (Level-4) | Success (Level-4) | Duration (Level-4) | Reps (Level-5) | Success (Level-5) | Duration (Level-5) | Reps (Total) | Success (Total) | Duration (Total) |
|-----------|---------:|-----:|---------------:|------------------:|-------------------:|---------------:|------------------:|-------------------:|---------------:|------------------:|-------------------:|-------------:|----------------:|-----------------:|
| sub-01    | 12 | 53  | 87  | 0.943 | 03:51:53 | 61  | 0.607 | 01:54:00 | 53  | 1.000 | 02:05:45 | 201 | 0.856 | 07:51:38 |
| sub-02    | 12 | 55  | 77  | 0.961 | 03:31:10 | 57  | 0.456 | 02:09:48 | 55  | 0.855 | 02:37:35 | 189 | 0.778 | 08:18:33 |
| sub-04    | 11 | 55  | 67  | 0.985 | 03:17:55 | 56  | 0.446 | 02:06:00 | 53  | 0.887 | 02:39:48 | 176 | 0.784 | 08:03:42 |
| sub-06    | 11 | 47  | 46  | 0.978 | 03:29:24 | 42  | 0.548 | 02:44:22 | 12  | 0.917 | 00:45:31 | 100 | 0.790 | 06:59:18 |
| **Total** | **46** | **210** | **277** | **0.964** | **14:10:22** | **216** | **0.514** | **08:54:11** | **173** | **0.913** | **08:08:38** | **666** | **0.805** | **31:13:11** |

`Reps` = total plays of the level; `Success` = fraction of repetitions that ended in level completion; durations in `h:m:s`.

## Event files and annotations
For each run, a `_events.tsv` file lists the timing and duration of every repetition. A richer `_desc-annotated_events.tsv` file provides three categories of events:

- **button presses** — every controller input;
- **in-game events** — handcrafted annotations such as kills and health losses;
- **replay events** — one entry per repetition with `trial_type` `gym-retro_game`, indicating which `.bk2` replay was played at which onset.

The full annotation schema is documented [here](https://github.com/courtois-neuromod/shinobi/blob/annotations/code/annotations/ANNOTATIONS.md). The corresponding `.bk2` replay files are stored under `<participant>/<sess>/gamelogs/`.

:::{important}
Due to a recording error during acquisition, a subset of `.bk2` replay files were lost. The affected repetitions are still listed in the events files but have an empty `stim_file` field. Users should decide on a case-by-case basis whether to exclude the corresponding fMRI volumes from analysis.
:::
