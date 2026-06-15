# movie10

This dataset includes about 10 hours of functional data per participant (6 participants total). The python & psychopy scripts for preparation and presentation of the clips can be found in `src/tasks/video.py` of the following github [repository](https://github.com/courtois-neuromod/task_stimuli).
Session tags `<sess>` were `001`, `002` etc, and the number and composition of sessions varied from subject to subject. The `<task>` tags used in DataLad corresponded to each movie (`bourne`, `wolf`, `life`, `figures`) and a numerical index of the segments shown as each movie was cut into roughly ten minutes segments presented in separate run. Exact cutting points were manually selected to not interrupt the narrative flow. Fade out to a black screen was added at the end of each clip, and with a few seconds overlap between the end of a clip and the beginning of the next clip. The movie segments can be found under `movie10/stimuli/<movie>/<movie>_seg<seg>.mkv`, and the functional runs are named `func_sub-<participant>_ses-<sess>_task-<movie><seg>`, where the `<participant>` tag ranges from `sub-01` to `sub-06`. A companion file `_events.tsv` contains the timing and type of conditions presented to the subject.

The participants watched the following movies ([cogatlas](https://www.cognitiveatlas.org/id/trm_4c898da401420/)):
 * `<task>` name `bourne`: [The Bourne supremacy](https://en.wikipedia.org/wiki/The_Bourne_Supremacy_%28film%29). Duration ~100 minutes.
 * `<task>` name `wolf`: [The wolf of wall street](https://en.wikipedia.org/wiki/The_Wolf_of_Wall_Street_%282013_film%29). Duration ~170 minutes.
 * `<task>` name `figures`: [Hidden figures](https://en.wikipedia.org/wiki/Hidden_Figures). Duration ~120 minutes. This movie was presented twice, for a total duration of ~240 minutes.
 * `<task>` name `life`: [Life](https://en.wikipedia.org/wiki/Life_(British_TV_series)) Disc one of four: "Challenges of life, reptiles and amphibian mammals". DVD set was narrated by David Attenborough. Duration, and lasted ~50 minutes. This movie was presented twice, for a total duration of ~100 minutes.

It should be noted that although three of the participants are not native anglophones, all participants watched the movies in English. The three native francophone participants are fluent in English and report regularly watching movies in English.



:::{important}
The duration of BOLD series are slightly varying across participants and repetitions. If consistent length is required for analysis, series can be trimmed at the end to match duration, movie segments being aligned to the first TR.
:::


:::{important}
There are instances of re-scanned segments (due to scan QC fail), these re-scans will be in separate sessions. These should be handled or excluded in analysis requiring continuity of the presentation of the story.
:::
