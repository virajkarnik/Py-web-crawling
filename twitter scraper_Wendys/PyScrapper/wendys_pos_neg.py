from xlwt import Workbook
import json
import re
from collections import Counter
import matplotlib.pyplot as plt


print 'This is a Python program to perform a sentiment anlaysis on the tweets from Wendys'
json_statuses_file = open('json_statuses_file.txt', 'r')
json_statuses = json.load(json_statuses_file)
json_statuses_file.close()

#creating instance of excel sheet
i = 0
book = Workbook()
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, 'Good Reviews Count')
sheet1.write(0, 1, 'Bad Reviews Count')

status_texts = [ status['text'] 
                 for status in json_statuses ]

# Get a collection of all space delimited words from all tweets
statuses = [ w 
         for t in status_texts 
           for w in t.split(',') ]

# List of positive words for Wendys
positive_words = ['tasty','fresh','wonderful','good','fast','happy','thank','nice','great','fantastic','like']

negative_words = ['bad','slow','dull','angry','anti','expensive','tasteless']

n=len(statuses)

positive=0
negative=0
notDetermined=0

for status in statuses:
    status = status.lower()
    isPositive=False
    # Iterating to find positive words
    for positive_word in positive_words:
        if isPositive is False:
            if positive_word in status and ('wendys' in status):
                isPositive=True
                break                           
    if isPositive is True:
        positive+= 1
        
    
    if isPositive is False:    
        isNegative=False
        # Iterating to find negative words 
        for negative_word in negative_words:
            if isNegative is False:
                if negative_word in status and ('wendys' in status):
                    isNegative=True
                    break                           
        if isNegative is True:
            negative+= 1
            
    if isNegative is False and isPositive is False:
        notDetermined+= 1
         
supportive_tweets=[positive,negative]


sheet1.write(1, 0, positive)
sheet1.write(1, 1, negative)
print ('Positive reviews - ' + repr(positive))
    
print ('Negative reviews - ' + repr(negative))

book.save('.\wendy_rev.xls')
