#coding=utf-8
import csv
import string

def conclusion(buyerList, day):
    with open(unicode('analyse/汇总表-'+day+'.csv', 'utf-8'), 'wb') as outFiler:
        outFile = csv.writer(outFiler, dialect='excel')
        for i in buyerList:
            with open(unicode('analyse/总持仓-'+i+'.csv', 'utf-8'), 'rb') as inFiler:
                inFile = csv.reader(inFiler, dialect='excel')
                for j in inFile:
                    outFile.writerow(j)

    newRecord = []
    with open(unicode('in/证券营业部.csv', 'utf-8'), 'ab') as outFiler:
        outFile = csv.writer(outFiler, dialect='excel')
        with open(unicode('out/' + day + '-券商.csv', 'utf-8'), 'rb') as inFiler:
            inFile = csv.reader(inFiler, dialect='excel')
            for record in inFile:
                if ((abs(string.atof(record[5]))>=0.5) and (record[2] not in buyerList) and (record[2] not in newRecord)):
                    outFile.writerow([record[2]])
                    newRecord.append(record[2])
        with open(unicode('out/' + day + '-券商三日.csv', 'utf-8'), 'rb') as inFiler:
            inFile = csv.reader(inFiler, dialect='excel')
            for record in inFile:
                if ((abs(string.atof(record[5]))>=0.5) and (record[2] not in buyerList) and (record[2] not in newRecord)):
                    outFile.writerow([record[2]])
                    newRecord.append(record[2])

    print ''
    if len(newRecord)>0:
        print 'I have added %d new agencies into the original list!' % (len(newRecord))
    else:
        print 'Today you don\'t need to refresh the list.'
