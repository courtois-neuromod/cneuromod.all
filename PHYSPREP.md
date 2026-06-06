# PhysPrep

## Overview
The physiological data were preprocessed using a pipeline developed in the context of the CNeuroMod project, called [Physprep](https://github.com/courtois-neuromod/physprep).
Physprep is a pipeline that segments, cleans and processes PPG, ECG, EDA, and respiratory (RSP) signals
from minimal user input. The Physprep pipeline integrates open access python packages including Phys2Bids,
NeuroKit2, and Systole.

## Outputs
The description of participant, session, task and event tags can be found in the Datasets section.

Each participant folder (`sub-*`) contains the following outputs alongside the fMRI data:
- `ses-*/func`
  - `*_physio.tsv.gz` : raw segmented biosignals.
  - `*_physio.json` : contains tsv columns names, start time, and signal sampling frequency information.

The derivatives can be found under the `<dataset>.physprep` folders:
- `ses_*/func`
  - `*_desc-preproc_physio.tsv.gz` : processed time series.
  - `*_desc-physio_events.tsv` : extracted sparse features.
  - `*_desc-quality.json` : quality assessment

## Preprocessing pipeline description
The workflow developed to process the physiological data is based mainly on Phys2Bids, Scipy, Neurokit2 (for the specific dependencies, please check the [requirements.txt](https://github.com/courtois-neuromod/physprep/blob/main/requirements.txt)).

The following section details the post-acquisition filtering procedure used for each physiological modality.

### Photoplethysmography

The PPG timeseries were first downsampled to 1000 Hz, before being filtered following recommandations given by [Elgendi et al. 2013](https://doi.org/10.1371/journal.pone.0076585). The artefacts were removed using a bidirectional butterworth bandpass filter (low cutoff: 0.5 Hz; high cutoff: 8 Hz; order: 3). A notch filter was then applied to remove remaining artefacts (Q: 100; see [Bottenhorn et al., 2021](https://doi.org/10.1101/2021.04.01.437293)). Systolic peaks were then detected using the method described in [Elgendi et al. (2013)](https://doi.org/10.1371/journal.pone.0076585), and implemented in NeuroKit2 (see [`ppg_findpeaks`](https://neuropsychology.github.io/NeuroKit/functions/ppg.html#ppg-findpeaks) documentation). Systolic peaks corrected using the method implemented in the Neurokit2 package. Peak placements were corrected using the peak-to-peak differences: intervals between peaks outside of the 0.5-1.5 seconds range were identified as outliers, and were corrected (see [`signal_fixpeaks`](https://neuropsychology.github.io/NeuroKit/functions/signal.html#signal-fixpeaks) documentation).

### Electrocardiography

The ECG signals were downsampled to 1000 Hz. The ECG filtering procedure was implemented as per the [manufacturer application notes](https://www.biopac.com/wp-content/uploads/app242x.pdf). Namely, a bidirectional butterworth highpass filter (cutoff: 2 Hz; order: 2) was first apply to remove low frequency artefacts such as respiration and baseline wander. A second-order IIR notch digital filter was performed to filter fundamental and specific harmonics (Q: 100; see [manufacturer application notes](https://www.biopac.com/wp-content/uploads/app242x.pdf) and [Bottenhorn et al., 2021](https://doi.org/10.1101/2021.04.01.437293)). A bidirectional butterworth lowpass filter (cutoff: 40 Hz; order: 2) was finally applied. The R-peaks were detected using a probabilistic approach as implemented in the [NeuroKit2 ProMAC method](https://neuropsychology.github.io/NeuroKit/functions/ecg.html#ecg-peaks). R-peaks were corrected using the same procedure as described above for the systolic peak detection.

### Electrodermal activity

The EDA filtering procedure was implemented as per [NeuroKit2 default EDA cleaning method](https://neuropsychology.github.io/NeuroKit/functions/eda.html#preprocessing). Since EDA signal is characterised by low-frequency components and MRI gradients introduce high-frequency artefacts, a bidirectional butterworth lowpass filter (cutoff: 3 Hz; order: 4) was employed to clean the signal, as suggested by [Privratsky et al. (2020)](https://doi.org/10.1016/j.ijpsycho.2020.09.015). However, unlike what is proposed in that article, we did not apply a highpass filter in order to keep the tonic component of the EDA signal. The signal was than downsample to 1000 Hz. After the filtering procedure, the EDA signal was decomposed into its phasic and tonic components using the method implemented in Biopac's Acqknowledge (i.e. highpass filtering with a cutoff of 0.05 Hz). From the extracted phasic component, the skin conductance responses were detected by finding the local maxima in the signal (minimum relative amplitude of 0.1).

### Respiratory activity

The RSP filtering procedure was implemented as per [Khodadad et al., 2018](https://doi.org/10.1088/1361-6579/aad7e6), which includes a bidirectional
butterworth bandpass filter (low cutoff: 0.05 Hz; high cutoff: 3 Hz; order: 2). The lower cutoff was set to preserve breathing rate higher than 3 breath
per minute. The signal was than downsample to 1000 Hz. The peaks and troughs were identified on the downsampled signal as per [Khondadad et al. (2018)](https://doi.org/10.1088/1361-6579/aad7e6).


## QC-ing pipeline description
In order to evaluate the usability of the physiological data, quality indices were calculated for each modality on the filtered signals. These signals were
analysed in 1-minute consecutive windows for each run. The quality assessment is summarized in the `*_desc-quality.json` files provided for each run, which contain the percentage of valid windows across the run for each modality. That percentage was used to provide a `Pass` or `Fail` assessment, where the quality of the run is considered acceptable (`Pass`) if more than 80% of the windows in a run were considered as acceptable.

:::{important}
Even if a quality assessment is provided for each run, it is the responsibility of the researchers to make sure the data met their quality requirements.
:::

### Cardiac signals

We assessed the quality of cardiac signals (PPG and ECG) for each run based on normal NN intervals mean and NN intervals standard deviation. One-minute segments were classified as good if the mean of NN intervals was within the range of 600 and 1200, and if the standard deviation was below 300. Based on the number of segments classified as good,
we provided the percentage of the run containing cardiac signals within the normal NN intervals range. Futher quality checks should be carried out to ensure that the
available cardiac signal is suitable for a given analysis.

### Electrodermal activity

The quality of the signal was assessed for each one-minute window based on the procedure proposed by [Böttcher et al. (2022)](https://doi.org/10.1038/s41598-022-25949-x). This method uses a dual criterion based on the rate of amplitude change (RAC) and a threshold on the signal amplitude.

### Respiratory activity

To ensure that the respiratory waveforms are within a normal range, a threshold of 0.5 Hz was used on the signal rate. If the averaged respiratory rate within a specific
window was below 0.5 Hz, the signal was considered normal. However, if the averaged respiratory rate exceeded that threshold, the signal window was classified as having
poor quality. Futher quality checks should be carried out to ensure that the available respiratory signal is suitable for a given analysis.
