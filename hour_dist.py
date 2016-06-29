'''10.2 Write a program to read through the mbox-short.txt and 
figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and 
then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

C:\Users\viraj\Documents\Study\python\Coursera\week 7\ms.txt
'''

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
data = handle.readlines()

for line in data:
    pc = line.split()
    for p in pc:
        t = re.findall('[0-9]*\S',p)
        if t <>[]: print 't is:', t
#    a = re.findall('^From *.([0-9].:)\S',line)
#    if a <> []: print a