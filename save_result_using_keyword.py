import urllib
from bs4 import BeautifulSoup
from xlwt import Workbook
import re

keyword = raw_input('Enter keyword you want to search:')
# connecting to link
raw_url = 'http://in.reuters.com/search/news?blob=' + keyword
print raw_url
html = urllib.urlopen(raw_url)

book = Workbook()
sheet1 = book.add_sheet("Sheet 1")

# collecting all the html
soup = BeautifulSoup(html)
tags = list()
# scaning to look for anchor tags. all anchor tags info collected in list 'tags'
tags = soup('h3')
print len(tags)
i = 0
sheet1.write(i, 0, 'Tags')
for line in tags:
    i = i + 1
    a = re.findall('>(.*\s)<', str(tags[i-1].contents[0]))
    if len(a) >0: 
        print a
        sheet1.write(i, 0, a)

book.save('C:\Users\\viraj\Documents\Study\python\Rugved work\\trial.xls')
