# friends

## Overview

This dataset contains functional MRI (fMRI) data acquired while 6 CNeuroMod participants watched episodes of the American sitcom *Friends* in English. The dataset covers seasons 1–7. fMRI responses span the whole brain and are synchronized with multimodal movie stimuli — visual frames, audio samples, and time-stamped language transcripts.

The Friends dataset is the primary training corpus for the [Algonauts Project 2025 Challenge](https://algonautsproject.com/) (*How the Human Brain Makes Sense of Multimodal Movies*), which benchmarks computational encoding models of multimodal brain responses.

## Stimulus

Each episode provides three synchronized stimulus streams:

- **Visual frames** — continuous video at the original frame rate
- **Audio samples** — stereo audio track
- **Language transcripts** — time-stamped English subtitles

Each episode is split into multiple scanning segments (typically a/b, and a/b/c/d for double episodes) of ~12 minutes each. Segments have a small overlap so participants can catch up with the storyline between runs. The BIDS `task` entity encodes season, episode, and segment as `task-s<season>e<episode>[ab]` (e.g., `task-s01e01a`).

:::{important}
A mistake happened when the pilot episode (`s01e01`) was accidentally skipped at the beginning of the first season. It was shown to participants after they had watched episodes `s01e02` to `s01e06`, causing a slight disruption in the storyline. In the latest release, files have been renamed to match the episodes’ intended order (rather than the order in which they were administered) and to be consistent with external data such as annotation corpora.
:::

## Coverage

All six subjects completed seasons 1–7, with one exception: `sub-04` only completed seasons 1–4 (and a few segments of season 5). Stimuli from season 7 (~10 hours) are included in the released dataset; fMRI responses for that season are withheld as a held-out in-distribution test set, as currently featured in the Algonauts 2025 Challenge and to appear in the future CNeuroMod benchmark.
