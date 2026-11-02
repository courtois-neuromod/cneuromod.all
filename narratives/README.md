# narratives

## Overview
Five participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`) completed 12 fMRI sessions in which they listened to spoken stories and performed two behavioural tasks (free recall and recency judgment) immediately after each story. Each session included two stories, and the full set of eight stories was repeated three times across sessions (4 pairs of stories × 3 repetitions = 12 sessions). The stimuli are a sub-selection of eight stories (~97 min of unique audio in total) drawn from the *Narratives* collection ([Nastase et al., 2021](https://doi.org/10.1038/s41597-021-01033-3)):

- “Lucy” (`Lucy`) — 9 min
- “The Man Who Forgot Ray Bradbury” (`Forgot`) — 14 min
- “I Knew You Were Black” (`Black`) — 13 min
- “It’s Not the Fall That Gets You” (`Notthefallintact`) — 9 min
- “Slumlord” (`Slumlord`) — 15 min
- “Pie Man” (`Pieman`) — 7 min
- “Pretty Mouth and Green My Eyes” (`Prettymouth`) — 11 min
- “Tunnel Under the World” (`Tunnelpart1`, `Tunnelpart2`) — split in two blocks of 12 min each

What makes this dataset distinctive is that it pairs naturalistic spoken-narrative comprehension with in-scanner spoken free recall and episodic recency judgments across three repetitions within the same deeply sampled CNeuroMod participants, enabling comparisons with the larger cross-sectional *Narratives* benchmark as well as other CNeuroMod language and movie-watching datasets (`langlocalizer`, `harrypotter`, `friends`, `movie10`).

## Tasks
For each story `<Story>`, three functional runs were acquired in sequence (`*Recall` was acquired separately for each half of *Tunnel Under the World*, followed by a single `*Recency` run):
- **listening** (`task-<Story>Story`): Participants were asked to listen to the story very carefully.
- **recall** (`task-<Story>Recall`): Participants were asked to provide a spoken account of what they heard. They were told they had as much time as needed and were asked to provide as many details as they could.
- **recency** (`task-<Story>Recency`): Presented with two fragments from the story, participants had to choose which of the two fragments came first.

Tasks were presented with custom PsychoPy scripts synchronized to the scanner trigger. Sounds were delivered through Sensimetrics S15 insert headphones.

## Acquisition
Data were acquired on a Siemens Prisma Fit 3T scanner with a 64-channel head/neck coil at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM, Montréal, following the CNeuroMod protocol (TR = 1.49 s, 2 mm isotropic voxels, multiband acceleration factor 4).

## Preprocessing
- `fmriprep`: fMRIPrep preprocessing.
- `mriqc`: image quality metrics.
- `tsnr`: temporal SNR maps.
- `timeseries`: parcellated timeseries.
