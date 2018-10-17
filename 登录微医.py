import json
import demjson
import requests
from time import sleep
from selenium import webdriver
wd = webdriver.PhantomJS(
    executable_path=r"D:\python-project\phantomjs-2.1.1-windows\bin\phantomjs.exe")  # 构建浏览器
loginUrl = 'https://www.guahao.com/user/login'
wd.get(loginUrl)  # 进入登陆界面
wd.find_element_by_xpath(
    '//*[@id="loginId"]').send_keys('18768061363')  # 输入用户名
wd.find_element_by_xpath(
    '//*[@id="password"]').send_keys('513shenghewo')  # 输入密码
wd.save_screenshot(str("登录界面.png"))
wd.find_element_by_name("validCode").send_keys(input("输入验证码\n>>> "))
wd.find_element_by_xpath('//*[@id="J_LoginSubmit"]').click()  # 点击登陆
req = requests.Session()  # 构建Session
cookies = wd.get_cookies()  # 导出cookie
for cookie in cookies:
    req.cookies.set(cookie['name'], cookie['value'])  # 转换cookies
test = req.get('https://www.guahao.com/expert/new/shiftcase/?expertId=127556466557799000&hospDeptId=127548647953601000&hospId=125369370584301000')
# json string:
data = demjson.decode(test.text)
for i in range(10):
    try:
        url = data['data']['shiftSchedule'][i]['url']
        if url:
            print("第" + str(i) + "个：" + url)
        else:
            print("url为空")
            break
    except BaseException:
        print("所有未约满的已经列出！")

url_1 = wd.get('https://www.guahao.com' + url)
try:
    wd.find_element_by_xpath(
        '// *[ @ id = "J_DiseaseName"]').send_keys('身体不舒服')  # 输入密码
    wd.find_element_by_xpath(
        '/ html / body / div[1] / div[2] / div[1] / form / div[2] / div[6] / div / label / input').click()  # 点击登陆
    wd.find_element_by_xpath('//*[@id="J_Booking"]').click()  # 点击登陆
    print("预约成功！")
except BaseException:
    print("预约异常！")
