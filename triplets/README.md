# triplets
## Overview

Four right-handed, English–French bilingual participants (`sub-01`, `sub-02`, `sub-03`, `sub-06`) completed repeated sessions of two complementary fMRI tasks designed to investigate the neural representations of individual words and their semantic relationships. The dataset combines single-word familiarity judgments with semantic association judgments on triplets of words, enabling the investigation of lexico-semantic processing within individuals across repeated measurements.

The stimuli comprise 1,588 unique English words spanning a broad range of lexical, psycholinguistic, perceptual, and conceptual features, organized into 709 triplets. The experimental design allows researchers to investigate how properties such as word length, frequency, orthographic complexity, concreteness, and sensorimotor features modulate brain responses to individual words, and how these representations relate to semantic decisions involving multiple words.

The dataset is part of the CNeuroMod deep-phenotyping initiative and supports the study of individual variability in semantic representations and their organization across the cortex. The experimental paradigm and initial analyses are described in Deep phenotyping lexico-semantic processing: the cneuromod-triplets dataset (Licata et al., 2023).



## Tasks
The protocol comprises a behavioral word-reading preparation task and two fMRI tasks: single-word familiarity judgments and semantic association judgments involving triplets of words.

- **Single-word reading (pre-scan preparation):** Before scanning sessions, participants reviewed the experimental word list, identified words whose meanings were unfamiliar, and consulted their definitions. This preparation was intended to familiarize participants with the vocabulary used in the imaging tasks.
- **Single-word familiarity (task-singlewords_fam):** Participants viewed individual English words and rated their subjective familiarity with the concept represented by each word on a three-point scale: 1 (unfamiliar), 2 (somewhat familiar), or 3 (familiar). Each word was presented visually for 0.5 s, preceded and followed by fixation, with a jittered interstimulus interval. The task was designed to characterize neural responses to individual words and their modulation by lexical, perceptual, and semantic properties.
- **Semantic association (task-triplet):** Participants viewed three English words simultaneously and selected the word they considered least related in meaning to the other two. Each triplet was presented for 4 s, with a jittered interstimulus interval. Participants were instructed to respond intuitively, without extended deliberation, and to make their best guess when unfamiliar with a word. The task measures context-dependent semantic association judgments and associated response times. Because semantic relationships can be subjective, there is no single universally correct response for every triplet.

Both fMRI tasks used repeated stimulus presentations across sessions, allowing the assessment of within-participant variability in behavioral judgments and neural responses.

## Acquisition
Data were acquired on a Siemens Prisma Fit 3T scanner with a 64-channel head/neck coil at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM, Montréal, following the CNeuroMod protocol (TR = 1.49 s, 2 mm isotropic voxels, multiband acceleration factor 4).

## Preprocessing

The following derivatives may be available through the CNeuroMod processing pipelines, depending on the dataset release:

- `fmriprep`: fMRIPrep preprocessing.
- `mriqc`: image quality metrics.
- `tsnr`: temporal signal-to-noise ratio maps.
- `timeseries`: parcellated time series.