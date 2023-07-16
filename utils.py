import re
from string import punctuation

def remove_special_characters(tweet):
    # Regular expression pattern to match special characters
    special_char_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    
    # Remove special characters from the text
    tweet = special_char_pattern.sub('', tweet)
    
    return tweet

def clean_tweets(tweet):
    # remove username
    while tweet.find('@') > -1:
        username_idx = tweet.find('@')
        if username_idx != -1:
            username_end_idx = tweet.find(':', username_idx)
            username = tweet[username_idx: username_end_idx]
            tweet = tweet.replace(username, '')
        else:
            print('>>', username_idx)
    tweet = tweet.replace('RT : ', '').replace('RT','').strip()
    # punctuations cleaning
    for p in punctuation:
        tweet = tweet.replace(p,'')
    tweet = tweet.replace('\n', '')
    # remove emojies
    
    return tweet