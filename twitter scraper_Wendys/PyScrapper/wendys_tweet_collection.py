# This is a Python program to find out negative and positive tweets about Wendys

import twitter
import json
from urllib import unquote

#---------------------------------------------
# Function to authenticate using Twitter API.  The keys used are critical to one user and are not #meant to be shared. Later, while scraping twitter for CL Kings, I might need company specific #twitter account to create such an app.
def oauth_login():
    CONSUMER_KEY = 'SKeR7JceYHh6V7MA9aQg2LIs9'
    CONSUMER_SECRET ='YkMQ6GY1EuOVwxfHnc1lc8wr6OzoIveYiKgdbBwqtPyillJj41'
    OAUTH_TOKEN = '289922127-yer28rcHdG14s6REh9z2LZ53ibBgLnsy6djB0Ff8'
    OAUTH_TOKEN_SECRET = 'B7eGgOfnxE7nGRK25BPanc6rj9AoToR6ENb3bdsKYkFx9'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api
 

#----------------------------------------------
# Main body of the program

print 'This is a Python program to find out positive and negative tweets about Wendys'
twitter_api = oauth_login()
# File to store JSON data. File will be later used to parse JSON to find positive and negative #reviews
json_statuses_file = open('json_statuses_file.txt', 'w')
query = "@wendys" # The query string
recent = "recent"      # The type of result we want, this will give only recent tweets
tweet_count = "100"    # Search API limits maximum number of tweets returned to 100

# Use the Twitter Search API to get the results. The query is used to get 100 recent tweets with the word "@Wendys".
wendys_tweets = twitter_api.search.tweets(q=query, count=tweet_count, include_entities=1, result_type=recent)
twitter_statuses = wendys_tweets['statuses']

# Iterate to generate 99 queries. In each query we try to get 100 tweets. But API might return less than 100 tweets sometimes.
for page_counter in range(0, 99): 
    
    try: # Find the smallest Twitter ID in the set of statuses returned for each query
        no_of_statuses = len(wendys_tweets['statuses'])
        for status_counter in range(0, no_of_statuses):
            tweet_ids.append(wendys_tweets['statuses'][status_counter]['id']) 
        min_tweet_id = min(tweet_ids)
        
    except: # Exception handling
        print "Exception encountered. Exiting for-loop."
        break;          # Exit the iteration
    
    # Returns results with an ID less than (that is, older than) or equal to the specified ID.
    wendys_tweets = twitter_api.search.tweets(q=query, count=tweet_count, include_entities=1, result_type=recent, max_id=min_tweet_id)
    twitter_statuses = twitter_statuses + wendys_tweets['statuses']
    no_of_statuses = len(wendys_tweets['statuses'])
    
print 'Total no.of statuses gathered - ', len(twitter_statuses)    
print 'Printing statuses to file....' 
json_statuses_file.write(json.dumps(twitter_statuses, indent=1))

json_statuses_file.close()
print 'Printing to file complete.'
print 'The program has completed.'
