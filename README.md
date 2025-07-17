# Bayesian-Modeling

## Overview

**Bayesian-Modeling** is a text classification project that identifies the authorship or source category of unknown texts using Bayesian-style probabilistic models. This project specifically explores whether stylistic features in text—such as sentence structure, word length, and vocabulary—can successfully distinguish between poetic and lyrical writing, even when the texts share a common theme. For this project, four Christmas-themed texts were analyzed: two known (training) texts and two unknown ones, all spanning different genres and time periods.

## Project Files

- `model.py` / `textmodel.py`: Core class `TextModel` for building and comparing text models using various features such as word frequencies, sentence lengths, stems (via the Porter stemmer), and vowel counts.
- `porter.py`: An implementation of the Porter Stemming Algorithm used for extracting word stems.
- `train1.txt`: Lyrics to *All I Want for Christmas Is You* by Mariah Carey (1994).
- `train2.txt`: *A Visit from St. Nicholas* by Clement Clarke Moore (1823).
- `unknown1.txt`: Robert Frost's 1916 poem *Christmas Trees*.
- `unknown2.txt`: Jose Feliciano's 2014 song *Feliz Navidad*.
- `analysis.txt`: Summary of results from applying the model.
- `overview.txt`: Original project design proposal and motivation.

## Methodology

The model constructs five key feature dictionaries from each text:

1. **Words** – Frequency of each word.
2. **Word Lengths** – Distribution of word lengths.
3. **Stems** – Frequency of stems using the Porter Stemmer.
4. **Sentence Lengths** – Distribution of sentence lengths by word count.
5. **Number of Vowels** – Frequency of vowels (a, e, i, o, u).

Each unknown text is compared to both training texts using a log-probability scoring method across each feature. The model then sums the scores and selects the best match.

## Results

Despite all four texts sharing the Christmas theme and containing poetic or lyrical structure, the model successfully differentiated between songs and poems. The matches were as follows:

- `train1.txt` (Mariah Carey) matched with `unknown2.txt` (*Feliz Navidad*).
- `train2.txt` (Clement Clarke Moore) matched with `unknown1.txt` (*Christmas Trees* by Robert Frost).

These results validated the initial hypothesis that the model could distinguish between poetic and lyrical texts based on structure and word use, not just theme.

## How to Run

1. Ensure all text files and `porter.py` are in the same directory as `textmodel.py`.
2. Run the script using a Python interpreter:
   ```bash
   python3 textmodel.py
