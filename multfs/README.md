# multfs

## Overview
Five participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`) performed 12 structured visual working-memory tasks while fMRI was acquired, in the dataset presented as *TaskScape-WM* (Lei et al.). Each participant completed one behavioural training session followed by 16 scanning sessions of about 30–35 min of task acquisition each. Eye-tracking and BIOPAC physiological signals (ECG, PPG, skin conductance, respiration) were recorded alongside the fMRI.

What makes the dataset distinctive is its factorial design. The stimuli are eight photorealistic images rendered from 3D models, crossing two object categories (faces and buses), two identities per category and two viewpoints (left- or right-facing), and shown at one of two screen locations. The same small set of working-memory operations is applied across systematically varied stimulus features, so that task rule, stimulus content and their interaction can be dissociated. Ordered stimulus pairs are sampled exhaustively and repeated at least five times per participant, yielding more than 400 distinct task conditions with at least five correct-trial repetitions. This supports representational similarity analysis, brain encoding and generalization across tasks and individuals, and the dataset can serve as a benchmark for brain–model alignment.

## Tasks
All tasks were implemented in PsychoPy and answered with the "X" (match) and "B" (non-match) buttons of a [custom MRI game controller](https://doi.org/10.1371/journal.pone.0290158). The 12 tasks combine a few temporal structures with different task-relevant features (location, category or identity):

- **DMS-Loc**: one Delayed Match-to-Sample task on stimulus location. It is a fixed reference task, run in every session to monitor session-to-session variability.
- **1-Back**: three tasks (location, category, identity). Each trial is a sequence of six stimuli, with each stimulus compared with the previous one.
- **CTXDM**: two Contextual Decision-Making tasks differing in feature order. The outcome of a first comparison selects the feature used for a second comparison, and only the second outcome is reported.
- **InterDMS**: six Interleaved Delayed Match-to-Sample tasks, crossing two interleaving patterns (ABAB, ABBA) with three task-relevant features. Two DMS-like comparisons are interleaved within a sequence of four stimuli.

Each stimulus lasts one TR (1.49 s). Each session comprises seven runs: one DMS-Loc, one 1-Back, two CTXDM and three InterDMS runs. Task variants and trial orders are counterbalanced across sessions. Stimuli were presented with [task_stimuli](https://github.com/courtois-neuromod/task_stimuli).

## Behavioural performance
Response rates were high in all task families (about 97–99%). Mean accuracy was 94.6% for 1-Back, 93.3% for InterDMS and 77.8% for CTXDM, which is the most demanding task because of its context-dependent rule switching.

## Acquisition
Data were acquired on a Siemens Prisma Fit 3T scanner with a 64-channel head/neck coil at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM, Montréal, following the CNeuroMod protocol. Gaze was recorded from the right eye at 250 Hz with Pupil Core, and physiological signals with a BIOPAC MP160 system.

## Preprocessing
- `fmriprep`: fMRIPrep preprocessing.
- `mriqc`: image quality metrics.
- `tsnr`: temporal SNR maps.
- `timeseries`: parcellated timeseries.
