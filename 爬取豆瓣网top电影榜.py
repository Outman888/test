import pymysql
from selenium import webdriver
wd = webdriver.PhantomJS(
    executable_path=r"D:\python-project\phantomjs-2.1.1-windows\bin\phantomjs.exe")  # 构建浏览器
Url = 'https://movie.douban.com/tv/#!type=tv&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit=20&page_start=140'
wd.get(Url)
def get_conn():
    '''建立数据库连接'''
    conn = pymysql.connect(host='192.168.23.222',
                                user='root',
                                password='123456',
                                db='python',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return conn
def main():
   conn = get_conn()  # 建立数据库连接
   for i in range(1,201): #排行前200
     text= wd.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/div[4]/div/a[' + str(i) + ']/p').text
     if i in (19, 39, 59, 79, 99, 119, 139, 159, 179, 199):  # 在这些数的时候加载一次
        wd.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div[4]/a').click()  # 点击加载更多
     print(text)
     # 创建sql 语句，并执行
     cursor = conn.cursor() #创建游标
     sql = "INSERT INTO `movie` (`id`, `name`) VALUES ('"+str(i)+"', '"+text+"')"
     cursor.execute(sql)
     conn.commit()
   conn.close()  # 关闭数据库连接

if __name__ == '__main__':
        main()
