# delete-all-tweets

Simple script to delete all tweets from a timeline using tweepy.

Needs a valid config.ini file (see config_sample.ini for an example)

## Requirements

- tweepy

## Installation of the virtualenv (recommended)

```
pipenv install
```

## Usage

```
python delete-all-tweets.py
```

## Help

```
python delete-all-tweets.py -h
```

```
usage: delete-all-tweets.py [-h] [--debug] [-c]

delete-all-tweets

optional arguments:
  -h, --help      show this help message and exit
  --debug         Display debugging information
  -c, --cold_run  Cold run (doesn't delete anything)
```
