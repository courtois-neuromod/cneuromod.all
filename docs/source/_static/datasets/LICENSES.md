# Image licensing / provenance notes

Every dataset gallery tile is third-party cover art reproduced here to illustrate the
stimulus material used in the corresponding experiment, not project-owned artwork. This
file tracks, per image, where it came from and under what basis it's being reused, so the
reasoning doesn't need to be reconstructed later.

Entries for the images retrieved on 2026-09-02 from the legacy cneuromod.ca gallery
(`floc.jpg`, `hcptrt.png`, `movie10.jpg`, `retinotopy.jpg`, `things.jpg`) are not yet
individually documented here — see `README.md` in this directory for their provenance
table. New images added from here on should get a full entry below.

## friends.jpg

- **Depicts:** Seven pairs of hands holding up pink foil balloon letters spelling
  "FRIENDS" against a light blue background, used as the gallery tile for the `friends`
  dataset (fMRI viewing of the *Friends* TV series). Replaces the earlier legacy tile (an
  unlicensed *Friends* season 1 DVD cover scan carried over from the old cneuromod.ca
  gallery).
- **Author:** rawpixel.com, via Magnific.com (Freepik Company, S.L.U.).
- **Source:** [Magnific.com, "hands showing friends balloons word"](https://www.magnific.com/free-photo/hands-showing-friends-balloons-word_18655090.htm),
  retrieved 2026-09-03. Original 7752×3072 JPG; downscaled to 600×238 for the gallery
  tile.
- **License:** Magnific/Freepik "Free for commercial use WITH ATTRIBUTION" license
  (license certificate on file). Permits web use and derivative works; requires
  attribution "designed by rawpixel.com - Magnific.com", credited below.

  <a href="https://www.magnific.com">designed by rawpixel.com - Magnific.com</a>

## petit-prince.jpg

- **Depicts:** Photograph of a physical copy of *Le Petit Prince* (Antoine de
  Saint-Exupéry), the audiobook used as the stimulus for the `petit-prince` dataset.
- **Author:** Fayza Blz.
- **Source:** [Wikimedia Commons, `File:Livre petit prince.jpg`](https://commons.wikimedia.org/wiki/File:Livre_petit_prince.jpg)
  (also embedded on the [French Wikipedia article](https://fr.wikipedia.org/wiki/Le_Petit_Prince#/media/Fichier:Livre_petit_prince.jpg)),
  retrieved 2026-09-03. Original 2988×5312; cropped to the book cover (removing the
  surrounding table background) and downscaled to 600×953 for the gallery tile.
- **License:** CC BY-SA 4.0 (own work, uploaded by the photographer). Free to share and
  adapt with attribution; derivatives must carry the same or a compatible license.
  Attribution: photograph © Fayza Blz, CC BY-SA 4.0.
- **Note:** this replaces an earlier candidate (an English Wikipedia fair-use-only book
  cover scan) that was swapped out in favour of this freely-licensed photo.

## emotion-videos.jpg

- **Depicts:** A grid of colourful cartoon emoticon faces spanning a range of moods
  (happy, sad, angry, surprised, in love, etc.), illustrating the emotion categories
  targeted by the `emotion-videos` dataset's stimulus set.
- **Author:** pch.vector, via Magnific.com (Freepik Company, S.L.U.).
- **Source:** [Magnific.com, "Emoticons with different mood and emotions set"](https://www.magnific.com/free-vector/emoticons-with-different-mood-emotions-set-vector-illustrations-cute-characters-avatars-cartoon-color-collection-abstract-faces-with-eyes-mouth-smiley-caricature-concept_24644325.htm),
  retrieved 2026-09-03. Downscaled 8000×4800 → 600×360 for the gallery tile.
- **License:** Magnific/Freepik "Free for commercial use WITH ATTRIBUTION" license
  (license certificate on file). Permits web use and derivative works; requires
  attribution "designed by pch.vector - Magnific.com", credited below.

  <a href="https://www.magnific.com">designed by pch.vector - Magnific.com</a>

- **Note:** this replaces an earlier candidate (a Cowen & Keltner 2017 PNAS figure,
  Fig. 2, which turned out to be standard-copyright — freely readable but not
  openly licensed — and additionally embedded third-party photos not licensed to this
  project).

## mario.png

- **Depicts:** A pixel-art red amanita-muscaria mushroom (a `Super Mario`-style power-up
  icon), used as the gallery tile for the `mario` game-play dataset.
- **Author:** Vecteezy contributor (stock asset "Red mushroom fungi amanita muscaria
  pixel bit retro game").
- **Source:** [Vecteezy, "Red mushroom fungi amanita muscaria pixel bit retro game"](https://www.vecteezy.com/),
  downloaded under the Vecteezy Free License (license certificate on file,
  `Vecteezy-License-Information.pdf`), retrieved 2026-09-03. Original 1920×1920 JPG;
  trimmed to content and downscaled to 600×600 for the gallery tile. The white background
  was subsequently keyed out to transparent (flood-fill from the image border on
  near-white pixels, with the anti-aliased fringe alpha-blended) and the file re-saved
  as PNG on 2026-09-03, so the tile reads cleanly against both light and dark doc themes.
- **License:** Vecteezy Free License. Permits use in digital projects, including
  modification/derivative works, with attribution to Vecteezy.com. Attribution:
  mushroom icon via Vecteezy.com.

## harrypotter.jpg

- **Depicts:** An illustrated young witch in a wide-brimmed purple hat, holding an open
  spellbook, used as the gallery tile for the `harrypotter` dataset (fMRI viewing of
  *Harry Potter and the Philosopher's Stone*). Replaces the earlier legacy tile (an
  unlicensed film cover scan carried over from the old cneuromod.ca gallery).
- **Author:** Freepik, via Magnific.com (Freepik Company, S.L.U.). AI-generated image
  ("free-ai-image").
- **Source:** [Magnific.com, "enchanting witch with spellbook"](https://www.magnific.com/free-ai-image/enchanting-witch-with-spellbook_420644498.htm),
  retrieved 2026-09-03. Original 4000×5846 PNG; downscaled to 600×877 for the gallery tile.
- **License:** Magnific/Freepik "Free for commercial use WITH ATTRIBUTION" license
  (license certificate on file). Permits web use and derivative works; requires
  attribution "designed by Freepik - Magnific.com", credited below.

  <a href="https://www.magnific.com">designed by Freepik - Magnific.com</a>

## mariostars.png

- **Depicts:** The same [`mario.png`](#img-mariopng) mushroom artwork (transparent
  background) with a yellow five-point star badge (drawn programmatically, solid fill
  with a dark outline) composited in the upper-right corner, to visually distinguish
  the `mariostars` dataset's gallery tile from `mario`/`mario3`/`mario_eeg`.
- **Author / source / license:** derivative of `mario.png` — see that entry above for
  the base artwork's provenance and license. The star badge itself is an original
  vector shape with no external source.
- **Attribution:** mushroom icon via Vecteezy.com.

## mario3.png

- **Depicts:** The same [`mario.png`](#img-mariopng) mushroom artwork (transparent
  background) with a yellow circular badge containing a bold white "3" (drawn
  programmatically) composited in the upper-right corner, to visually distinguish the
  `mario3` dataset's gallery tile from `mario`/`mariostars`/`mario_eeg`.
- **Author / source / license:** derivative of `mario.png` — see that entry above for
  the base artwork's provenance and license. The badge itself is an original shape
  with no external source.
- **Attribution:** mushroom icon via Vecteezy.com.

## shinobi.png

- **Depicts:** A stylised colourful ninja mascot logo (armoured ninja head crossed by two
  katanas in front of a shuriken-star badge, "SHINOBI" banner beneath), used as the
  gallery tile for the `shinobi` game-play dataset. Replaces the earlier legacy tile (an
  unlicensed *Shinobi III: Return of the Ninja Master* Sega Mega Drive box art scan
  carried over from the old cneuromod.ca gallery).
- **Author:** pikisuperstar, via Magnific.com (Freepik Company, S.L.U.).
- **Source:** [Magnific.com, "detailed colorful ninja logo"](https://www.magnific.com/free-vector/detailed-colorful-ninja-logo_15266641.htm),
  retrieved 2026-09-03. Original 2000×2000 transparent PNG; trimmed to content (1538×1538)
  and downscaled to 600×600 for the gallery tile.
- **License:** Magnific/Freepik "Free for commercial use WITH ATTRIBUTION" license
  (license certificate on file). Permits web use and derivative works; requires
  attribution "designed by pikisuperstar - Magnific.com", credited below.

  <a href="https://www.magnific.com">designed by pikisuperstar - Magnific.com</a>

## ood.jpg

- **Depicts:** A publicity still of Charlie Chaplin in his "Tramp" costume (bowler hat,
  cane), from the 1915 Essanay Studios film *The Tramp*, used as the gallery tile for the
  `ood` dataset (out-of-distribution audiovisual stimuli held out to test generalization
  of brain encoding models).
- **Author:** P.D Jankens.
- **Source:** [Wikimedia Commons / Wikipedia, `File:Charlie_Chaplin.jpg`](https://en.wikipedia.org/wiki/File:Charlie_Chaplin.jpg),
  uploaded by Fred Chess, retrieved 2026-09-03. Original 1280×1600 (JPEG); downscaled to
  600×743 for the gallery tile.
- **License:** Public domain in the United States (published before January 1, 1931;
  `PD-US-expired`/`PD-1923`). No attribution required.

## anat.jpg

- **Depicts:** A montage of anatomical and quantitative MRI acquisitions (T1w, T2w,
  MP2RAGE, ME-GRE, magnetization transfer, diffusion-weighted imaging) with labels for
  the morphometry/demyelination/axon-degeneration measures each protocol targets, used as
  the gallery tile for the `anat` dataset.
- **Author:** Mathieu Boudreau, Agah Karakuzu, Arnaud Boré, Basile Pinsard, Kiril
  Zelenkovski, Eva Alonso-Ortiz, Julie Boyle, Lune Bellec, Julien Cohen-Adad — the authors
  of the dataset's preferred-citation paper (see `anat/CITATION.cff`), "Longitudinal
  reproducibility of brain and spinal cord quantitative MRI biomarkers", Imaging
  Neuroscience, 2025.
- **Source:** Figure from the above paper, carried over unchanged from the legacy
  cneuromod.ca gallery (retrieved 2026-09-02; see `README.md` in this directory).
- **License:** CC-BY 4.0, per the authors of the paper.

## mario_eeg.png

- **Depicts:** The same [`mario.png`](#img-mariopng) mushroom artwork (transparent
  background) with a white circular badge, dark outline, containing a yellow jagged
  waveform evoking an EEG trace (drawn programmatically) composited in the upper-right
  corner, used as the gallery tile for the `mario_eeg` dataset.
- **Author / source / license:** derivative of `mario.png` — see that entry above for
  the base artwork's provenance and license. The badge and waveform are original
  shapes with no external source.
- **Attribution:** mushroom icon via Vecteezy.com.

## narratives.jpg

- **Depicts:** Title-page illustration for *The Orphant Annie Book* (James Whitcomb
  Riley, 1908) showing a group of children gathered around a woman telling them a story,
  used as the gallery tile for the `narratives` dataset (fMRI listening to spoken
  narratives).
- **Author:** Ethel Franklin Betts (1877–1959).
- **Source:** [Wikimedia Commons, `File:Orphant Annie Book – Title page.jpg`](https://commons.wikimedia.org/wiki/File:Orphant_Annie_Book_%E2%80%93_Title_page.jpg),
  from *The Orphant Annie Book*, Bobbs-Merrill Co., Indianapolis, 1908 (via Internet
  Archive), retrieved 2026-09-03. Original 1776×1121; downscaled to 600×379 for the
  gallery tile.
- **License:** Public domain in the United States (published before January 1, 1931;
  `PD-US-expired`/`PD-1923`). No attribution required.
