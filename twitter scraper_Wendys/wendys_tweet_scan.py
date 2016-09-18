import urllib
from bs4 import BeautifulSoup
from xlwt import Workbook
import re
import twitter

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

print 'This is a Python program to find out positive and negative tweets about Wendys'
twitter_api = oauth_login()


keyword = raw_input('Enter keyword you want to search:')
# connecting to link
raw_url = 'https://twitter.com/' + keyword

html = urllib.urlopen(raw_url)

book = Workbook()
sheet1 = book.add_sheet("Sheet 1")

# collecting all the html
soup = BeautifulSoup(html)
tags = list()
i = 0
g_count = 0
b_count = 0
# scaning to look for tweet p tags. all p tags info collected in list 'tags'
tags = soup('p')
sheet1.write(i, 0, 'Tags')
sheet1.write(i, 1, 'Good Reviews Count')
sheet1.write(i, 2, 'Bad Reviews Count')
print len(tags)

    
for tag in tags:
    print i
    try:
        a = re.findall('good|excellent|tasty|fresh|bright|brighten|perfect|subtly', str(tags[i-1].contents[0]))
        if len(a) >0: 
            print 'Good tag: ', tags[i-1].contents[0]
            g_count = g_count + 1
            sheet1.write(g_count, 0, tags[i-1].contents[0])
            
        
        b = re.findall('sorry|bad|tasteless|unhappy|slow|worry|try|ruin|rude|shame|disappointed', str(tags[i-1].contents[0]))
        print 'b scanned', b
        if len(b) >0: 
            print 'Bad tag: ', tags[i-1].contents[0]
            b_count = b_count + 1
            sheet1.write(b_count, 0, tags[i-1].contents[0])
        i = i + 1
    except (UnicodeEncodeError, IndexError):
            i = i + 1
            continue

sheet1.write(1, 1, g_count)
sheet1.write(1, 2, b_count)
book.save('.\wendy_rev.xls')
