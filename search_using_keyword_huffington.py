import urllib
from bs4 import BeautifulSoup
import re

# connecting to link
html = urllib.urlopen(' http://www.huffingtonpost.com/ ')
kw = raw_input('Enter search keyword: ')
keyw = '.'+ kw+ '.'
print keyw

# collecting all the html
soup = BeautifulSoup(html)

# scaning to look for anchor tags. all anchor tags info collected in list 'tags'
tags = soup('a')

print tags[0].contents[0]
x = 1
# scanning through all the links on home page
for i in range(0, len(tags)):
    print i
    
    try:
        result = re.findall('',tags[i].contents[0])
        if not result is None:
            print 'Result ', x, ': ', tags[i].contents[0]
            x = x + 1
#        print 'Content: ', tags[i].contents[0]
    except:
        print "********* No content **********"
    
    # connecting to sublinks to get count of other anchor tags
#    temphref = tags[0].get('href', None)
#    tempHtml = urllib.urlopen(temphref)
#    tempSoup = BeautifulSoup(tempHtml)
#    temptags = tempSoup('a')
#    print "Length of temptags: ", len(temptags)
    

    #print href
#    tempSoup = BeautifulSoup(tempHtml)
#    tags = tempSoup('a')
#    print map(str, tags[0])
#    print tags[0].contents[0]
#    print tags[0].get('href', None)
    
print "Length of tags: ", len(tags)
    
