#re模块下的函数

#compile(pattern)：创建模式对象
import re
pat = re.compile('A')
m = pat.search('CBA')  # 等价于 re.search('A','CBA')
print(m)
m = pat.search('CBD')
print(m)
None  # 没有匹配到，返回None（False）

#search(pattern,string)：在字符串中寻找模式
m=re.search('A','ABCAAA')
print(m)
m=re.search('d','11112121')
print(m)
None

