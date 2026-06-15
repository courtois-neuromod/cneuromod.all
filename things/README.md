# things

## Overview
N=4 participants completed between 33 (`sub-06`) and 36 (`sub-01`, `sub-02`, `sub-03`) fMRI sessions of a continuous recognition task with images from the [THINGS dataset](https://things-initiative.org/). The first session included 3 runs, and all subsequent sessions included 6 runs. Each 4.7 minutes run included 60 trials. For each trial, an image was shown in the center of the screen for 2.98s, followed by a 1.49s ISI. Subjects maintained fixation on a black fixation marker overlaid onto the image center and visible at all times throughout a run. Images were sampled from 720 THINGS categories. `sub-01`, `sub-02`, `sub-03` were shown 6 images per category (4320 unique stimuli), and `sub-06` was shown 5 images for 480 categories and 6 images for the remaining 240 (3840 unique stimuli).  

## Visual memory task
Each image was shown three times throughout the duration of the experiment (it was repeated once within and once across weekly sessions). For each trial, participants reported whether the image was shown for the first time (“unseen”) or whether it had been shown previously (“seen”), either during the current or a previous session or both. Participants also reported whether or not they felt confident in their answer. Responses (seen/unseen ✕ sure/unsure) were made with the right thumb by pressing one of four buttons (top, bottom, left, right) on a video game controller designed by the team and described in [Harel et al. (2022)](https://psyarxiv.com/m2x6y/). No feedback on memory performance was given to participants throughout the entire duration of the experiment.

## Event file annotations
For each functional run, a companion file `_events.tsv` contains the timing and duration of each trial, the identity of the image shown, the condition (seen/unseen), whether the image was repeated between and/or within session, the subject's response and whether it was correct, the delay and number of trials since the last presentation (for repeating items), and metrics of fixation compliance derived from eye-tracking data. Available trial annotations are described [here](https://github.com/courtois-neuromod/things_memory_results/blob/marie_dev/src/behav_data/events_descriptors_wEyetrack.json)

:::{important}
A few sessions were accidentally administered out of the planned order, introducing atypical patterns of repetition for images shown during/after those sessions. Users may want to exclude these sessions from analyses that depend on repetition patterns or memory performance. These include `ses-024`, `ses-025` and `ses-026` for `sub-03`, and `ses-019` to `ses-026` (inclusively) for `sub-06`. fMRI data from `run 6` of `sub-06`'s `ses-008` are excluded from the dataset due to mistakenly positionned MRI field-of-view.
:::
