#coding=utf-8
import csv
import string

def numFormat(result):
    for i in range(3,6):
        result[i] = string.atof(result[i])
    if len(result)>6:
        for i in range(7,10):
            result[i] = string.atof(result[i])
    return result

def findTodayRecord(name, dateName, fileSuffix):
    x = []
    with open(unicode('out/'+ dateName + fileSuffix, 'utf-8'), 'rb') as inReader:
        inFile = csv.reader(inReader, dialect='excel')
        for i in inFile:
            if name == i[1]:
                numRecord = numFormat(i)
                if numRecord not in x:
                    x.append(numRecord)
    return x

def importLog(name, dateName):
    x = []
    xName = []
    y = []
    yName = []
    with open(unicode('analyse/汇总表-'+ dateName + '.csv', 'utf-8'), 'rb') as inReader:
        inFile = csv.reader(inReader, dialect='excel')
        for i in inFile:
            if name == i[1]:
                numRecord = numFormat(i)
                xName.append(numRecord[1])
                yName.append(numRecord[1])
                x.append([numRecord[j] for j in range(6)])
                y.append([numRecord[6], numRecord[8], numRecord[9], numRecord[7]])
    return [x, xName, y, yName]

def updateVar(x, xName, newRecord, oldRecord):
    if oldRecord==[]:
        i = ['+' if newRecord[5]>0 else '-', newRecord[3], newRecord[4], newRecord[5]]
    else:
        i = ['+' if newRecord[5]-oldRecord[5]>0 else '-', newRecord[3]-oldRecord[3], newRecord[4]-oldRecord[4], newRecord[5]-oldRecord[5]]

    if newRecord[1] in xName:
        x[xName.index(newRecord[1])] = i
    else:
        xName.append(newRecord[1])
        x.append(i)

    return [x, xName]

def analyse(buyer, dateList):
    a = findTodayRecord(buyer, dateList[-1], '-券商.csv')
    b = findTodayRecord(buyer, dateList[-1], '-券商三日.csv')
    [avantHier, avantHierName, cVar, cVarName] = importLog(buyer, dateList[0])
    [yier, yierName, cVar, cVarName] = importLog(buyer, dateList[2])
    [today, todayName] = [[], []]

    ai = 0
    alen = len(a)
    bi = 0
    blen = len(b)
    # Update the result of three days before
    while (bi<blen):
        record = b[bi]
        if record[1] in todayName:
            oldRecord = today[todayName.index(record[1])]
            [oldRecord[3], oldRecord[4], oldRecord[5]] = [oldRecord[3]+record[3], oldRecord[4]+record[4], oldRecord[5]+record[5]]
        else:
            if record[1] in avantHierName:
                oldRecord = avantHier[avantHierName.index(record[1])]
                [record[3], record[4], record[5]] = [record[3]+oldRecord[3], record[4]+oldRecord[4], record[5]+oldRecord[5]]
            todayName.append(record[1])
            today.append(record)
        bi += 1

    tdRecord = [i for i in todayName]

    # Update the variance
    for i in tdRecord:
        if i not in avantHierName:
            [cVar, cVarName] = updateVar(cVar, cVarName, today[todayName.index(i)], [])
        else:
            [cVar, cVarName] = updateVar(cVar, cVarName, today[todayName.index(i)], avantHier[avantHierName.index(i)])

    # Update the result of yesterday
    while (ai<alen):
        if (a[ai][1] not in tdRecord):
            record = a[ai]
            if record[1] in todayName:
                oldRecord = today[todayName.index(record[1])]
                [oldRecord[3], oldRecord[4], oldRecord[5]] = [oldRecord[3]+record[3], oldRecord[4]+record[4], oldRecord[5]+record[5]]
            else:
                if record[1] in yierName:
                    oldRecord = yier[yierName.index(record[1])]
                    [record[3], record[4], record[5]] = [record[3]+oldRecord[3], record[4]+oldRecord[4], record[5]+oldRecord[5]]
                todayName.append(record[1])
                today.append(record)
        ai += 1

    # Update the variance
    for i in todayName:
        if i not in tdRecord:
            if i not in yierName:
                [cVar, cVarName] = updateVar(cVar, cVarName, today[todayName.index(i)], [])
            else:
                [cVar, cVarName] = updateVar(cVar, cVarName, today[todayName.index(i)], yier[yierName.index(i)])

    # Copy(inherit) the result of days before
    for i in yierName:
        if i not in todayName:
            today.append(yier[yierName.index(i)])
            todayName.append(i)

    with open(unicode('analyse/总持仓-' + buyer + '.csv', 'utf-8'), 'wb') as outPuter:
        outFile = csv.writer(outPuter, dialect='excel')
        for i in today:
            varRecord = cVar[cVarName.index(i[1])]
            outFile.writerow([i[0],i[1],i[2],i[3],i[4],i[5],varRecord[0],varRecord[3],varRecord[1],varRecord[2]])
