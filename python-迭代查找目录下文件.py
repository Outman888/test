# -*- coding: utf-8 -*-

fo=open("a.txt",encoding="utf-8")
print(fo.name)
print(fo.closed)
print(fo.mode)
try:
     print(fo.read())
except  Exception as err:
     print(err)
finally:
     fo.close()