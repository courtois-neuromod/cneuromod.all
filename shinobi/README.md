# shinobi

## Overview
This dataset contains about 8h of gameplay on the videogame Shinobi III The Return of the Ninja Master, for N=4 participants (`sub-01`, `sub-02`, `sub-04` and `sub-06`). Participants used a custom-built fully fiber-optic MRI controller, designed by the team and described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158). In each run, participants played 3 levels in cycles and always in the same order. These levels were selected in the game to have fairly homogeneous core game mechanics (see the [Sega documentation](https://sega.fandom.com/wiki/Shinobi_III:_Return_of_the_Ninja_Master) for more details on game structure):
 * `Level-1` corresponded to round 1 of the original game, "Zeed's Resurrection". It included one mini-boss and one boss fight.
 * `Level-4` corresponded to the beginning of round 4 of the original game, "Destruction". It included no mini-boss or boss fight.
 * `Level-5` corresponded to the beginning of round 5 of the original game, "Electric demon". It included one mini-boss fight and no boss fight.

## Run design
Participants moved to the next level if they successfully completed a level, or lost three lives. A new level was then initiated unless 10 minutes had elapsed from the start of the run, at which point the run ended. The duration of each run is thus variable to a degree, with a minimum of ten minutes. Due to the fixed order in the cycle, `Level-1` was repeated more often than `Level-4` and `Level-5`.

In this dataset and the related documentation, we use the term `run` to designate a single functional sequence acquisition (per the usual in neuroimaging). The term `repetition` is used to designate the play of a single level (from start to either completion or the loss of three lives). As such, each run contains around 3 to 5 repetitions.

For each functional run, a companion file `_events.tsv` contains the timing and duration of each repetition played, as well as a `_desc-annotated_events.tsv` file that additionally contains richer annotations, including button presses and handcrafted game events annotations (Kills, Health losses). Additional documentation on the available annotations can be [found here](https://github.com/courtois-neuromod/shinobi/blob/annotations/code/annotations/ANNOTATIONS.md).

## Game files
The companion `.bk2` files can be found in the `<participant>/<sess>/gamelogs` folder. 

:::{important}
Due to a programming error a certain number of game recording files were lost during acquisition, these repetitions are still listed in the events file but their `stim_file` field is left blank. Choice is left to the user whether to exclude the corresponding fMRI volumes or not for their analysis.
:::
