# petit-prince

## Overview

Five participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`) listened to the full audiobook of Antoine de Saint-Exupéry's *Le Petit Prince* (1943) twice during fMRI, once in French and once in English, for about 3.2 hours of spoken narrative per participant. Every section of the story was heard once in each language.

The stimuli are the same as in the [Individual Brain Charting](https://individual-brain-charting.github.io/docs/) project, and they also form the basis of the *Le Petit Prince* multilingual fMRI corpus ([Li et al., 2022](https://doi.org/10.1038/s41597-022-01625-7), OpenNeuro [ds003643](https://openneuro.org/datasets/ds003643)). That corpus scanned large groups of native English, French and Chinese listeners, each hearing the story once in their native language. The CNeuroMod dataset complements it: a few bilingual individuals from a deeply sampled cohort exposed to many naturalistic and language datasets heard the *Le Petit Prince* narrative in English and French.

## Stimuli

The audiobook is split into nine sections per language, and each section is presented in a separate run.

| `<task>` | Language | Sections (runs) | Run durations | Total |
|---|---|---|---|---|
| `lppFR` | French | 9 (`run-01`…`run-09`) | 9.9–12.7 min | ~99 min |
| `lppEN` | English | 9 (`run-01`…`run-09`) | 8.9–12.3 min | ~95 min |

Run durations include a few seconds of scanning before and after the audio. The audio files come from ds003643, which is installed as a subdataset in `petit-prince/bids/sourcedata/ds003643`. They are exposed through file-level symlinks in `petit-prince/bids/stimuli/` (`task-lppFR_section_<n>.wav`, `task-lppEN_section-<n>.wav`). The Chinese sections (`task-lppCN_*`) are available there too, but they were not presented. Each `_events.tsv` file gives the audio onset and the `stim_file` played in that run.

## Sessions and runs

Each participant completed three sessions of six runs. Language order was counterbalanced: French first for `sub-01` and `sub-02`, English first for `sub-03`, `sub-05` and `sub-06`.

| Participants | `ses-001` | `ses-002` | `ses-003` |
|---|---|---|---|
| `sub-01`, `sub-02` | FR 1–6 | FR 7–9, EN 1–3 | EN 4–9 |
| `sub-03`, `sub-05` | EN 1–6 | EN 7–9, FR 1–3 | FR 4–9 |
| `sub-06` | EN 1–5 | EN 6–9, FR 1–2 | FR 3–7 |

`sub-06` is missing French runs 8 and 9 (2 runs in total). Functional runs are named `sub-<participant>_ses-<sess>_task-lpp<FR|EN>_run-<section>_part-<mag|phase>_bold.nii.gz`. Before each run, participants were told to listen carefully because they would be asked a few questions about the story at the end. Presentation used the `Story` task of the [task_stimuli](https://github.com/courtois-neuromod/task_stimuli) repository (`src/sessions/ses-petitprince.py`).
