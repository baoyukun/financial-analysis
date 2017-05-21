#coding=utf-8
import string

def numFormat(s):
    result = s.split()
    for i in range(3,6):
        result[i] = string.atof(result[i])
    return result

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
    a = []
    b = []

    with open(unicode('analyse/'+buyer+'.txt', 'utf-8'), 'w') as outFile:
        for i in dateList:
            with open(unicode('out/'+i+'-券商.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    if buyer in j:
                        numRecord = numFormat(j)
                        if numRecord not in a:
                            print >>outFile, j[:-1]
                            a.append(numRecord)


    with open(unicode('analyse/'+buyer+'-三日.txt', 'utf-8'), 'w') as outFile:
        for i in dateList:
            with open(unicode('out/'+i+'-券商三日.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    if buyer in j:
                        numRecord = numFormat(j)
                        if numRecord not in b:
                            print >>outFile, j[:-1]
                            b.append(numRecord)

    permuBack1 = [3,0,1,2]
    permuBack3 = [1,2,3,0]
    permuForward = [1,2,3,0]
    pointer = 3
    c = [[],[],[],[]]
    cName = [[],[],[],[]]
    cVar = []
    cVarName = []
    ai = 0
    alen = len(a)
    bi = 0
    blen = len(b)

    for date in dateList:
        pointer = permuForward[pointer]
        [today, todayName, yier, yierName, avantHier, avantHierName] = [[], [], c[permuBack1[pointer]], cName[permuBack1[pointer]], c[permuBack3[pointer]], cName[permuBack3[pointer]]]

        # Update the result of three days before
        while (bi<blen and b[bi][0]==date):
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
        while (ai<alen and a[ai][0]==date):
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

        c[pointer] = today
        cName[pointer] = todayName

    with open(unicode('analyse/总持仓-'+buyer+'.txt', 'utf-8'), 'w') as outFile:
        for i in c[pointer]:
            varRecord = cVar[cVarName.index(i[1])]
            print >>outFile, '%-20s%-30s%-110s%-70f%-70f%-70f%-30s%-70f%-70f%-30f'%(i[0],i[1],i[2],i[3],i[4],i[5],varRecord[0],varRecord[3],varRecord[1],varRecord[2])