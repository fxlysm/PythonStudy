#coding:utf-8

# 法一：
# f=open('foo.txt','r')
# contents = f.read()
# print  contents

#法二
with open('foo.txt','r') as file:
    contents =file.read()
    print  contents

# 1、第一种写法在文件使用结束后需要关闭文件
# 而第二种写法会自动识别（在需要的时候 打开）

# 2、 第一种攘量 f 为全局变量
#     第二咱写法 变量为file为全局变量
