# mutemusic

## Overview
Five participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`, `sub-06`) listened to familiar and unfamiliar music tracks in which parts of the audio had been replaced by silence, and were instructed to imagine the continuation of the music during the silent gaps ("mute" music). The paradigm is adapted from [Kraemer et al. (2005)](https://doi.org/10.1038/434158a), and was designed to study auditory imagery of different types of music, including vocal, orchestral and synthetic (video game) music.

## Stimuli
A pool of 75 music tracks was compiled, split into three categories of 25 tracks:
- `Lyrics`: tracks with discernible lyrics, mostly popular English-language songs from the 1960s to the 1990s, along with lesser-known tracks by the same artists or from the same era.
- `Orchestral`: instrumental tracks without lyrics, from film and TV soundtracks, classical music and jazz, covering a diverse range of instruments and ensembles.
- `Synthetic`: video game music. About half of the category (13 tracks) comes from the level soundtracks of Super Mario Bros, Super Mario Bros 3 and Shinobi 3, which most participants had played for other CNeuroMod datasets (see [mario](https://github.com/courtois-neuromod/mario) and [shinobi](https://github.com/courtois-neuromod/shinobi)). The remaining tracks come from other games of the same console generations (NES, Super NES, Megadrive, PlayStation).

Within each track, a segment of 45 s to 1 min 15 s covering at least one complete musical phrase was selected. A quarter of each segment was replaced by 2 to 4 silences lasting 4, 5 or 6 s, randomly placed with at least 5 s between two silences; the first 5 s of each segment were always played in full. Audio was peak-normalized to -1 dB and loudness-normalized to -18 LUFS.

## Familiarity assessment and playlists
Before scanning, participants rated their familiarity with each of the 75 tracks by listening once to 8 s excerpts containing the main theme of each piece, and answering "Yes", "No" or "Maybe".

For each participant, 60 tracks were then selected: 20 per category, of which 10 were rated familiar ("Yes") and 10 unfamiliar ("No"). Tracks were chosen so that the total duration of silence was matched between familiar and unfamiliar tracks. The 60 tracks were randomly distributed across six playlists of 10 tracks, each playlist including 5 familiar and 5 unfamiliar tracks, with no more than 3 consecutive tracks from the same group.

## Imaging sessions
Each functional run presented one playlist. Participants were instructed to listen to the tracks and to imagine the continuation of the music during the silences. After each track, they rated how well they had been able to imagine the music during the silences on a 5-point scale (1: unable to imagine anything, 5: perfect mental reconstruction). Depending on availability, participants completed 2 to 6 playlists per session. Each of the six playlists was presented three times, with the order of playlists randomized across repetitions and participants.

fMRI acquisition and preprocessing followed the standard CNeuroMod protocol.

## Questionnaires
Participants also completed the following self-report questionnaires on auditory imagery and musical expertise:
- the control subscale of the Bucknell Auditory Imagery Scale (BAIS-C);
- the Involuntary Musical Imagery Scale (IMIS);
- the Perceptual Abilities and Musical Training subscales of the Goldsmiths Musical Sophistication Index (Gold-MSI).
