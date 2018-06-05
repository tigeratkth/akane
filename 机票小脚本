# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:21:24 2018

@author: Tiger
"""

import requests
import datetime
import xlsxwriter as xw
import time

citystart=input('请输入出发城市，使用ISO国际码\n')
cityend=input('请输入目的城市\n')
date=input('请输入出发时间范围的开始时间，格式dd/mm/yyyy \n')
dateend = input('请输入出发时间范围的截止日期，格式dd/mm/yyyy\n')
staytime = input('请输入大致停留时间（实际计算会在停留时间加减3天）\n')
supPrice = input('请输入心理预期价格（人民币，搜索结果低于预期价位会以蓝色黑体显示）\n')


#时间运算
dateRestart=datetime.datetime.strptime(date,'%d/%m/%Y')+datetime.timedelta(days=(int(staytime)-3))
dateReend=datetime.datetime.strptime(dateend,'%d/%m/%Y')+datetime.timedelta(days=(int(staytime)+3))
dateRestartStr=dateRestart.strftime('%d/%m/%Y')
dateReendStr=dateReend.strftime('%d/%m/%Y')

#url处理
#flyFrom：出发城市
#flyTo：到达城市
#dateFrom: 搜索日期区间起点
#dateTo： 搜索日期区间终点
#loca：返回语言
#one_per_date: bool格式，打开为返回每日最低票价航班信息
#curr： 货币，CNY为人民币
urlDep= ('https://api.skypicker.com/flights?flyFrom='
              +citystart+
              '&to='
              +cityend+
              '&dateFrom='
              +date+
              '&dateTo='
              +dateend+
              '&local=en&one_per_date=1&curr=CNY')
urlRet=('https://api.skypicker.com/flights?flyFrom='
              +cityend+
              '&to='
              +citystart+
              '&dateFrom='
              +dateRestartStr+
              '&dateTo='
              +dateReendStr+
              '&local=en&one_per_date=1&curr=CNY')

#获得json格式的信息
rd=requests.get(urlDep)
#.json()意为将json格式的文件转换为字典格式，此处也可以使用json直接进行操作。
rdj=rd.json()
rr=requests.get(urlRet)
rrj=rr.json()
#获得时间和价格，存入字典文件，格式为：日期：价格
dinfo={}
rinfo={}
ddata=rdj['data']
rdata=rrj['data']
i =0
j=0
for i in range(len(ddata)):
    dinfo[ddata[i]['aTimeUTC']]=ddata[i]['price']
for j in range(len(rdata)):
    rinfo[rdata[j]['aTimeUTC']]=rdata[j]['price']
sorted(dinfo.keys())
sorted(rinfo.keys())

#构建表格
dDateList=[]
dpriceList=[]
rDateList=[]
rpriceList=[]
#字典的基本操作
for key,value in sorted(dinfo.items()):
    dDateList.append(key)
    dpriceList.append(value)
for key,value in sorted(rinfo.items()):
    rDateList.append(key)
    rpriceList.append(value)
#新建excel工作薄和工作表   
workbook = xw.Workbook('flightinfo.xlsx')
worksheet = workbook.add_worksheet('searchResult')
#制定格式
bold_format = workbook.add_format({'bold':True}) 
#将第一格宽度设置为20
worksheet.set_column(0, 0, 20)  
#在A1按照指定格式写入信息
worksheet.write('A1', '返程日期\去程日期',bold_format) 
#指定高亮信息的格式，蓝色黑体。
property = {  
    'bold': True,  
    'font_color': 'blue'  
} 

#在第一行的每一列写入特价航班的日期
row = 0
col = 1
row2 = 1
col2 = 0

for date in dDateList:
    rDate=time.strftime('%Y-%m-%d  %H:%M',time.localtime(date))
    worksheet.set_column(row,col,20)
    worksheet.write(row,col,rDate,bold_format)
    col=col+1
#在第一列写入返程航班的日期，并计算对应的去程航班和返程航班机票之和 
jj=0
ii=0
for jj in range(len(rDateList)):
    rDate2=time.strftime('%Y-%m-%d  %H:%M',time.localtime(rDateList[jj]))
    worksheet.write(row2,col2,rDate2,bold_format)
    col3 = 1
    for ii in range(len(dpriceList)):
        returenprice=dpriceList[ii]+rpriceList[jj]
        #如果价格低于预期，高亮显示
        if (returenprice < int(supPrice)):
            format = workbook.add_format(property) 
            worksheet.write(row2,col3,returenprice,format)
        else:
            worksheet.write(row2,col3,returenprice)
        col3=col3+1
        
    row2=row2+1
#关闭工作薄
workbook.close()
print('搜索完成，请查看同文件夹中flightinfo表格')




