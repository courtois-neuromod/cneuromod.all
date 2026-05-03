# Downloading

All CNeuroMod data are distributed as [DataLad](https://www.datalad.org/) repositories on GitHub under the [courtois-neuromod](https://github.com/courtois-neuromod) organisation. `cneuromod.all` is the master meta-repository tracking all datasets and their derivatives.

## Repository structure

`cneuromod.all` follows [YODA principles](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html): each experimental paradigm is a top-level folder (e.g. `hcptrt/`, `friends/`, `anat/`) containing independent git submodules for each data component:

| Submodule | Contents |
|---|---|
| `<dataset>/bids` | Raw BIDS data |
| `<dataset>/fmriprep` | fMRIPrep derivatives |
| `<dataset>/mriqc` | MRIQC quality reports |
| `<dataset>/physprep` | Physiological recordings |
| `<dataset>/<content>` | Additional content |
The `Contents` section of this documentation has separate pages for contents that are common to several datasets. The `Datasets` section of this documentation features the full list of datasets and associated contents, with dedicated sections for dataset-specific contents.

## Prerequisites

- [DataLad](http://handbook.datalad.org/en/latest/intro/installation.html) (Linux, macOS, Windows)
- A GitHub account with an SSH key configured ([instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent))
- S3 credentials from the CNeuroMod data manager, required to download restricted data (see [Access](access))

## Clone the meta-repository

```bash
# Clone metadata only — no data files are downloaded
datalad clone git@github.com:courtois-neuromod/cneuromod.all.git
cd cneuromod.all
```

**Important:** Do not use `datalad install -r` or `git submodule update --init --recursive`. Submodules re-expose their own sub-submodules at differing versions for provenance tracking; recursive installation triggers a massive redundant filesystem traversal.

## Install a submodule

Submodules are installed individually as needed. This fetches git history but no annexed data files:

```bash
datalad get -n hcptrt/bids
```

## Download data files

Once a submodule is installed, retrieve actual data files with `datalad get`:

```bash
# Get all files in a submodule
cd hcptrt/bids && datalad get .

# Get a specific subset (e.g. all MNI-space functional outputs)
datalad get hcptrt/fmriprep/sub-*/ses-*/func/*space-MNI152NLin2009cAsym_*

# Use -J n to download in parallel with n threads
datalad get -J 4 hcptrt/bids/sub-01
```

## S3 credentials

Restricted data are stored on an Amazon S3 fileserver. Set your credentials in the terminal before downloading:

```bash
export AWS_ACCESS_KEY_ID=<s3_access_key>
export AWS_SECRET_ACCESS_KEY=<s3_secret_key>
```

Credentials are provided by the data manager after approval of an access request (see [Access](access)).

## Versioning

Cloning gives you the latest stable release by default. To reproduce results from a specific release:

```bash
git checkout 2020
```

## Updates

To pull the latest release into an existing clone:

```bash
datalad update -r --merge --reobtain-data
```

The `--reobtain-data` flag automatically re-downloads files you had previously retrieved if they were modified upstream.
