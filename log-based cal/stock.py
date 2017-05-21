#coding=utf-8
import time
from dateSort import sort
from cleaning import cleanData
from analysis import analyse
from synthesis import conclusion

start = time.clock()

date = ['2017-5-19', '2017-5-17', '2017-5-18', '2017-5-16']

who = []
with open(unicode('in/证券营业部.txt', 'utf-8'), 'r') as inFile:
    for i in inFile:
        who.append(i[:-1])

sortedDate = sort(date)

cleanData(sortedDate[-1])

for i in who:
    analyse(i, sortedDate)

conclusion(who, sortedDate[-1])

end = time.clock()
print '......analysis took %fs, successfully done :)' % (end-start)
