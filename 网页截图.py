# -*- coding: utf-8 -*-

from selenium import webdriver
import time


def take_screenshot(url, save_fn="capture.png"):
    # browser = webdriver.Firefox() # Get local session of firefox
    #谷歌浏览器截取当前窗口网页
    browser = webdriver.PhantomJS(
    executable_path=r"D:\python-project\phantomjs-2.1.1-windows\bin\phantomjs.exe")  # 构建浏览器
    #phantomjs截取整张网页
    browser.maximize_window()
    browser.get(url) # Load page
    #将页面的滚动条拖到最下方，然后再拖回顶部
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);
            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    for i in range(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(10)

    browser.save_screenshot(save_fn)
    print("恭喜您，截图成功！")
    browser.close()


if __name__ == "__main__":
    url = input("请输入网址：");
    print("你输入的网址是: ", url)
    take_screenshot(url)
