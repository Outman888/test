# coding:utf-8
import urllib.request
import urllib.parse
import re
import urllib
import chardet

pattern = re.compile(r'StationID=Z\d{8}">[\u4e00-\u9fa5]{1,50}')
pattern1 = re.compile(r'[\u4e00-\u9fa5]{1,50}')


# 返回指定网页的内容
def open_url(url):
    try:
        req = urllib.request.Request(url)
        req.add_header(
            'User-Agent',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
        response = urllib.request.urlopen(req)
        html = response.read()
        chardit1 = chardet.detect(html)
        html_string = html.decode(chardit1['encoding']).encode('utf-8')
        html_string = html_string.decode('utf-8')
        return html_string
    except Exception as err:
        return "1111111111"
    finally:
        print("Goodbye!")

    # num为用户自定，返回的是所有页的段子列表


def get_content(num):
    text_list = []  # 获取公司id列表
    for page in range(20001, int(num)):
        address = 'http://www.93rc.com/Q/CompanyInfo.aspx?CompanyID=Z' + \
            str(page)
        html = open_url(address)
        print(address)
        result = re.findall(pattern, html)
        print(result)

        # 每一页的result都是一个列表，将里面的内容加入到text_list
        for each in result:
            result1 = re.findall(pattern1, each)
            print(result1[0])
            text_list.append(result1[0])

    print(text_list)
    return text_list


# num是指定网页页数
def save(num):
    # 写方式打开一个文本，把获取的段子列表存放进去
    with open('a.txt', 'w', encoding='utf-8') as f:
        text = get_content(num)
        # 和上面去掉<br />类似
        for each in text:
            if '<br />' in each:
                new_each = re.sub(r'<br />', '\n', each)
                f.write(new_each)
            else:
                f.write(str(each) + '\n')


if __name__ == '__main__':
    content = save(21001 + 1)
