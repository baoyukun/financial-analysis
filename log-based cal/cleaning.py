#coding=utf-8
import re
import csv
import string

def wanToYi(s):
    value = (re.split('：|万|亿',s))[1]
    if '万' in s:
        value = '%f' % (string.atof(value)/10000)
    return value

def wanToYi1(s):
    value = (re.split('<|>',s))[2]
    if '万' in s:
        value = '%f' % (string.atof(value)/10000)
    return value

def wanToYi2(s):
    value = (re.split('<|>',s))[1]
    value = '%f' % (string.atof(value)/10000)
    return value

def cleanData(date):
    with open('in/'+date+'.txt', 'r') as inFile:
        text = inFile.read()

    stockRecord = re.findall('>.*明细：.*证券', text)
    dealRecord = re.findall('成交额：.*元', text)
    buyRecord = re.findall('合计买入：.*元', text)
    sellRecord = re.findall('合计卖出：.*元', text)
    netRecord = re.findall('净额：.*元', text)
    whoRecord = (re.compile('买入金额最大的前5名营业部.*?跟买成功率：', re.DOTALL)).findall(text)

    # For debugging, you can at any time print the record to the file by using
    # print (' '*5).join(Record)+'\n'

    with open(unicode('out/'+date+'-股票.csv', 'utf-8'),'wb') as out1, open(unicode('out/'+date+'-券商.csv', 'utf-8'),'wb') as out2, open(unicode('out/'+date+'-股票三日.csv', 'utf-8'),'wb') as out3, open(unicode('out/'+date+'-券商三日.csv', 'utf-8'),'wb') as out4:
        iterator = -1
        for entry in stockRecord:
            iterator += 1
            if '连续三个交易日' in entry:
                outFile1 = csv.writer(out3, dialect='excel')
                outFile2 = csv.writer(out4, dialect='excel')
            else:
                outFile1 = csv.writer(out1, dialect='excel')
                outFile2 = csv.writer(out2, dialect='excel')

            name = (re.split('>|\)',entry))[1] + ')'
            deal = wanToYi(dealRecord[iterator])
            buy = wanToYi1(buyRecord[iterator])
            sell = wanToYi1(sellRecord[iterator])
            net = wanToYi1(netRecord[iterator])

            outFile1.writerow([date, name, deal, buy, sell, net])

            who = re.findall('title=".*"', whoRecord[iterator])
            action = re.findall('tr rel">.*<', whoRecord[iterator])

            for i in range(len(who)):
                calling = (re.split('"',who[i]))[1]
                if calling == '机构专用':
                    continue
                outFile2.writerow([date, name, calling, wanToYi2(action[i*3]), wanToYi2(action[i*3+1]), wanToYi2(action[i*3+2])])
