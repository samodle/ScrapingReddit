# ScrapingReddit

This repository contains two scripts.  The first leverages PRAW to scrape reddit.  The second parses the 59GB Reddit scrape from Princeton.

## PRAW

Using PRAW to Crawl Reddit w/ Python.  Requires config file formatted like this:
````
APP_CLIENT_ID = ''
APP_CLIENT_SECRET = ''
APP_NAME = ''
REDDIT_USERNAME = ''
REDDIT_PW = ''

SubReddits = ['funny', 'askreddit', 'worldnews', 'today', 'news', 'todayilearned', 'showerthoughts', 'jokes']
NumberOfSubs = 4
````

## Princeton Data

Takes the 59GB csv files, reades through it iteratively and exports the relevant portions as a csv.

## Sources
##### Credit to these two tutorials (main.py):

> https://towardsdatascience.com/scraping-reddit-data-1c0af3040768

> https://www.storybench.org/how-to-scrape-reddit-with-python/

##### Princeton Dataset:

> https://nlp.cs.princeton.edu/SARC/0.0/raw/
