import datetime
import itchat
itchat.auto_login()
users = itchat.search_friends(name=u'小贝')
#找到UserName
userName = users[0]['UserName']
itchat.send("主人，今天舟山的天气如下：")
print(datetime.datetime.now().hour)
