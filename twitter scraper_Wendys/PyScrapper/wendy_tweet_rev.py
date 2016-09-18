import twitter
import json
from urllib import unquote

#---------------------------------------------
# Function to authenticate using Twitter API
def oauth_login():
    
    CONSUMER_KEY = 'SKeR7JceYHh6V7MA9aQg2LIs9'
    CONSUMER_SECRET ='YkMQ6GY1EuOVwxfHnc1lc8wr6OzoIveYiKgdbBwqtPyillJj41'
    OAUTH_TOKEN = '289922127-yer28rcHdG14s6REh9z2LZ53ibBgLnsy6djB0Ff8'
    OAUTH_TOKEN_SECRET = '	B7eGgOfnxE7nGRK25BPanc6rj9AoToR6ENb3bdsKYkFx9'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#----------------------------------------------
# Main body of the program

#print 'Welcome! The program has started.'
#print 'This is a Python program to fetch approximately 10,000 recent tweets about the US Open Final (2015)'
twitter_api = oauth_login()
json_statuses_file = open('json_statuses_file.txt', 'w')         # File to store JSON data
execution_output_file = open('execution_output_file.txt', 'w')   # File to store some debugging print statements
query = "#UsOpenFinal" # The query string
recent = "recent"      # The type of result we want, this will give only recent tweets
tweet_count = "100"    # Search API limits maximum number of tweets returned to 100

# Use the Twitter Search API to get the results. The query is used to get 100 recent tweets with the word "#UsOpenFinal".
us_open_final = twitter_api.search.tweets(q=query, count=tweet_count, include_entities=1, result_type=recent)
twitter_statuses = us_open_final['statuses']
tweet_ids = []
no_of_statuses = len(twitter_statuses)
