# gamepad

## Overview
This dataset was acquired as a validation study of the CNeuroMod videogame controller. The CNeuromod videogame controller is an open source, custom-built, fiber-optic, MRI compatible video game controller, designed by our team engineer, Mr. André Cyr, and described in [Harel et al. (2023)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0290158). For a detailed description of the controller, including building instructions visit this [site](https://controller-doc.readthedocs.io/en/latest/).

## Behavioural and imaging sessions
The gamepad dataset contains both fMRI and behavioural data acquired on 4 participants (`sub-01`, `sub-02`, `sub-03` and `sub-06`) during a simple cued-response task in which the participants were instructed to press the various controller buttons for short and long durations (5 blocs of 10 trials per condition).

For each subject we acquired 8 sessions, of two runs each. Four of the sessions were acquired in the MRI scanner using our typical setup (i.e 64-channel head coil) along with the MRI-compatible videogame controller, during which we acquired BOLD recordings. The four remaining sessions were acquired in our MRI [simulator](https://pstnet.com/products/mri-simulator/), with a mock 64-channel head coil, and using a [commercially available SNES-like controller](https://lyonsden.net/innext-usb-game-controller-review/). The latter served as a reference for our validation study. Mock and MRI sessions were alternated, and the starting order (mock or MRI first) was counterbalanced across subjects. For the MRI sessions, the behavioural data can be found in the `*_events.tsv` files stored in the `func` folder. For the mock sessions, behavioural data can be found in the `beh` folder.
