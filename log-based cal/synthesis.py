#coding=utf-8
import csv

def conclusion(buyerList, lastDate):
    with open(unicode('analyse/汇总表-'+ lastDate + '.csv', 'utf-8'), 'wb') as outFiler:
        outFile = csv.writer(outFiler, dialect='excel')
        for i in buyerList:
            with open(unicode('analyse/总持仓-'+i+'.csv', 'utf-8'), 'rb') as inFiler:
                inFile = csv.reader(inFiler, dialect='excel')
                for j in inFile:
                    outFile.writerow(j)
