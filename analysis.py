#coding=utf-8
import string

def numFormat(s):
    result = s.split()
    for i in range(3,6):
        result[i] = string.atof(result[i])
    return result

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
    ai = 0
    alen = len(a)
    bi = 0
    blen = len(b)

    for date in dateList:
        pointer = permuForward[pointer]
        [today, todayName, yier, yierName, avantHier, avantHierName] = [[], [], c[permuBack1[pointer]], cName[permuBack1[pointer]], c[permuBack3[pointer]], cName[permuBack3[pointer]]]

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

        for i in yierName:
            if i not in todayName:
                today.append(yier[yierName.index(i)])
                todayName.append(i)

        c[pointer] = today
        cName[pointer] = todayName

    with open(unicode('analyse/总持仓-'+buyer+'.txt', 'utf-8'), 'w') as outFile:
        for i in c[pointer]:
            print >>outFile, '%-20s%-30s%-110s%-70f%-70f%-30f'%(i[0],i[1],i[2],i[3],i[4],i[5])
