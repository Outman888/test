# -*- coding: utf-8 -*-
#python 2.7.9
'''
    百度即用API -- 天气调用
    通过拼音访问城市天气
'''
import sys, urllib.request,json

url = "http://apis.baidu.com/apistore/weatherservice/weather?citypinyin="

city= input("输入你想查询城市的名称拼音:")
#完整api访问接口
url=url+city

req = urllib.request.Request(url)
#给定header
#这里注意填写自己的apikey
req.add_header("apikey", "2c967fe4a5c591dcbd03acbf80f7f679")

resp = urllib.urlopen(req)
content = resp.read()

#通过json的loads将获得数据内容转换成python对象
info = json.loads(content);

#获取具体内容
if(info['errNum'] == -1):
    print (info['errMsg'])
else:
    print ("你查询的当地天气信息如下：")
    print ("城市：", info['retData']['city']  )
    print ("经度：", info['retData']['longitude'])
    print ("纬度：", info['retData']['latitude'])
    print ("查询日期：", info['retData']['date'])
    print ("最新预报时间：", info['retData']['time'])
    print ("海拔：", info['retData']['altitude'])
    print ("天气：", info['retData']['weather'])
    print ("最低气温：", info['retData']['l_tmp'])
    print ("最高气温：", info['retData']['h_tmp'])
    print ("风向：", info['retData']['WD'])
    print ("风力：", info['retData']['WS'])
    print ("日出时间：", info['retData']['sunrise'])
    print ("日落时间：", info['retData']['sunset'])