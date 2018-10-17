#coding=utf-8
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='C:\phantomjs\phantomjs.exe')
driver.get("http://www.baidu.com/")
print(driver.current_url)
driver.quit()