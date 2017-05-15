#coding=utf-8
import string
        
def numFormat(s):
    result = s.split()
    for i in range(3,6):
        result[i] = string.atof(result[i])
    return result

def add(x,x0):
    for i in x:
        if i[1]==x0[1]:
            i[0] = x0[0]
            i[3] += x0[3]
            i[4] += x0[4]
            i[5] += x0[5]
            break
    return x
            
def analyse(buyer, dateList):
    a = []
    b = []
    
    with open(unicode('analyse/'+buyer+'.txt', 'utf-8'), 'w') as outFile:
        for i in dateList:
            with open(unicode('out/'+i+'-券商.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    if buyer in j:
                        print >>outFile, j[:-1]
                        a.append(numFormat(j))
                        
    
    with open(unicode('analyse/'+buyer+'-三日.txt', 'utf-8'), 'w') as outFile:
        for i in dateList:
            with open(unicode('out/'+i+'-券商三日.txt', 'utf-8'), 'r') as inFile:
                for j in inFile:
                    if buyer in j:
                        print >>outFile, j[:-1]
                        b.append(numFormat(j))
    
    permu = [0,2,3,4,1]
    permuBack = [0,4,1,2,3]
    pointer = 4
    c = [[],[],[],[],[]]
    cName = [[],[],[],[],[]]
    ai = 0
    bi = 0
    
    for i in range(len(dateList)):
        pointer = permu[pointer]
        c[pointer] = []
        cName[pointer] = []
        
        # Add on the result of three days before
        j = permu[pointer]
        while (bi<len(b) and b[bi][0]==dateList[i]):
            if b[bi][1] in cName[pointer]:
                c[pointer] = add(c[pointer], b[bi])
            else:
                cName[pointer].append(b[bi][1])
                if b[bi][1] not in cName[j]:
                    c[pointer].append(b[bi])
                else:
                    for k in c[j]:
                        if k[1]==b[bi][1]:
                            c[pointer].append(k)
                            break
                    c[pointer] = add(c[pointer], b[bi])
            bi += 1
        
        record = cName[pointer]
        
        # Add on the result of today
        j = permuBack[pointer]
        while (ai<len(a) and a[ai][0]==dateList[i]):
            if a[ai][1] not in record:
                if a[ai][1] in cName[pointer]:
                    c[pointer] = add(c[pointer], a[ai])
                else:
                    cName[pointer].append(a[ai][1])
                    if a[ai][1] not in cName[j]:
                        c[pointer].append(a[ai])
                    else:
                        for k in c[j]:
                            if k[1]==a[ai][1]:
                                c[pointer].append(k)
                                break
                        c[pointer] = add(c[pointer], a[ai])
            ai += 1
               
        # Copy the result of yesterday
        for k in c[j]:
            if k[1] not in cName[pointer]:
                cName[pointer].append(k[1])
                c[pointer].append(k)
                
    with open(unicode('analyse/'+'总持仓-'+buyer+'.txt', 'utf-8'), 'w') as outFile:
        for i in c[pointer]:
            print >>outFile, '%-20s%-30s%-110s%-70f%-70f%-30f'%(i[0],i[1],i[2],i[3],i[4],i[5])