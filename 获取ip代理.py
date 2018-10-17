#作者：晴天
#链接：https://www.zhihu.com/question/47464143/answer/234430051
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#-*- coding:utf-8 -*-
import urllib.request
import re
import requests
import pymysql

#抓取三个网页上比较新的免费代理ip和port到_crawl
def _gaoni():
    urls=['http://www.ip3366.net/free/?stype=1&page=1',
          'http://www.ip3366.net/free/?stype=1&page=2']
    re_gaoni=re.compile(r'(\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3})</td>\s*?\n\s*?<td>(\d{2,5})')
    list_gaoni=[]
    maxtrynum=10
    for url in urls:
        for tries in range(maxtrynum):
            try:
                response=urllib.request.Request(url)
                page=urllib.request.urlopen(response)
            except:
                if tries < (maxtrynum-1):
                   continue
                else:
                    print ('failed')
        html=page.read().decode('utf-8',errors='ignore')#python3
        list_gaoni=list_gaoni+re_gaoni.findall(html)
    return list_gaoni

def _66ip():
    urls=['http://www.66ip.cn/index.html',
          'http://www.66ip.cn/2.html']
    re_66ip=re.compile(r'(\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3})</td><td>(\d{2,5})')
    list_66ip=[]
    maxtrynum=10
    for url in urls:
        for tries in range(maxtrynum):
            try:
                response=urllib.request.Request(url)
                page=urllib.request.urlopen(response)
            except:
                if tries < (maxtrynum-1):
                   continue
                else:
                    print ('failed')
        html=page.read().decode('utf-8',errors='ignore')#python3
        list_66ip=list_66ip+re_66ip.findall(html)
        print(list_66ip)
    return list_66ip

def _httpdaili():
    re_httpdaili=re.compile(r'(\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3})</td>\s*?\n\s*?<td>(\d{2,5})')
    list_httpdaili=[]
    maxtrynum=10
    for tries in range(maxtrynum):
        try:
            response=urllib.request.Request('http://www.httpdaili.com/mfdl/')
            page=urllib.request.urlopen(response)
        except:
            if tries < (maxtrynum-1):
               continue
            else:
                print ('failed')
    html=page.read().decode('utf-8',errors='ignore')#python3
    list_httpdaili=list_httpdaili+re_httpdaili.findall(html)
    return list_httpdaili

_crawl=_gaoni()+_66ip()+_httpdaili()

#抓取数据库中ip_agent表的数据到_MySQLdata,清空ip_agent
host='127.0.0.1'
dbName='hello'
user='root'
password='root'
db=pymysql.connect(host,user,password,dbName,charset='utf8')
cur=db.cursor()
try:
    cur.execute("SELECT * FROM ip_agent")
    _MySQLdata=cur.fetchall()
except:
    print ("can't fetch MySQLdata")
db.commit()
try:
    cur.execute("DELETE FROM ip_agent")
    db.commit()
except:
    db.rollback()

#整合去重
_all=[]
for m in _crawl:
    if m not in _all:
       _all.append(m)
for n in _MySQLdata:
    if n not in _all:
       _all.append(n)

#筛选出有效数据
_useful=[]
for i in _all:
    proxies={"http":"http://"+i[0]+":"+i[1]}
    url='http://www.baidu.com'
    try:
        requests.get(url,proxies)
    except:
        pass
    else:
        if i not in _useful:
           _useful.append(i)

#存入数据库
for m in _useful:
    param=(m[0],m[1])
    sql="INSERT INTO ip_agent VALUES (%s,%s)"
    cur.execute(sql,param)
cur.close()
db.commit()
db.close()