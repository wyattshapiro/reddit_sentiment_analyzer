# Reddit Analyzer

Analyzes comments from given subreddits on reddit.com scraped with https://github.com/wyattshapiro/reddit_scraper


## License
Copyright (c) Wyatt Shapiro 2018

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Installation

Clone the repo onto your machine with the following command:

$ git checkout https://github.com/wyattshapiro/reddit_sentiment_analyzer


## Dependencies

We use Python 2.7.

See https://www.python.org/downloads/ for more information.

----

We use virtualenv to manage dependencies, if you have it installed you can run
the following commands from the root code directory to create the environment and
activate it:

$ virtualenv venv  
$ source venv/bin/activate

See https://virtualenv.pypa.io/en/stable/ for more information.

----

We use pip to install dependencies, which comes installed in a virtualenv.
You can run the following to install dependencies:

$ pip install -r requirements.txt

See https://pip.pypa.io/en/stable/installing/ for more information.

----

We use a config file to set constants. Create a config.py file in src/ that matches the config.py.sample file.

See config.py.sample for more information.

----

We use NLTK for a lexicon. You must uncomment the following line for first install:

nltk.download('vader_lexicon')


## Config

- BASE_DIR
- INPUT_PATH
- OUTPUT_PATH
- INPUT_PATH_POS
- INPUT_PATH_NEG

## Input

File with following fields, ordered in this way:

- subreddit_name
- subreddit_id
- submission_title
- parent_comment_id
- comment_link
- created_utc
- body
- author
- score
- ups
- downs
- saved
- gilded


## Known Bugs

1. Sentiment does not account for a scenario where the post was negative and the comment was positive because it affirmed the negative sentiment
2. Need the exact order of inputs and all the fields for script to work


## Credits

I found the sentiment analysis writing to .txt code from a github repo that I now cannot find :(
