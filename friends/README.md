# friends

## Overview

This dataset contains functional MRI (fMRI) data acquired while 6 CNeuroMod participants watched episodes of the American sitcom *Friends* in English. The dataset covers seasons 1–7 (~65 hours of content per subject), making it one of the largest naturalistic fMRI datasets available. fMRI responses span the whole brain and are synchronized with multimodal movie stimuli — visual frames, audio samples, and time-stamped language transcripts.

The Friends dataset is the primary training corpus for the [Algonauts Project 2025 Challenge](https://algonautsproject.com/) (*How the Human Brain Makes Sense of Multimodal Movies*), which benchmarks computational encoding models of multimodal brain responses.

## Stimulus

Each episode provides three synchronized stimulus streams:

- **Visual frames** — continuous video at the original frame rate
- **Audio samples** — stereo audio track
- **Language transcripts** — time-stamped English subtitles

Each episode is split into two scanning segments (a/b) with a small overlap so participants can catch up with the storyline between runs. The BIDS `task` entity encodes season, episode, and segment as `task-s<season>e<episode>[ab]` (e.g., `task-s01e01a`).

:::{important}
A mistake happened when ripping the first season, causing `s01e01` and `s01e06` to be swapped in name and order of presentation. Files were renamed afterward to match external data such as annotations. However the order of presentation remains, slightly disrupting the storyline presented to the participant.
:::

## Coverage

All six subjects completed seasons 1–6, with one exception: `sub-04` only completed seasons 1–4 (and a few segments of season 5). Season 7 (~10 hours) is included in the dataset; fMRI responses for that season are withheld as a held-out in-distribution test set for the Algonauts 2025 Challenge.
