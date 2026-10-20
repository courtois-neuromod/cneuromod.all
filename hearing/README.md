# hearing

## Overview
Clinical audiology tests administered to all six CNeuroMod participants (`sub-01` to `sub-06`) around MRI sessions, to check that years of repeated scanning, with hearing protection, did not damage their hearing. Tests were run by a trained clinical audiologist over about 1.5 years, starting from baseline measures acquired in January–February 2021. The number of hearing sessions differs across participants, from 4 for `sub-04`, who suspended scanning during the protocol, to 18 for `sub-05`, who has a pre-existing hearing impairment (no otoacoustic emissions in the left ear) and was therefore followed with an intensive five-week pure-tone audiometry protocol.

What makes the dataset distinctive is that hearing was measured immediately before and after a scan session, to capture temporary threshold shifts, and again 48 hours to 7 days after a scan session, to compare against baseline and capture lasting changes. It combines conventional (0.25–8 kHz) and extended high-frequency (9–20 kHz) pure-tone audiometry with distortion product otoacoustic emissions (DPOAEs), which probe outer hair cell function and can reveal subclinical changes before thresholds shift. Participants had no measurable hearing damage attributable to MRI noise. See Fortier et al. (2025) for the full analysis.

## Tests
Each session started with a routine check of the outer and middle ear. The tests are stored as BIDS-like `beh` files, one task per test:

- **Tymp** (`task-Tymp`): tympanometry, 226 Hz probe tone.
- **Reflex** (`task-Reflex`): ipsilateral stapedial reflex at 0.5, 1, 2 and 4 kHz and with broadband noise.
- **PTA** (`task-PTA`): air-conduction pure-tone audiometry, standard (0.25–8 kHz) and extended high-frequency (9–20 kHz) ranges, in 5 dB HL steps.
- **DPOAE** (`task-DPOAE`) and **DPGrowth** (`task-DPGrowth`): distortion product otoacoustic emissions (F2 = 1–10 kHz, F2/F1 = 1.22, L1/L2 = 65/55 dB SPL) and their growth function.
- **TEOAE** (`task-TEOAE`): transient-evoked otoacoustic emissions.
- **MTX** (`task-MTX`): matrix speech-in-noise perception test, in French and English.

The `sessions.json` file describes the session types: three baselines (start of the CNeuroMod project, start and end of the audiology protocol) and numbered experimental sessions linked to a scan session.

## Acquisition
Tests were run in a GENIE GN-17 soundproof booth, with MADSEN Zodiac (tympanometry, reflex) and MADSEN Astera2 (audiometry) equipment, and Otodynamics ILO systems (OAEs). Participants were scanned at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM, Montréal. The data are behavioural only; there are no imaging derivatives.
