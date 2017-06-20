#coding=utf-8
import time
import csv
from dateSort import sort
from cleaning import cleanData
from analysis import analyse
from synthesis import conclusion

start = time.clock()

date = ['2017-6-8', '2017-6-6', '2017-6-7', '2017-6-9']

who = []
with open(unicode('in/证券营业部.csv', 'utf-8'), 'rb') as csvfile:
    spamreader = csv.reader(csvfile, dialect='excel')
    for row in spamreader:
        who.append(row[0])

sortedDate = sort(date)

cleanData(sortedDate[-1])

for i in who:
    analyse(i, sortedDate)

conclusion(who, sortedDate[-1])

end = time.clock()
print '......analysis took %fs, successfully done :)' % (end-start)
