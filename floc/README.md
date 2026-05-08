# floc

## Overview
Four participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`) completed six sessions of a functional localizer task designed to identify brain regions responding preferentially to specific stimulus categories. The task was based on a [Psychopy implementation](https://github.com/NBCLab/pyfLoc) of the [Stanford VPN lab's fLoc task](https://doi.org/10.1523/JNEUROSCI.4822-14.2015) using stimuli from the fLoc functional localizer package (downloaded [here](https://github.com/VPNL/fLoc)).

## Imaging sessions
Each session included two functional runs of 3.85 minutes with randomly ordered ~6s blocks of rapidly presented images from one of five categories : `faces`, `places`, `bodies`, `objects` and `characters`. Each block included 12 trials for which an image from the block’s category was displayed centrally for 0.4s, followed by a 0.095-0.1s ISI. Subjects were instructed to fixate on a red dot in the middle of the screen and to press a button with the right thumb on a custom mri-compatible video game controller ([Harel et al. (2022)](https://psyarxiv.com/m2x6y/)) whenever the same image appeared twice in a row (the “one-back” task variation).

## Tasks
Blocks of baseline condition during which the red fixation dot appeared on a grey background for 5.96s were also intermixed in the block sequence. Each run included 6 blocks from each of the five categories and 6 blocks of baseline. For each session, the first run included images from the house (`places`), body (`body parts`), word (`characters`), adult (`faces`) and car (`objects`) fLoc package sub-categories. The second run included images from the corridor (`places`), limb (`body parts`), word (`characters`), adult (`faces`) and instrument (`objects`) sub-categories.
