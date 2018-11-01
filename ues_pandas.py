#!/user/bin/python
#-*-coding:utf-8-*-

from pandas import Series
import pandas as pd

s = Series([1,4,'aaa','bb'])
# print(s[1])
#索引
# print(s.index)
#值
# print(s.values)
#可以自定义索引
s2 = Series(['zhangsan','man',30], index=['name','sex','age'])
# print(s2)
# print(s2['name'])

ss = Series({'id':123,'name':'test','date':'20181015'})
#如果自定义了索引，自定的索引会自动寻找原来的索引，如果一样的，就取原来索引对应的值，这个可以简称为“自动对齐”。
# print(ss['id'])
ss1 = Series({'id':123,'name':'test','date':'20181015'}, index=['id','name','time'])
# print(ss1['names'])
#判断是否为空
# print(ss1.isnull())
#重新定义索引
ss1.index = ['a','b','c']
# print(ss1)

#二维数组
from pandas import DataFrame
#字典套列表
data = {'name':['google','baidu','yahoo'],'marks':[100,200,300],'price':[1,2,3]}
f1 = DataFrame(data)
# print(f1)
#键值顺序可以自定义
f2 = DataFrame(data,columns=['marks','name','price'])
# print(f2)
#字典套字典
newdata = {'lang':{'first':'python','second':'java'},'price':{'first':5000,'second':1000}}
f3 = DataFrame(newdata)
# print(f3)
print(f3['lang'])