from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread
import time


def web():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome()
    browser.get(
        'https://www.nike.com/cn/t/zoom-pegasus-35-turbo-%E7%94%B7%E5%AD%90%E8%B7%91%E6%AD%A5%E9%9E%8B-8F4K8W/AJ4114-486')
    browser.find_element_by_xpath(
        '//*[@id="buyTools"]/div[1]/div/label[4]').click()
    browser.find_element_by_xpath(
        '//*[@id="buyTools"]/div[2]/button[1]').click()
    time.sleep(3)
    i = browser.find_element_by_class_name('cart-jewel').text
    print(i)
    if i == '1':
       browser.get('https://www.nike.com/cn/zh_cn/s/register')
       browser.find_element_by_xpath(
           "//*[contains(text(),'立即登录')]").click()
       browser.find_element_by_name(
           'verifyMobileNumber').send_keys('1832342345809')  # 输入账号
       browser.find_element_by_name('password').send_keys("52234234234")  # 输入密码
       browser.find_element_by_xpath(".//*[@value='登录']").click()  # 点击登录
       print("抢货成功！！！")
    else:
        print(i)


if __name__ == '__main__':
    for i in range(3):
        t1 = Thread(target=web)
        t1.start()
    time.sleep(1000000)
