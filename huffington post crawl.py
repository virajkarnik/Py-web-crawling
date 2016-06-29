import urllib
from bs4 import BeautifulSoup

# connecting to link
html = urllib.urlopen(' http://www.huffingtonpost.com/ ')

# collecting all the html
soup = BeautifulSoup(html)

# scaning to look for anchor tags. all anchor tags info collected in list 'tags'
tags = soup('a')

print tags[0].contents[0]

# scanning through all the links on home page
for i in range(0, len(tags)):
    print i
    try:
        print tags[i].contents[0]
    except:
        print "********* No content **********"
    
    # connecting to sublinks to get count of other anchor tags
    temphref = tags[0].get('href', None)
    tempHtml = urllib.urlopen(temphref)
    tempSoup = BeautifulSoup(tempHtml)
    temptags = tempSoup('a')
    print "Length of temptags: ", len(temptags)
    

    #print href
#    tempSoup = BeautifulSoup(tempHtml)
#    tags = tempSoup('a')
#    print map(str, tags[0])
#    print tags[0].contents[0]
#    print tags[0].get('href', None)
    
print "Length of tags: ", len(tags)
    
 