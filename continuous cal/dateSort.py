import string

def sort(dateFormatList):
    dateNumList = []
    sortedFormatList = []
    
    for j in [i.split('-') for i in dateFormatList]:
        dateNumList.append([string.atoi(k) for k in j])
    
    dateNumList.sort()
    
    for i in dateNumList:
        sortedFormatList.append('%d'%i[0]+'-'+'%d'%i[1]+'-'+'%d'%i[2])
    
    return sortedFormatList