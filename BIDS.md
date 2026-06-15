# BIDS

All functional and anatomical data has been formatted in [BIDS](https://bids.neuroimaging.io/), for more information visit the Brain Imaging Data Structure documentation [site](https://bids-specification.readthedocs.io/en/stable/).

Some of the files do not follow the main BIDS convention:
- Anatomical sequences with multiple contrasts are following [BEP001](https://bids.neuroimaging.io/bep001).
- Spinal cord imaging use Body Part tag proposed in [BEP025](https://bids.neuroimaging.io/bep025) (`bp-cspine`) to allow to distinguish them from brain anatomical images acquired with the same contrasts.

Note that BIDS session names have no meaning apart from being data acquired in the same session. The number of runs, the tasks and their order within each session will not match from one participant to another. Note that a few session indices are skipped if the whole session was discarded for various scanning issues.
