#coding=utf-8
import string

def conclusion(buyerList, day):
    with open(unicode('analyse/汇总表-'+day+'.txt', 'utf-8'), 'w') as outFile:
        for i in buyerList:
            with open(unicode('analyse/总持仓-'+i+'.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    print >>outFile, j[:-1]

    newRecord = []
    with open(unicode('in/证券营业部.txt', 'utf-8'), 'a') as outFile:
        with open(unicode('out/' + day + '-券商.txt', 'utf-8'), 'r') as inFile:
            for i in inFile:
                record = i.split()
                if ((abs(string.atof(record[5]))>=0.5) and (record[2] not in buyerList) and (record[2] not in newRecord)):
                    print >>outFile, record[2]
                    newRecord.append(record[2])
        with open(unicode('out/' + day + '-券商三日.txt', 'utf-8'), 'r') as inFile:
            for i in inFile:
                record = i.split()
                if ((abs(string.atof(record[5]))>=0.5) and (record[2] not in buyerList) and (record[2] not in newRecord)):
                    print >>outFile, record[2]
                    newRecord.append(record[2])

    print ''
    if len(newRecord)>0:
        print 'I have added %d new agencies into the original list!' % (len(newRecord))
    else:
        print 'Today you don\'t need to refresh the list.'
