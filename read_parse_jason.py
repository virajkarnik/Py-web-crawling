import json
import urllib

url = raw_input('Enter URL:')
opn = urllib.urlopen(url)
data = opn.read()
print data

try:
    js = json.loads(data)
except:
    js = None

count = list()
i = 0

for item in js['comments']:
    c = js["comments"][i]["count"]
    i = i+1
    cnt = int(c)
    count.append(cnt)
    print cnt

print "Sum:", sum(count)