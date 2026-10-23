# emotion-videos

## Overview
Five participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`) watched 1888 silent short video clips from the [Cowen & Keltner (2017)](https://doi.org/10.1073/pnas.1702247114) database ([https://www.alancowen.com/video](https://www.alancowen.com/video)), which evoke a broad range of affective states. Each clip was normed on 34 emotion categories and 14 affective dimensions by an independent sample; no ratings were collected from CNeuroMod participants. Multi-echo fMRI was acquired together with ECG, PPG, electrodermal activity, respiration and eye-tracking. Each video was shown once per participant.

## Stimuli
The database contains 2185 silent clips. Clips lasting more than 20 s (46 clips) were discarded, and the remaining clips were screened by two evaluators for extreme content (e.g. pornography, murder, animal abuse; 251 clips removed). Clips shorter than 1 s were looped so that they were shown for at least 1 s.

## Imaging sessions
Participants completed 36 runs of 8:20 min over 6 to 7 sessions. Each run contained 45 to 65 clips separated by an inter-trial interval of 3, 4, 5 or 6 s (randomized). A fixation marker (three concentric circles) was shown for 1.5 s before each clip and used for eye-tracking drift correction. Each run started with an instruction screen asking participants to keep their eyes open and fixate the marker. Clip order within a run is the same for all participants, whereas run order is randomized per participant. Stimuli were presented with [task_stimuli](https://github.com/courtois-neuromod/task_stimuli).

## Physiology and eye-tracking
Physiological signals were recorded with a BIOPAC MP160 system: 3-lead ECG, PPG (right hallux for four participants, right posterior tibial artery for one), skin conductance on the arch of the right foot, and a respiration belt at the abdominal or thoracic level. Eye-tracking was recorded from the right eye with a Pupil Core camera at 250 Hz, with a 9-point calibration before each run.

## Preprocessing
- `fmriprep`: fMRIPrep 25.2.3, with each echo in native space.
- `tedana`: optimal combination and denoising with tedana 25.1.0.
- `tsnr`: temporal SNR maps.
- `physprep`: preprocessed and quality-checked physiological data.
- `mriqc`: image quality metrics.

## Acquisition notes
Some functional runs were excluded because of technical problems or human error.

| Subject | Session | Notes |
|---|---|---|
| `sub-01` | `ses-002` | Interrupted after the first run (`run-01`) because of a scanner issue. |
| `sub-02` | `ses-003` | Only one session was acquired. |
| `sub-03` | `ses-001` | Whole session discarded (`run-01` to `run-03`) because of a stimulus projection problem; stimuli were repeated in `ses-002`. |
| `sub-05` | `ses-002` | `run-02` and `run-04` repeat `run-04` and `run-01` of `ses-001`, respectively, because of an acquisition error. |

Eye-tracking issues:

| Subject | Session | Notes |
|---|---|---|
| `sub-01` | `ses-005` | The fiber optic of the eye-tracker was not working properly. |
| `sub-03` | `ses-002` | Eye-tracking data discarded because of equipment issues: images were darker than usual, making pupil detection harder. |
| `sub-05` | `ses-005` | The eye-tracking software crashed after the first run and could not restart. |
| `sub-05` | `ses-006` | The eye-tracking software crashed in the middle of `run-05` and `run-06`. |
| `sub-06` | `ses-004` | Problems with pupil detection; only `run-06` had to be discarded. |
