# Dataset gallery artwork

Tiles rendered by `_render_dataset_gallery()` on the documentation landing page.

A dataset gets an image tile when a file named `<dataset>.jpg` or `<dataset>.png` exists
here; otherwise it falls back to the per-dataset emoji in
`docs/source/_ext/constants.py` (`_DATASET_EMOJI`). Dropping a new image in this
directory is all that is needed to promote a card — no code change.

## Provenance

All files were retrieved on 2026-09-02 from the legacy gallery at
<https://www.cneuromod.ca/gallery/datasets/>, where they have been published since the
site's inception.

| File | Source file | Note |
|---|---|---|
| `anat.jpg` | `anat.jpg` | unchanged |
| `floc.jpg` | `floc.jpg` | unchanged |
| `hcptrt.png` | `hcptrt.png` | unchanged |
| `movie10.jpg` | `hiddenfigures.jpg` | downscaled 1800×776 → 600×259 |
| `retinotopy.jpg` | `retinotopy.jpg` | unchanged |
| `things.jpg` | `things.jpg` | unchanged |

Several of these are third-party cover art for the stimuli used in the corresponding
experiments (*Hidden Figures*). They illustrate the stimulus material and are reproduced
here as they already appear on the project website.

Aspect ratios and background colours vary widely; the `.ds-tile` rules in
`../custom.css` normalise them (fixed tile height, `object-fit: contain`, theme-aware
letterbox background), so images need no cropping or flattening before being added.

## Licensing

Per-image copyright and reuse notes are tracked in [`LICENSES.md`](LICENSES.md) in this
directory. Add an entry there for every new tile — these are all third-party cover art
used to illustrate experiment stimuli, not project-owned images, so provenance matters.
