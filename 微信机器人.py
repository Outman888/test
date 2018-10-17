from wxpy import *
bot = Bot()

# 机器人账号自身
myself = bot.self

# 向文件传输助手发送消息
bot.file_helper.send('Hello from wxpy!')

bot = Bot()
# 在 Web 微信中把自己加为好友
bot.self.add()
bot.self.accept()

# 发送消息给自己
bot.self.send('能收到吗？')
my_friend = ensure_one(bot.search('👽贺贤东👽'))
tuling = Tuling(api_key='6690099e99a9425399755f3115fd9497')

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)