#coding=utf-8
import time
from dateSort import sort
from cleaning import cleanData
from analysis import analyse
from synthesis import conclusion

start = time.clock()

date = ['2017-4-7','2017-4-10','2017-4-11','2017-4-12','2017-4-13',
        '2017-4-14','2017-4-17','2017-4-18','2017-4-19','2017-4-20',
        '2017-4-21','2017-4-24','2017-4-25','2017-4-26','2017-4-27',
        '2017-4-28','2017-5-2','2017-5-3','2017-5-4','2017-5-5',
        '2017-5-8','2017-5-9','2017-5-10','2017-5-11','2017-5-12',
        '2017-5-15','2017-5-16','2017-5-17','2017-5-18','2017-5-19']

# Add new members here
who = []

for i in date:
    cleanData(i)

sortedDate = sort(date)

for i in who:
    analyse(i, sortedDate)

conclusion(who)

end = time.clock()
print '......analysis took %fs, successfully done :)' % (end-start)
