# narratives

## Overview
Participants were asked to listen to (and perform two tasks on) the following sub-selection of stories from Nastase, S.A., Liu, YF., Hillman, H. et al. The “Narratives” fMRI dataset for evaluating models of naturalistic language comprehension. Sci Data 8, 250 (2021). https://doi.org/10.1038/s41597-021-01033-3

- “Lucy” : 9 min
- “The Man Who Forgot Ray Bradbury” : 14 min
- “I Knew You Were Black” :  13 min
- “It’s Not the Fall That Gets You” : 9 min
- “Slumlord” : 15 min
- “Pie Man” : 7 min
- “Pretty Mouth and Green My Eyes” : 11 min
- “Tunnel Under the World” :  split in two blocks of 12 min each

## Tasks

- **listening** : Participants were asked to listen to a story very carefully. 
- **recall** : Participants were asked to provide an account of what their heard. They were told they had as much time as need and asked to provide as many details as they could.
- **recency** : Presented with two fragments, participants had to choose which of the two fragments came first.

Tasks were presented with custom PsychoPy scripts synchronized to the scanner trigger. Sounds were delivered through Sensimetrics S15 insert headphones.

## Acquisition
Data were acquired on a Siemens Prisma Fit 3T scanner with a 64-channel head/neck coil at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM, Montréal, following the CNeuroMod protocol (TR = 1.49 s, 2 mm isotropic voxels, multiband acceleration factor 4).

## Preprocessing
- `fmriprep`: fMRIPrep preprocessing.
- `mriqc`: image quality metrics.
- `tsnr`: temporal SNR maps.
- `timeseries`: parcellated timeseries.
