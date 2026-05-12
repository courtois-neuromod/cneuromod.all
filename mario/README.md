# mario

## Overview
The mario dataset explores behavioural and brain correlates of videogame play and includes five participants (sub-01, sub-02, sub-03, sub-05 and sub-06; two females, three males) who played Super Mario Bros (SMB; Nintendo, 1985) inside an MRI scanner. The dataset comprises ~15h of fMRI data per subject. Among the participants, sub-01 and sub-06 had prior experience with SMB, and two participants (sub-01 and sub-02) reported regular videogame play. One participant (sub-03) reported no videogame experience, except for another retro platformer called Shinobi III: Return of the Ninja Master (RotNM; Sega, 1993) she practiced for 10+hours as part of a prior CNeuroMod experiment (shinobi dataset).

## Game environment
To play the game, participants used the CNeuromod videogame controller described in [Harel et al. (2023)](https://doi.org/10.1371/journal.pone.0290158). The game software was run on a console emulator using OpenAI’s gym-retro library (Nichol et al., 2018), a Python-based platform supporting emulators for over 10 retro consoles and thousands of games. Built on gym (Brockman et al., 2016), a library designed for reinforcement learning, gym-retro integrates console emulators via the Libretro API (Libretro, n.d.).
In this experiment, SMB was played and recorded at a 60Hz framerate. Because the game is fully deterministic, only player inputs (button presses) were recorded, enabling the reconstruction of exact replays of gameplay sequences.

## Task
SMB is a commercial platform side scroller game released in 1985 by the company Nintendo. The aim of the game is to go right and reach the end of each level, while avoiding a variety of obstacles and enemies. The platormers genre was selected by the CNeuroMod team because gym-retro was developed for a major reinforcement competition centered on this genre (OpenAI, 2018). This game was further selected for its compatibility with gym-retro and its commercial success, ensuring engaging gameplay but also extensive prior litterature investigating the design of the game (Dahslkog & Togelius, 2012; Thompson, 2023). As in other platformers, players navigate a linear two-dimensional environment filled with enemies and obstacles to reach a destination. The player may collect some power ups which change the form and behaviour of the character in the game.

## Levels
For this study, 22 levels were selected for their gameplay similarity. Specifically, all original levels of SMB were used with the exception of the water and boss levels, which feature very different game mechanics than the other.
Each attempt at completing a level began with no power up and three lives and is called a "repetition". The attempt was completed if the player reached the end of the level or lost all three lives trying. When players died, they resumed their attempt from the start of the level, or from a dedicated spawn point only featured in some levels and selected by the original game designers.

## Practice and discovery phases
The participants first repeated each level until they could succeed at least once, with all the levels presented in order (Discovery phase). Then, they played randomly selected levels for the remaining sessions.

| Subject   |   Repetitions (Discovery) |   Repetitions (Practice) | Duration (Discovery)   | Duration (Practice)   |   Success rate (Discovery) |   Success rate (Practice) |   Repetitions (Total) |   Success rate (Total) | Duration (Total)   |
|-----------|---------------------------|--------------------------|------------------------|-----------------------|----------------------------|---------------------------|-----------------------|------------------------|--------------------|
| 01        |                       230 |                      567 | 03:54:27               | 09:47:11              |                   0.578261 |                  0.781305 |                   797 |               0.72271  | 13:41:38           |
| 02        |                       227 |                      487 | 04:57:35               | 12:30:24              |                   0.400881 |                  0.671458 |                   714 |               0.585434 | 17:27:59           |
| 03        |                       176 |                      451 | 04:49:38               | 11:57:19              |                   0.431818 |                  0.698448 |                   627 |               0.623604 | 16:46:57           |
| 05        |                       177 |                      457 | 05:30:04               | 12:27:44              |                   0.367232 |                  0.582057 |                   634 |               0.522082 | 17:57:48           |
| 06        |                       134 |                      468 | 04:25:41               | 13:37:40              |                   0.626866 |                  0.856838 |                   602 |               0.805648 | 18:03:22           |
| Total     |                       944 |                     2430 | 23:37:27               | 60:20:19              |                   0.481011 |                  0.718021 |                  3374 |               0.651896 | 83:57:47           |
