# floc ROIs

Subject-specific functional regions of interest (ROIs) derived from the fLoc dataset using a first-level GLM and Kanwisher-group group parcels as spatial priors.

## Task

Four participants (`sub-01`, `sub-02`, `sub-03`, `sub-05`) completed six sessions of the fLoc functional localizer task, based on [pyfLoc](https://github.com/NBCLab/pyfLoc) (adapted from the [Stanford VPNL fLoc task](https://doi.org/10.1523/JNEUROSCI.4822-14.2015)). Each session included two functional runs (~3.85 min) of ~6 s blocks of rapidly presented images from five categories: `faces`, `places`, `bodies`, `objects`, and `characters`. Subjects performed a one-back repetition-detection task while fixating a central red dot. Baseline blocks (fixation only) were intermixed throughout. The two runs per session used complementary sub-category sets (e.g., house vs. corridor for `places`; adult faces in both).

## Analysis pipeline

ROIs are derived through a six-step pipeline; full scripts and instructions are in `code/README.md` inside the `floc/rois` submodule.

1. **Design matrices** — GLM design matrices are built from each subject's `*events.tsv` files across all fLoc sessions (~6 sessions, 2 runs each).
2. **First-level GLM** — A nilearn first-level GLM is run on the fLoc BOLD data, producing t-score and beta maps for all nine contrasts (see below).
3. **Warp Kanwisher parcels to subject space** — Group parcels (n=40, CVS space) from the [Kanwisher lab](https://web.mit.edu/bcs/nklab/GSS.shtml#download) are warped CVS → MNI (FreeSurfer/FSL) → T1w (ANTs using fMRIPrep transforms) for each subject.
4. **Parcel masks** — Binary parcel masks (face, scene, body, object) are created as the intersection of each warped group parcel and above-threshold voxels in the subject's contrast map (α = 0.0001).
5. **ROI masks** — Subject-specific ROI masks (FFA, OFA, pSTS, PPA, OPA, MPA, EBA) are derived by ranking voxels within an enlarged group-derived ROI mask by t-score and selecting the top fraction proportional to the group ROI size.
6. **Manual flat-map ROIs** — For `sub-01`, `sub-02` and `sub-03`, ROI boundaries were additionally drawn manually on cortical flat maps using Inkscape and PyCortex.

## GLM contrasts

Nine contrasts are estimated per subject from all fLoc sessions pooled together:

- **Kanwisher-style**: `faceMinObject`, `sceneMinObject`, `bodyMinObject`, `objectMinRest`
- **NSD-style** (each category vs. all others): `faces`, `places`, `bodies`, `characters`, `objects`

## ROIs

Seven bilateral ROIs are derived by intersecting subject t-score maps with group-level Kanwisher parcels warped from CVS to native (T1w) space:

| ROI | Full name | Contrast |
|-----|-----------|----------|
| FFA | Fusiform Face Area | face |
| OFA | Occipital Face Area | face |
| pSTS | Posterior Superior Temporal Sulcus | face |
| PPA | Parahippocampal Place Area | scene |
| OPA | Occipital Place Area | scene |
| MPA | Medial Place Area | scene |
| EBA | Extrastriate Body Area | body |

Each ROI is available as left-hemisphere, right-hemisphere and bilateral binary masks in native subject (T1w) space. For `sub-06`, who did not complete the fLoc task, ROI masks were derived from voxelwise noise ceilings from the main THINGS task.

For `sub-01`, `sub-02` and `sub-03`, ROI boundaries were additionally drawn manually on cortical flat maps and are available via `anat/pycortex`.
