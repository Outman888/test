#!/usr/bin/python3

import pymysql
import os

# 打开数据库连接
db = pymysql.connect("192.168.23.222", "root", "123456", "mypython")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

try:
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * from user")

    #fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    #fetchall(): 接收全部的返回结果行.
    #rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
    results = cursor.fetchall()
    for row in results:
      user = row[0]
      # 打印结果
      print("user=%s" %
          (user))
except BaseException:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
os.system('pause') #按任意键继续