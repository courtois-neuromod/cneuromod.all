# anat

## Overview
The anatomical dataset includes longitudinal anatomical images of the brain and upper spinal cord at an approximate rate of 4 sessions a year. The primary intended use of this dataset is to monitor the structural stability of the brain of participants for the duration of the study. Many quantitative measures of brain structure can also be derived and included in analyses, such as gray matter morphometry, tractography or measures of myelination. Cortical flat maps cut with TkSurfer 6.0.0 are provided with the freesurfer derivatives for visualization.

## Acquisition sequences
The MRI sequences are described in more detailed in [](Brain_anatomical_sequences) and [](Spinal_cord_anatomical_sequences), including pdfs of the Siemens exam cards.

Brain T1w, T2w and DWI were copied from the HCP aging and development protocol for Prisma MRI scanner.
Other sequences were selected and optimized by the Courtois NeuroMod team.

## Defacing
All images covering the face were anonymized by zeroing the data in the face, teeth and ears regions with a custom mask warped from the MNI space based on a linear registration of the T1w brain MRI series. This defacing script is available [here](https://github.com/courtois-neuromod/ds_prep/blob/main/mri/prepare/deface_anat.py)
