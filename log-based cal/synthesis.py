#coding=utf-8

def conclusion(buyerList, day):
    with open(unicode('analyse/汇总表-'+day+'.txt', 'utf-8'), 'w') as outFile:
        for i in buyerList:
            with open(unicode('analyse/总持仓-'+i+'.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    print >>outFile, j[:-1]
