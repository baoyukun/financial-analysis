#coding=utf-8

def conclusion(buyerList):

    with open(unicode('analyse/0汇总表.txt', 'utf-8'), 'w') as outFile:
        i = 'Reset the file!'

    with open(unicode('analyse/0汇总表.txt', 'utf-8'), 'a') as outFile:
        for i in buyerList:
            with open(unicode('analyse/总持仓-'+i+'.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    print >>outFile, j[:-1]
