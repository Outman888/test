import json
import demjson
import datetime
import requests
from threading import Timer
import itchat


def printweather():
    r = requests.get('http://api.jirengu.com/getWeather.php?city=舟山')
    data = demjson.decode(r.text)
    print(type(data))
    data1 = data['weather'][0]['last_update']
    data3 = ""
    for i in range(11):
        try:
            rq = data['weather'][0]['future'][i]['date']  # 日期
            high = data['weather'][0]['future'][i]['high']  # 最高温度
            low = data['weather'][0]['future'][i]['low']  # 最低温度
            day = data['weather'][0]['future'][i]['day']  # 星期几
            text = data['weather'][0]['future'][i]['text']  # 天气情况
            data2 = day + rq[5:10] + ":" + text + \
                " " + low + "℃-" + high + "℃ "
            if data2:
                data3 = data3 + data2 + "\n\n"
            else:
                print("url为空")
                break
        except BaseException:
            print("")
    print(data1 + "\n" + data3)
# account=itchat.get_friends('Flyer_hxd')
# print(type(account))
# print(str(account[0]))
# print(type(str(account[0])))
# username=eval(str(account[0]))
# print(username)
# print(type(eval(str(account[0]))))
# print(username['UserName'])
    itchat.send_msg("主人，今天舟山的天气如下：" + "\n" + data3, toUserName='filehelper')
    if datetime.datetime.now().hour == 6:
            # 想给谁发信息，先查找到这个朋友
        users = itchat.search_friends(name=u'贺贤东')
        # 找到UserName
        userName = users[0]['UserName']
        itchat.send("主人，今天舟山的天气如下：" + "\n" + data3, toUserName=userName)
        users = itchat.search_friends(name=u'阿拉少爷')
        # 找到UserName
        userName = users[0]['UserName']
        itchat.send("主人，今天舟山的天气如下：" + "\n" + data3, toUserName=userName)
    t = Timer(1800, printweather)
    t.start()


if __name__ == "__main__":
    itchat.auto_login()
    printweather()
