import urllib
from bs4 import BeautifulSoup
from xlwt import Workbook
import re

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
            
        
        b = re.findall('sorry|bad|tasteless|unhappy|slow|worry|try', str(tags[i-1].contents[0]))
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
book.save('C:\Users\\viraj\Documents\Study\python\\twitter scraper_Wendys\wendy_rev.xls')

#raw_url_2 = 'https://twitter.com/' + keyword + 'with_replies'
#html_2 = urllib.urlopen(raw_url)
#soup_2 = BeautifulSoup(html)
#tags_2 = list()
#j = 0
## scaning to look for tweet tags. all anchor tags info collected in list 'tags'
#tags_2 = soup('p')
#print len(tags_2)
#
#for tag in tags:
#    try:
#        print tags_2[j].contents[0]
#        a_2 = re.findall('good|excellent|tasty|fresh', str(tags_2[i-1].contents[0]))
#        if len(a_2) >0: 
#            print 'Good tag: ', tags_2[i-1].contents[0]
#        
#        b_2 = re.findall('bad|sorry|tasteless|unhappy|slow', str(tags_2[i-1].contents[0]))
#        if len(b_2) >0: 
#            print 'Bad tag: ', tags_2[i-1].contents[0]
#        j = j + 1
#    except (UnicodeEncodeError, IndexError):
#        j = j + 1
#        continue
#
#    