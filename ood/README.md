# ood

## Overview

The `ood` ("out-of-distribution") dataset was collected to test how well brain encoding models trained on CNeuroMod movie data (friends and movie10) generalize to movie content that differs from their training distribution in different ways. Participants watched excerpts from six films and TV programs chosen to span a range of genres, visual styles, tones and languages: a silent black-and-white comedy, hand-drawn and digital animation, a vintage children's show in Canadian French, a nature documentary, and a neo-noir crime feature film.

The dataset served as the held-out test set for the second, out-of-distribution phase of the [Algonauts 2025 challenge](https://arxiv.org/abs/2501.00504), in which models trained on Friends and movie10 were evaluated on their ability to predict brain responses to these new stimuli. Results from the challenge winners show that prediction accuracy drops substantially relative to in-distribution data (Friends season 7), and that the drop is largest for the most atypical stimuli, such as silent film, abstract animation, and nature documentaries (d'Ascoli et al., 2026).

## Stimuli

Each source was edited into two segments of roughly ten minutes (8–12 min), each presented in a separate run, for about two hours of unique content per participant. Every participant saw every segment once (no repetitions).

| `<task>` | Source | Segment durations | Notes |
|---|---|---|---|
| `chaplin1`, `chaplin2` | "The Pawn Shop" (Chaplin, 1916), a Charlie Chaplin film | 10.7, 10.1 min | Music, black-and-white; no speech |
| `mononoke1`, `mononoke2` | [Princess Mononoke](https://en.wikipedia.org/wiki/Princess_Mononoke) (Miyazaki, 1997) | 10.5, 10.6 min | Hand-drawn animation |
| `passepartout1`, `passepartout2` | [Passe-Partout](https://en.wikipedia.org/wiki/Passe-Partout), season 2, episodes 7–8 | 10.5, 10.8 min | French-language children's show from Québec |
| `planetearth1`, `planetearth2` | [Planet Earth](https://en.wikipedia.org/wiki/Planet_Earth_(2006_TV_series)) (BBC, 2006), episode 2 "Mountains" | 10.8, 10.4 min | Originally a wildlife documentary with narration; scenes featuring wildlife were edited out to show only landscapes |
| `pulpfiction1`, `pulpfiction2` | [Pulp Fiction](https://en.wikipedia.org/wiki/Pulp_Fiction) (Tarantino, 1994) | 11.6, 9.4 min | Neo-noir crime comedy |
| `wot1`, `wot2` | [World of Tomorrow](https://en.wikipedia.org/wiki/World_of_Tomorrow_(film)) (Hertzfeldt, 2015) | 8.8, 8.0 min | Abstract, minimalist animated short |

Segments were cut from the source videos with [MLT `melt`](https://www.mltframework.org/), with every step recorded as a `datalad run` command in the stimuli dataset. Some segments are a single continuous excerpt (`chaplin`, `mononoke`, `pulpfiction`, `wot`), while others join two non-contiguous excerpts (`passepartout`, `planetearth`). Each segment starts with a fade-in from black and ends with a fade-out to black, and a black gap separates spliced excerpts. Audio was normalized with a dynamic range compressor and equalizer so that loudness stays comparable across sources. The edited segments are in `ood/bids/stimuli/<source>/task-<source><seg>_video.mkv`, next to the uncut source videos.

## Sessions and runs

Data were collected in two sessions per participant:

- `ses-001`: `chaplin`, `mononoke`, `passepartout`
- `ses-002`: `planetearth`, `pulpfiction`, `wot`

For `sub-05`, the `passepartout` runs were acquired in `ses-002` instead of `ses-001`. Functional runs are named `sub-<participant>_ses-<sess>_task-<source><seg>_bold.nii.gz`, with a companion `_events.tsv` file. Presentation used the same software as the other CNeuroMod video tasks (`src/tasks/video.py` in the [task_stimuli](https://github.com/courtois-neuromod/task_stimuli) repository).

:::{important}
The `ood` segments were the hidden test set of the Algonauts 2025 challenge. Teams never had access to the brain data during the challenge. If you compare your results to the challenge leaderboard, keep in mind that the official scores were computed on parcel-wise timeseries (Schaefer 1000 parcels, MNI152NLin2009cAsym, z-scored per run) produced with the challenge's preprocessing.
:::

## Preprocessing

- `fmriprep`: fMRIPrep preprocessing.
- `mriqc`: image quality metrics.
- `tsnr`: temporal SNR maps.
- `timeseries`: parcellated timeseries.
