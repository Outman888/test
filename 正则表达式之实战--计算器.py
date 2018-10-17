# -*- coding: utf-8 -*-
import re
#本内容借鉴了别人的compile用法，我觉得这个用起来，代码比较简洁，明了

bk = re.compile(r'\([^()]+\)')  # 寻找最内层括号规则
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')  # 寻找乘法运算规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')  # 寻找除法运算规则
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')  # 寻找加法运算规则
subt = re.compile(r'(-?\d+\.?\d*\-{2}\d+\.?\d*)|(-?\d+\.?\d*\-\d+\.?\d*)')  # 寻找减法运算规则
remove = re.compile(r'[^(].*[^)]')  # 脱括号规则

def cal_mul(s):
    '''计算表达式中的乘法'''
    sp = re.split(r'\*',mul.search(s).group())
    result = str(float(sp[0]) * float(sp[1]))
    return result

def cal_div(s):
    '''计算表达式中的除法'''
    sp = re.split(r'\/',div.search(s).group())
    result = str(float(sp[0]) / float(sp[1]))
    return result

def cal_add(s):
    '''计算表达式中的加法'''
    sp = re.split(r'\+',add.search(s).group())
    result = re.sub(add,str(float(sp[0]) + float(sp[1])),s,count=1)
    return result

def cal_subt(s):
    '''计算表达式中的减法'''
    sp = subt.search(s).group()
    if sp.startswith('-'):                                     #如果表达式是以-开头 -1-1
        s1 = re.sub(r'\-','+',sp)                              #将-替换成+        +1+1
        s2 = cal_add(s1)                                       #调用加法           +2
        s3 = re.sub(r'\++','-',s2)                             #将结果替换成-       -2
        result = re.sub(subt,s3,s,count=1)
    else:
        s1 = re.split(r'\-',sp)
        result = re.sub(subt,str(float(s1[0]) - float(s1[1])),s,count=1)
    return result

def main():
    while True:
        s = input("请输入计算公式(q退出) >>>>")
        if s == "q":
            exit()
        else:
            s = "".join([i for i in re.split('\s+',s)])        #将输入的表达式中空格去掉
            if  not s.startswith('(') or not s.endswith(')'):  #判断输入是否在括号内
                s = "(%s)"%s                                   # 1+2 -->(1+2)
            while bk.search(s):                                #判断s中是否有内层括号
                s = re.sub(r'\-{2}','+',s)                     #如果表达式中含有--  -->  +     例如：--2 --> +2
                s1 = bk.search(s).group()                      #找到最内存括号
                if div.search(s1):                             #判断s1中是否有除法
                    s2 = div.search(s1).group()                #获得除法的表达式
                    s3 = s1.replace(s2,cal_div(s2))            #字符串替换
                    if re.search(r'\(\+?\-?\d+\.?\d*\)',s3):   #判断s3是否为括号内的值 例如：(3)
                        s3 = remove.search(s3).group()         #将值的括号去掉　　　　(3) --> 3
                    s = s.replace(s1,s3)                       #将s中的s1替换为s3
                elif mul.search(s1):                           #判断表达式中是否有乘法
                    s2 = mul.search(s1).group()
                    s3 = s1.replace(s2,cal_mul(s2))
                    if re.search(r'\(\+?\-?\d+\.?\d*\)',s3):
                        s3 = remove.search(s3).group()
                    s = s.replace(s1,s3)
                elif subt.search(s1):                          #判断表达式中是否有减法
                    s2 = subt.search(s1).group()
                    s3 = s1.replace(s2,cal_subt(s2))
                    if re.search(r'\(\+?\-?\d+\.?\d*\)',s3):
                        s3 = remove.search(s3).group()
                    s = s.replace(s1,s3)
                elif add.search(s1):                           #判断表达式中是否有加法
                    s2 = add.search(s1).group()
                    s3 = s1.replace(s2, cal_add(s2))
                    if re.search(r'\(\+?\-?\d+\.?\d*\)',s3):
                        s3 = remove.search(s3).group()
                    s = s.replace(s1,s3)
            print("计算结果是：%s"%s)

if __name__ == '__main__':
    main()