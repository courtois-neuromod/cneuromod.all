# floc ROIs

Subject-specific functional regions of interest (ROIs) derived from the fLoc dataset using a first-level GLM and Kanwisher-group group parcels as spatial priors.

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
