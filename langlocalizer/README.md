# langlocalizer

## Overview
Four participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`) completed three sessions, one week apart, of standard language localizers while fMRI was acquired. All four are right-handed and fluent in both English and French; two are native English speakers and two native French speakers. Each session comprises two runs of each of four tasks (about 38 min of acquisition), interleaved in randomized order with non-language CNeuroMod tasks.

What makes the dataset distinctive is that it systematically crosses modality (reading vs. listening) and language (English vs. French) within the same individuals, with three repetitions of the whole protocol. This deep-sampling design makes it possible to separate variability in the topography of the language network between participants from variability within a participant across sessions, modalities and languages. It complements the CNeuroMod HCP-TRT and movie-watching data, and was used in the manuscript *Deep phenotyping the language network* ([Bilgin et al., 2025](https://openreview.net/pdf?id=07S1CPoQYP)) to define subject-specific language regions of interest. Those ROIs are not part of this dataset: they will be distributed with the atlases in `anat/atlases`.

## Tasks
All localizers follow block designs contrasting intact language with a control, from the [Fedorenko lab's functional localizers](https://evlab.mit.edu/funcloc):

- **reading** (`task-reading`, VisualLoc): English sentences vs. non-word sequences ([Fedorenko et al., 2010](https://doi.org/10.1152/jn.00032.2010)). 5 min 58 s per run, 16 experimental blocks of 18 s (8 per condition) and 5 fixation blocks of 14 s.
- **listening** (`task-listening`, AudioLoc): English auditory passages vs. acoustically degraded versions of the same passages ([Scott et al., 2016](https://doi.org/10.1152/jn.00459.2016)). Same block structure as the reading task.
- **aliceEn** and **aliceFr** (AliceLoc, [Ayyash et al., 2021](https://doi.org/10.1101/2021.05.20.445018)): passages from *Alice in Wonderland* in English or French, acoustically degraded versions of the passages, and passages in an unfamiliar language (Tamil). 4 min 12 s per run, 12 experimental blocks of 18 s (4 per condition) and 4 fixation blocks of 12 s. In the manuscript the two versions are recoded as first (L1) and second (L2) language of each participant.

Tasks were presented with custom PsychoPy scripts synchronized to the scanner trigger. Sounds were delivered through Sensimetrics S15 insert headphones.

## Acquisition
Data were acquired on a Siemens Prisma Fit 3T scanner with a 64-channel head/neck coil at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM, Montréal, following the CNeuroMod protocol (TR = 1.49 s, 2 mm isotropic voxels, multiband acceleration factor 4).

## Preprocessing
- `fmriprep`: fMRIPrep preprocessing.
- `mriqc`: image quality metrics.
- `tsnr`: temporal SNR maps.
- `timeseries`: parcellated timeseries.
