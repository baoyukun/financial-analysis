#coding=utf-8
import time
from dateSort import sort
from cleaning import cleanData
from analysis import analyse
from synthesis import conclusion

start = time.clock()

date = ['2017-5-19', '2017-5-17', '2017-5-18', '2017-5-16']

who = ['中信证券股份有限公司上海古北路证券营业部',
       '中信证券股份有限公司上海淮海中路证券营业部',
       '中信证券股份有限公司上海溧阳路证券营业部',
       '中信证券股份有限公司上海漕溪北路证券营业部',
       '中信证券股份有限公司杭州四季路证券营业部',
       '中信建投证券股份有限公司重庆涪陵广场路证券营业部',
       '中国中投证券有限责任公司杭州环球中心证券营业部',
       '中国银河证券股份有限公司绍兴证券营业部',
       '中国银河证券股份有限公司杭州庆春路证券营业部',
       '中国银河证券股份有限公司北京阜成路证券营业部',
       '国泰君安证券股份有限公司上海江苏路证券营业部',
       '国泰君安证券股份有限公司上海福山路证券营业部',
       '国泰君安证券股份有限公司宁波君子街证券营业部',
       '国泰君安证券股份有限公司成都北一环路证券营业部',
       '方正证券股份有限公司上海保定路证券营业部',
       '方正证券股份有限公司绍兴胜利东路证券营业部',
       '方正证券股份有限公司杭州延安路证券营业部',
       '招商证券股份有限公司深圳蛇口工业七路证券营业部',
       '申万宏源证券有限公司上海闵行区东川路证券营业部',
       '东吴证券股份有限公司苏州西北街证券营业部',
       '华鑫证券有限责任公司宁波沧海路证券营业部',
       '华宝证券有限责任公司舟山解放西路证券营业部',
       '华泰证券股份有限公司成都南一环路第二证券营业部',
       '华泰证券股份有限公司舟山解放东路证券营业部',
       '华泰证券股份有限公司武汉首义路证券营业部',
       '华泰证券股份有限公司深圳益田路荣超商务中心证券营业部',
       '华泰证券股份有限公司上海武定路证券营业部',
       '华泰证券股份有限公司厦门厦禾路证券营业部',
       '光大证券股份有限公司佛山季华六路证券营业部',
       '湘财证券股份有限公司上海陆家嘴证券营业部',
       '财通证券股份有限公司温岭中华路证券营业部',
       '广发证券股份有限公司泉州涂门街证券营业部',
       '浙商证券股份有限公司临安万马路证券营业部']

sortedDate = sort(date)

cleanData(sortedDate[-1])

for i in who:
    analyse(i, sortedDate)

conclusion(who, sortedDate[-1])

end = time.clock()
print '......analysis took %fs, successfully done :)' % (end-start)
