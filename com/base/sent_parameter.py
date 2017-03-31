#coding:utf-8
#1
def get(text01,text02):
    print 'my name is '+text01+' , '+'Other name is '+text02

get('liuyong','lambert')

#2
def pet(animal_type='cat',pet_name='tom'):
    print '\n I have a '+animal_type+'.'
    print 'My '+animal_type+" 's name is "+pet_name

pet('tom')
pet('mouse','jerry')


# 3
def name(first_name,last_name):
    full_name=first_name+last_name
    return full_name

music = name('lambert','liu')
print music


#4
# 闭包：
# 内部函数对外部函数作用区域里变量的引用（非全局变量）
# 一个闭包就是你调用了一个函数A 这个函数A 返回了一个函数B给你 这个返回的函数B就叫闭包

# 装饰器：在不改变
def func1(num):
    print 'func1:',num

    def func2(num1):
        print  'func',num1

        return num1+num
    return func2
res =func1(20)   # res ==func2
print res(30)  #res(30) ==func2(30)





#5

def foo():
    m=0
    def foo1():
        m=1
        print m
    print m

    foo1()
    print m

foo()


# 6
print  '#6'
def outer():
    a=1
    def inner():
        b = a+1
        return b
    return inner
c=outer()
print  c()



print  '#7'
def outer2():
    a=[1]
    def inner():
        a[0] = a[0]+1
        return a[0]
    return inner
c=outer2()
print  c()