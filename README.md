# Courtois NeuroMod

The [Courtois NeuroMod project](https://www.cneuromod.ca/) is a dense fMRI database collected on 6 subjects since 2018 across a broad range of cognitive tasks. Full documentation — dataset descriptions, access instructions, and download guides — is available at [docs.cneuromod.ca](https://docs.cneuromod.ca).

## Repository structure

`cneuromod.all` is a [DataLad](https://www.datalad.org/) YODA meta-repository. Each experimental paradigm is a top-level folder (e.g. `hcptrt/`, `friends/`, `anat/`) containing independent git submodules for raw BIDS data, fMRIPrep derivatives, MRIQC reports, and other processing outputs. Most data files are git-annex symlinks and must be explicitly retrieved with `datalad get`.

## License

The CNeuroMod data are shared under a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

## How to cite

We kindly ask that all publications using CNeuroMod datasets include the following paragraph in their acknowledgement section:

> The Courtois project on neural modelling was made possible by a generous donation from the Courtois foundation, administered by the Fondation Institut Gériatrie Montréal at CIUSSS du Centre-Sud-de-l'île-de-Montréal and the University of Montreal. The Courtois NeuroMod team is based at "Centre de Recherche de l'Institut Universitaire de Gériatrie de Montréal", with several other institutions involved. See the CNeuroMod documentation for an up-to-date list of contributors (https://docs.cneuromod.ca).
