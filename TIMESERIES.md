# timeseries

## Overview
fMRI timeseries that capture local fluctuations in the BOLD response over time. `<dset>.timeseries` are extracted with the [cneuromod_extract_tseries library](https://github.com/courtois-neuromod/cneuromod_extract_tseries) from `<dset>.fmriprep` derivative datasets. BOLD signal is standardized, detrended, smoothed, masked, vectorized and saved into 2D arrays that can easily be integrated into machine-learning pipelines.

## Outputs
We extracted four kinds of timeseries:
- `schaefer1000`: a broadly-adopted cortical parcellation (Schaefer2028_1000Parcels7Networks) in standard MNI space. This parcellation was used to extract the BOLD signal for brain encoding analyses for the Algonauts 2025 Challenge.
- `cneuromod2026`: a custom parcellation in standard MNI space that extends beyond the schaefer1000 cortical parcels to also include subcortical and cerebellar parcels. Of note, the signal included in this parcellation was masked with selective individual grey matter masks derived from freesurfer anatomical segmentation.
- `voxel_mni`: a voxelwise signal extraction in MNI space (MNI152NLin2009cAsym). To facilitate fine-grained multi-subject analyses, the signal was masked using the same inclusive grey matter mask across all subjects. Columns in the timeseries arrays correspond to the same voxels aligned spatially across individuals.
- `voxel_native`: a voxelwise signal extraction in native (T1w) space extracted within a selective individual grey matter mask derived from freesurfer anatomical segmentation. These timeseries offer a selective fine-grained spatial representation optimized to capture the most signal in each subject while keeping the number of voxels relatively low. 

-----------------

## Code
fMRI timeseries are extracted with scripts from the [cneuromod_extract_tseries library](https://github.com/courtois-neuromod/cneuromod_extract_tseries) installed as a submodule under `./code` inside {dset}.timeseries repositories.

Timeseries extraction steps are the following:
- **build an EPI mask per subject applied to every dataset run.** This mask reconciles anatomical specifications (e.g., grey matter mask) and functional signal properties (run-specific fmriprep masks).
- **customize the parcellation atlas for each subject**. i.e., resample the parcellation atlas and mask it with the subject' EPI mask to exclude no-signal voxels from parcel signal averaging (parcel-extraction only).
- **denoise, standardize and smooth EPI volumes**. Use Niftimasker to mask EPI volumes with the EPI mask, standardize (z-score), smooth (fwhm=5.0) and denoise each run's signal. Denoising is performed by selecting fmriprep confounds with nilearn [load_confounds](https://nilearn.github.io/dev/modules/generated/nilearn.interfaces.fmriprep.load_confounds_strategy.html) to do high pass filtering and regress out 24 motion parameters (6 translation/rotation parameters, their quadratic terms and derivatives), global signal and average white matter and CSF signal.
- **extract timeseries**. For each pre-processed EPI volumes, vectorize the signal per voxel (with Niftimasker) or averaged per parcel (with NiftiLabelMasker).
- **save timeseries**. Save each run's timeseries into a nested HDF5 File organized per run and per session for each subject.

To extract a subject’s timeseries, the following bash scripts were ran (`run_extract_schaefer1000.sh` and `run_extract_cneuromod26.sh` for parcel extraction, and `run_extract_voxt1w.sh` and `run_extract_voxmni.sh` for voxelwise extraction in native and MNI space, respectively), specifying the subject’s number.

For example, to extract sub-01’s voxelwise signal in native space:
```bash

sbatch code/run_extract_voxt1w.sh  01
```

-----------------

## File details

**cneuromod2026**. Timeseries are extracted in MNI152NLin2009cAsym space with a custom 1134-parcel atlas that combines 996 cortical parcels from Schaefer2018 (1000 parcels, 7 networks), 50 subcortical parcels from Tian2020 (S3), and 88 cerebellar parcels from Nettekoven2024 (Asym128). The atlas is masked with a selective individual grey matter mask. The following files are saved per subject under ``timeseries/cneuromod2026/sub-<subject>/``:
- ``sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_label-GMfromFS_desc-indivFunc_mask.nii.gz``, the grey matter mask that delineates the brain voxels included in the timeseries. For each subject, a custom grey matter mask was derived from individual Freesurfer anatomical segmentation (warped to MNI space), intersected with a functional mask derived from run-wise functional masks estimated with fmriprep for the Friends dataset (the largest CNeuroMod dataset).
- ``sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_atlas-cneuromod26_desc-1134Parcels_dseg.nii.gz``, the parcellation atlas masked with the subject’s grey matter mask in MNI space.
- ``sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_atlas-cneuromod26_desc-1134Parcels_timeseries.h5``, the parcel timeseries. Run-wise timeseries are saved as 2D arrays of dim=(TRs, parcels) nested per fMRI session.

**schaefer1000**. Timeseries are extracted in MNI152NLin2009cAsym space with the Schaefer2018 1000 parcels, 7 networks parcellation atlas, masked with an inclusive grey matter mask. This parcellation was used to extract the BOLD signal for the Algonauts 2025 Challenge. The following files are saved per subject under ``timeseries/schaefer1000/sub-<subject>/``:
- ``sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_label-GMfromTemplate_desc-indivFunc_mask.nii.gz``, the grey matter mask that delineates the brain voxels included in the timeseries. For each subject, the template MNI152NLin2009cAsym grey matter mask was intersected with a functional mask derived from run-wise functional masks estimated with fmriprep for the Friends dataset.
- ``sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_atlas-Schaefer18_desc-1000Parcels7Networks_dseg.nii.gz``, the parcellation atlas masked with the subject’s grey matter mask in MNI space.
- ``sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_atlas-Schaefer18_desc-1000Parcels7Networks_timeseries.h5``, the parcel timeseries. Run-wise timeseries are saved as 2D arrays of dim=(TRs, parcels) nested per fMRI session.

**voxel_mni**. Voxelwise timeseries are extracted in MNI152NLin2009cAsym space within the same inclusive grey matter mask across all CNeuroMod subjects. The following files are saved under ``timeseries/voxel_mni/``:
- ``task-<dset>_space-MNI152NLin2009cAsym_label-GMfromTemplate_desc-AllFunc_mask.nii.gz``. For each subject, the template MNI152NLin2009cAsym grey matter mask was intersected with a functional mask derived from run-wise functional masks estimated with fmriprep for the Friends dataset. The final mask is the intersection of all six individual subject masks.
- ``sub-<subject>/sub-<subject>_task-<dset>_space-MNI152NLin2009cAsym_desc-voxelwise_timeseries.h5``, the voxelwise timeseries. Run-wise timeseries are saved as 2D arrays of dim=(TRs, voxels) nested per fMRI session. Columns correspond to the same voxels aligned spatially across individuals.

**voxel_native**. Voxelwise timeseries are extracted in native (T1w) space within a selective individual grey matter mask. The following files are saved per subject under ``timeseries/voxel_native/sub-<subject>/``:
- ``sub-<subject>_task-<dset>_space-T1w_label-GMfromFS_desc-indivFunc_mask.nii.gz``, the grey matter mask used to delineate timeseries voxels. This mask was derived from individual Freesurfer anatomical segmentation, and intersected with a functional mask derived from run-wise functional masks estimated with fmriprep for the Friends dataset.
- ``sub-<subject>_task-<dset>_space-T1w_desc-voxelwise_timeseries.h5``, the voxelwise timeseries. Run-wise timeseries are saved as 2D arrays of dim=(TRs, voxels) nested per fMRI session.


