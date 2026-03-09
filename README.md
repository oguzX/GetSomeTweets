# GetSomeTweets

A Python tool that fetches tweets via the Twitter API, cleans them, and performs Named Entity Recognition (NER) tagging on Turkish-language tweet content.

## Overview

This project searches for tweets about a specific topic (defaulting to "edirne"), cleans the raw text, and identifies named entities such as persons, organizations, locations, dates, and genders using a rule-based dictionary approach.

## Features

- Fetches up to 2500 tweets using the Tweepy library
- Cleans tweet text by removing hashtags, retweet markers, emojis, links, and punctuation
- Deduplicates tweets
- Performs rule-based NER tagging with BIO (Beginning-Inside-Outside) notation
- Saves tagged results to a timestamped `.txt` file in a `tweets/` directory

## Entity Types

| Tag          | Description                          |
|--------------|--------------------------------------|
| `Person`     | People's names (detected via dictionary or title rules like `Sn.`, `Dr.`, `Şehit`) |
| `Organization` | Companies, political parties, institutions |
| `Location`   | Cities, landmarks, countries, roads  |
| `Date`       | Month and day names (Turkish)        |
| `Gender`     | Gender-related words (`kadın`, `erkek`) |

## Project Structure

```
GetSomeTweets/
├── main.py          # Entry point: fetches, cleans, and processes tweets
├── tag.py           # NER logic: dictionary lookup and rule-based matching
├── dictionary.py    # Named entity dictionary (persons, orgs, locations, etc.)
├── wordNode.py      # Tree node structure for word relationships
├── classes/
│   └── Isim.py      # Entity class representing a found named entity
└── tweets/          # Output directory for tagged tweet files (timestamped)
```

## Setup

### Prerequisites

- Python 3.x
- A Twitter Developer account with API credentials

### Install dependencies

```bash
pip install tweepy snowballstemmer TurkishStemmer
```

### Configure Twitter API keys

Create a `twitterKeys.py` file in the project root:

```python
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

### Create output directory

```bash
mkdir tweets
```

## Usage

```bash
python main.py
```

The script will:
1. Search Twitter for tweets matching the configured query (default: `edirne`)
2. Clean and deduplicate the tweet text
3. Tag named entities using BIO notation
4. Save results to `tweets/<timestamp>.txt`

## Output Format

Each tweet is followed by its tagged entities in BIO notation:

```
Tweet text here
{B-Person}Ali
{B-Location}Edirne
--------------------------------------
```

## Notes

- The dictionary in `dictionary.py` is focused on Turkish content related to the Edirne/Trakya region.
- Rule-based detection supports title keywords like `Sn.`, `Dr.`, `Sayın`, `Şehit`, `Gazi`, `Müdürü` to identify person names from surrounding words.
- `twitterKeys.py` should be kept out of version control (add it to `.gitignore`).
