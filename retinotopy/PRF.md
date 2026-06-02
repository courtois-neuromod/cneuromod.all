# Population Receptive Field

Voxel-wise population receptive fields were estimated with the [analyzePRF](http://kendrickkay.net/analyzePRF/) MATLAB toolbox ([GitHub](https://github.com/cvnlab/analyzePRF); commit `a3ac908`, based on release 1.6) in MATLAB R2021a.

## Preprocessing

BOLD data were preprocessed with fMRIPrep (version 20.2.6), then detrended, normalized, and averaged over repeated runs of the same aperture type (e.g., all `ring` runs). The first three volumes of each run were dropped to allow for signal equilibrium. Binary aperture masks were temporally averaged to downsample to TR-locked samples (TR = 1.49 s) and resized to 192 × 192 pixels to reduce processing time.

## pRF estimation

Whole-brain voxels were vectorized and split into chunks of up to 240 voxels, then processed in parallel with analyzePRF. Output receptive field sizes and eccentricities were converted from pixels to degrees of visual angle; polar angles were converted from compass convention to signed north–south convention.

## Surface projection and ROI delineation

Volume outputs were projected to cortical surfaces using FreeSurfer `mri_vol2surf`. Visual ROI boundaries (V1, V2, V3, hV4, VO1/VO2, LO1/LO2, TO1/TO2, and V3a/V3b) were estimated with [Neuropythy](https://pypi.org/project/neuropythy/) (version 0.11.9) using a Bayesian mapping approach that refines individual parameters with group atlas priors. Surface values were reconverted to volumes in functional native subject space (T1w) using FreeSurfer's `mri_convert`, FSL's `fslorient2std`, and Nilearn's `resample_to_img`.

The data release includes binary ROI masks in native (T1w) volume space for `sub-01`, `sub-02`, and `sub-03`.

## Reference

Kay, K.N., Winawer, J., Mezer, A., & Wandell, B.A. (2013). Compressive spatial summation in human visual cortex. *Journal of Neurophysiology*, 110(2), 481–494. <https://doi.org/10.1152/jn.00105.2013>

St-Laurent, M., Pinsard, B., Contier, O. et al. CNeuroMod-THINGS, a densely-sampled fMRI dataset for visual neuroscience. *Sci Data* 13, 141 (2026). <https://doi.org/10.1038/s41597-026-06591-y>
