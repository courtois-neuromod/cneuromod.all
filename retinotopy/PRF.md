# Population Receptive Field

Voxel-wise population receptive fields were estimated with the [analyzePRF](http://kendrickkay.net/analyzePRF/) MATLAB toolbox ([GitHub](https://github.com/cvnlab/analyzePRF); commit `a3ac908`, based on release 1.6) in MATLAB R2021a.

## Preprocessing

BOLD data were preprocessed with fMRIPrep (version 20.2.6), then detrended, normalized, and averaged over repeated runs of the same aperture type (e.g., all `ring` runs). The first three volumes of each run were dropped to allow for signal equilibrium. Binary aperture masks were temporally averaged to downsample to TR-locked samples (TR = 1.49 s) and resized to 192 × 192 pixels to reduce processing time.

## pRF estimation

Whole-brain voxels were vectorized and split into chunks of up to 240 voxels, then processed in parallel with analyzePRF. Output receptive field sizes and eccentricities were converted from pixels to degrees of visual angle; polar angles were converted from compass convention to signed north–south convention.

## Surface projection and ROI delineation

Volume outputs were projected to cortical surfaces using FreeSurfer `mri_vol2surf`. Visual ROI boundaries (V1, V2, V3, hV4, VO1/VO2, LO1/LO2, TO1/TO2, and V3a/V3b) were estimated with [Neuropythy](https://pypi.org/project/neuropythy/) (version 0.11.9) using a Bayesian mapping approach that refines individual parameters with group atlas priors. Surface values were reconverted to volumes in functional native subject space (T1w) using FreeSurfer's `mri_convert`, FSL's `fslorient2std`, and Nilearn's `resample_to_img`.

The data release includes binary ROI masks in native (T1w) volume space for `sub-01`, `sub-02`, and `sub-03`.

## Pipeline

The full analysis runs in eight steps:

1. Build TR-locked binary aperture masks (ring, bar, wedge) downsampled from task frame rate to TR resolution (192×192 px).
2. Preprocess BOLD data: detrend, normalize, average across repeated runs of the same aperture type, then chunk into segments of up to 240 voxels for parallel processing.
3. Estimate pRF parameters (angle, eccentricity, RF size, R², gain) per chunk with analyzePRF in MATLAB R2021a (requires Optimization and Parallel Computing toolboxes; ~36 h/subject on Alliance Canada HPC).
4. Reassemble chunked outputs into whole-brain volumes and convert metrics to Neuropythy-compatible conventions.
5. Project volume maps to cortical surfaces with FreeSurfer `mri_vol2surf`.
6. Run Neuropythy `register_retinotopy` to refine individual pRF maps against a group HCP atlas prior and infer visual area labels (varea).
7. Convert Neuropythy surface outputs back to T1w volumes with `mri_convert` and `fslreorient2std`.
8. Resample ROI masks to functional (EPI) resolution; export binary masks for V1, V2, V3, hV4, VO1/VO2, LO1/LO2, TO1/TO2, V3a/V3b.

## Replication

Step-by-step instructions for replicating the full pipeline — including exact script calls, input/output file names, and HPC job parameters — are provided in the [pRF analysis code repository](https://github.com/courtois-neuromod/retinotopy.prf/blob/main/code/README.md).

## Reference

Kay, K.N., Winawer, J., Mezer, A., & Wandell, B.A. (2013). Compressive spatial summation in human visual cortex. *Journal of Neurophysiology*, 110(2), 481–494. <https://doi.org/10.1152/jn.00105.2013>

St-Laurent, M., Pinsard, B., Contier, O. et al. CNeuroMod-THINGS, a densely-sampled fMRI dataset for visual neuroscience. *Sci Data* 13, 141 (2026). <https://doi.org/10.1038/s41597-026-06591-y>
