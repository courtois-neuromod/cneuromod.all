# Shinobi training

The `shinobi/training` dataset contains behavioral-only at-home gameplay of *Shinobi III: Return of the Ninja Master* (Sega, 1993) for four CNeuroMod participants (`sub-01`, `sub-02`, `sub-04`, `sub-06`). It is a companion to the {doc}`shinobi </datasets/shinobi>` neuroimaging dataset and is stored as the [`shinobi/training`](https://github.com/courtois-neuromod/shinobi_training) submodule.

## Overview

Before any in-scanner session, participants trained at home on the same three levels as the scanning phase with no imposed regimen — they chose freely which level to play and how often to schedule a session. As an introduction, every participant first played Level-1 at least once: it gradually introduces the core mechanics (moving right, jumping, attacking and avoiding enemies) at an accessible difficulty. Beyond that, the data is intentionally heterogeneous across participants and well suited to studying learning trajectories or individual play styles, on its own or in conjunction with the scanning data.

## Game environment

Participants used the same setup as the scanning phase: the CNeuroMod fiber-optic MRI controller described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158), running on a console emulator via OpenAI's [gym-retro](https://github.com/openai/retro). Because the game is fully deterministic, only player inputs were recorded, allowing exact reconstruction of each play from the `.bk2` files.

## Session structure

A training session is an unrestricted collection of `.bk2` replays — one file per repetition (a single play of a level from start to completion or loss). There is no fixed session length or level order; participants scheduled sessions freely and chose which level to play each repetition.

## Per-subject summary

| Subject   | Sessions | Reps (Level-1) | Success (Level-1) | Duration (Level-1) | Reps (Level-4) | Success (Level-4) | Duration (Level-4) | Reps (Level-5) | Success (Level-5) | Duration (Level-5) | Reps (Total) | Success (Total) | Duration (Total) |
|-----------|---------:|---------------:|------------------:|-------------------:|---------------:|------------------:|-------------------:|---------------:|------------------:|-------------------:|-------------:|----------------:|-----------------:|
| sub-01    | 53  | 164 | 0.616 | 07:31:27 | 108 | 0.361 | 03:01:36 | 116 | 0.741 | 05:00:33 | 388  | 0.582 | 15:33:36 |
| sub-02    | 110 | 263 | 0.802 | 12:56:27 | 288 | 0.188 | 10:39:10 | 51  | 0.314 | 02:58:27 | 602  | 0.467 | 26:34:04 |
| sub-04    | 24  | 57  | 0.702 | 03:56:13 | 98  | 0.378 | 05:33:00 | 57  | 0.456 | 03:13:23 | 212  | 0.486 | 12:42:37 |
| sub-06    | 15  | 34  | 0.500 | 02:26:04 | 54  | 0.093 | 02:33:39 | 36  | 0.250 | 01:54:04 | 124  | 0.250 | 06:53:46 |
| **Total** | **202** | **518** | **0.712** | **26:50:11** | **548** | **0.246** | **21:47:25** | **260** | **0.527** | **13:06:27** | **1326** | **0.483** | **61:44:04** |

`Reps` = total plays of the level; `Success` = fraction of repetitions that ended in level completion; durations in `h:m:s`.
