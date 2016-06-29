import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter URL:')

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?' + urllib.urlencode({'sensor':'false', 'address': s_url})

url = urllib.urlopen(serviceurl)
data = url.read()
print "Length of data is", len(data)
tr = ET.fromstring(data)
#print data
cnt = tr.findall('comments/comment')
print 'count:', len(cnt)
numlist = list()
#print cnt

for item in cnt:
    num = item.find('count').text
    n = int(num)
    numlist.append(n)
    
print sum(numlist)