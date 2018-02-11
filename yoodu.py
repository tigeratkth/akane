# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:51:20 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
url1=input("请输入第一章的地址")
url2=input("请输入最后一章的地址")
name=input("请输入书名")
nums=0 #帮助处理url
for i in range(len(url1)):
    
    if url1[-i] in ['/']:
        tag1=url1[-i+1:-5]
        nums=i-1
        break
    
    
for i in range(len(url2)): 
    if url2[-i] in ['/']:
        tag2=url2[-i+1:-5]
        break
#处理扫面页数
tag1=int(tag1)
tag2=int(tag2)
num=tag2-tag1+1
page=tag1-1
#新建字符串用于存储
book=''
#确定起始位置

#新建用于保存的txt文件

#处理url
urlFront=url1[0:-nums]
#处理文件位置

adr=name+'.txt'
fSace= open(adr,'a')
#递增改变地址
for i in range(num):
    page= page+1
    #原始地址
    url=urlFront +str(page)+'.html'
    #访问时间30ms，本来使用try结构，但是ping之后发现网站很稳定，因此直接爬取就好。
    r=requests.get(url,timeout=30)
    #在网站的源代码中标示使用utf-8编码
    r.encoding = 'utf-8'
    rawText=r.text    
    #煲汤开始
    soup = BeautifulSoup(rawText, "html.parser")
    #直接使用string方法提取字符串
    mTitle = soup.find('h1').string
    #使用find_all方法提取所有p标签中的内容
    mText = soup.find_all('p')
    #将标题写入book中，并换两行与正文区分
    book = book+mTitle+'\n\n'
    #提取每个p标签中的内容
    for i in range(len(mText)):
            tr=mText[i].string
            #段首缩进，段尾换行
            book =  book +"    " +tr+'\n\n'    
    #本章保存完毕，换很多行与下一章区别
    book=book+'\n\n\n\n\n\n'
#写入书中
fSace.write(book)
#好习惯，用完关闭！
fSace.close()

    
    
    
    
