# cneuromod.all

Meta-repository for the [Courtois NeuroMod (CNeuroMod)](https://www.cneuromod.ca/) project — a dense fMRI database of 6 subjects scanned since 2018 across 11 experimental paradigms. Structured as a [DataLad](https://www.datalad.org/) YODA-principles dataset: each raw dataset and derivative is an independent git+git-annex repository registered here as a submodule (43 total).

## CRITICAL: do not recurse into submodules

- **Never** run `git submodule update --init --recursive` — submodules re-expose their own sub-submodules (at differing versions for provenance); recursive cloning triggers a massive, redundant filesystem
- **Never** run `datalad install -r` for the same reason
- Most data files are **git-annex symlinks** and will appear as broken symlinks until explicitly retrieved; this is expected and normal

## Essential DataLad commands

```bash
# Clone the meta-repo (metadata only, no data)
datalad clone git@github.com:courtois-neuromod/cneuromod.all.git

# Install a single submodule (git history only, no annexed data)
datalad get -n <submodule-path>

# Retrieve actual data files inside a submodule
cd <submodule-path> && datalad get <file-or-glob>

# Save submodule pointer updates
datalad save -m "description of change"
```

## Per-dataset metadata

Each top-level dataset folder (e.g. `hcptrt/`, `anat/`) may contain two metadata files that are auto-rendered into the Sphinx documentation at build time:

- **`CITATION.cff`** — Citation File Format 1.2.0 (`type: dataset`). The `preferred-citation` block points to the paper(s) users should cite. This renders as a "How to cite" tip admonition on the dataset's doc page. Citation and contributor lists are kept separate because the key reference for a dataset (often an analysis paper) may have different authors than the people who collected/curated the data.

- **`.all-contributorsrc`** — allcontributors JSON schema. Lists contributors with `contributions` role keys (`data`, `code`, `doc`, `design`, `review`, `maintenance`, `projectManagement`, `ideas`, `mentoring`, `bug`, `userTesting`, `financial`, `question`). Renders as a "Contributors" section with emoji annotations. People without GitHub accounts omit `login`; organizations are supported.

The Sphinx pipeline in `docs/source/conf.py` discovers both files automatically — no manual wiring needed. Add a `README.md` to a dataset folder and it appears in the docs; add `CITATION.cff` and/or `.all-contributorsrc` alongside it and the citation/contributor blocks render automatically.

## Submodule structure

| Path | Type | GitHub repo |
|---|---|---|
| `anat/bids` | BIDS raw | `courtois-neuromod/anat` |
| `anat/smriprep` | sMRIPrep derivative | `courtois-neuromod/anat.smriprep` |
| `anat/smriprep.longitudinal` | sMRIPrep longitudinal | `courtois-neuromod/smriprep.longitudinal` |
| `anat/freesurfer` | FreeSurfer | `courtois-neuromod/anat.freesurfer` |
| `anat/freesurfer.longitudinal` | FreeSurfer longitudinal | `courtois-neuromod/anat.freesurfer_longitudinal` |
| `anat/atlases` | Atlases | `courtois-neuromod/anat.atlases` |
| `anat/pycortex` | PyCortex surfaces | `courtois-neuromod/anat.pycortex` |
| `floc/bids` | BIDS raw | `courtois-neuromod/floc` |
| `floc/fmriprep` | fMRIPrep | `courtois-neuromod/floc.fmriprep` |
| `floc/mriqc` | MRIQC | `courtois-neuromod/floc.mriqc` |
| `floc/rois` | ROIs | `courtois-neuromod/floc.rois` |
| `friends/bids` | BIDS raw | `courtois-neuromod/friends` |
| `friends/fmriprep` | fMRIPrep | `courtois-neuromod/friends.fmriprep` |
| `friends/mriqc` | MRIQC | `courtois-neuromod/friends.mriqc` |
| `friends/physprep` | PhysPrep | `courtois-neuromod/friends.physprep` |
| `gamepad/bids` | BIDS raw | `courtois-neuromod/gamepad` |
| `gamepad/fmriprep` | fMRIPrep | `courtois-neuromod/gamepad.fmriprep` |
| `harrypotter/bids` | BIDS raw | `courtois-neuromod/harrypotter` |
| `harrypotter/fmriprep` | fMRIPrep | `courtois-neuromod/harrypotter.fmriprep` |
| `harrypotter/physprep` | PhysPrep | `courtois-neuromod/harrypotter.physprep` |
| `hcptrt/bids` | BIDS raw | `courtois-neuromod/hcptrt` |
| `hcptrt/fmriprep` | fMRIPrep | `courtois-neuromod/hcptrt.fmriprep` |
| `mario/bids` | BIDS raw | `courtois-neuromod/mario` |
| `mario/fmriprep` | fMRIPrep | `courtois-neuromod/mario.fmriprep` |
| `mario/physprep` | PhysPrep | `courtois-neuromod/mario.physprep` |
| `movie10/bids` | BIDS raw | `courtois-neuromod/movie10` |
| `movie10/fmriprep` | fMRIPrep | `courtois-neuromod/movie10.fmriprep` |
| `movie10/mriqc` | MRIQC | `courtois-neuromod/movie10.mriqc` |
| `movie10/physprep` | PhysPrep | `courtois-neuromod/movie10.physprep` |
| `retinotopy/bids` | BIDS raw | `courtois-neuromod/retinotopy` |
| `retinotopy/fmriprep` | fMRIPrep | `courtois-neuromod/retinotopy.fmriprep` |
| `retinotopy/prf` | pRF analysis | `courtois-neuromod/retinotopy.prf` |
| `shinobi/bids` | BIDS raw | `courtois-neuromod/shinobi` |
| `shinobi/fmriprep` | fMRIPrep | `courtois-neuromod/shinobi.fmriprep` |
| `shinobi/mriqc` | MRIQC | `courtois-neuromod/shinobi.mriqc` |
| `shinobi/physprep` | PhysPrep | `courtois-neuromod/shinobi.physprep` |
| `shinobi/training` | Training data | `courtois-neuromod/shinobi_training` |
| `things/bids` | BIDS raw | `courtois-neuromod/things` |
| `things/fmriprep` | fMRIPrep | `courtois-neuromod/things.fmriprep` |
| `things/mriqc` | MRIQC | `courtois-neuromod/things.mriqc` |
| `things/behaviour` | Behaviour | `courtois-neuromod/things.behaviour` |
| `things/glm` | GLM | `courtois-neuromod/things-glm` |
| `things/glmsingle` | GLMsingle | `courtois-neuromod/things.glmsingle` |
