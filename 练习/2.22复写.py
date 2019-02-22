class student:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('你的名字是%s ' % self.name)
def studentinfo(s):
    s.info()

一中=student('流川枫')
studentinfo(一中)

print('*'*30)

class test:
    a=100
    def __init__(self,b):
        self.b=b
t=test(200)
print('t.a=%d' % t.a)
print('test.a=%d' % test.a)
print('t.b=%d' % t.b)

print('*'*40)

class student2:
    def __init__(self,num):
        self.__num=num
    def print_name(self):
        print('your age is %d' % self.__num)
    def __ask(self):
        self.print_name()
    def ask2(self):
        self.__ask()
age=student2(30)
age.ask2()

class people:
    country='china'
    @classmethod
    def get_country(cls):
        return cls.country
p=people()
print(p.get_country())
print(people.get_country())

class people2:
    country='china'
    @classmethod
    def get_country(cls):
        return cls.country
    @classmethod
    def set_country(cls,country):
        cls.country=country
p=people2()
print(p.get_country())
p.set_country('USA')
print(p.get_country())

class dog:
    def __init__(self,name,color='black'):
        self.name=name
        self.color=color
    def run(self):
        print('汪汪汪!!')

class 柯基(dog):
    def set_name(self,name):
        self.name=name
    def eat(self):
        print('%s : i m eating!')
小短腿=柯基('饭饭')
print('名字为%s '% 小短腿.name)
小短腿.eat()
小短腿.set_name('科科')
print('现在换狗了,是%s ' % 小短腿.name)

class a:
    def printa(self):
        print('aaa')
class b:
    def printb(self):
        print('bbb')
class c(a,b):
    def printc(self):
        print('ccc')
阿C=c()
阿C.printa()

class 动物:
    def 叫(self):
        print('ao!!')
class 狗:
    def 叫(self):
        print('wang!')
class 猫:
    def 叫(self):
        print('miao!')

def test2(类):
    类.叫()

动物=动物()
动物.叫()
狗=狗()
猫=猫()

test2(狗)
test2(猫)

import time     ##导入time模块,一下会用到里面的time.time这个函数
def 装饰器(目标程序):    ##往装饰器导入参数--('目标程序'作为参数) 
    def 计时程序():        ##用计时程序来算目标程序的用时
        开始计时=time.time()   ##运用time.time函数记录开始时间
        目标程序()          ##此处开始run目标程序
        结束计时=time.time()   ##运用time.time函数记录结束时间
        用时=结束计时-开始计时  ##相减得出目标函数的运行时间
        print('消耗的时间为%d'% 用时)  ##打印结果出来
    return 计时程序            ##结束装饰器,要求计时程序交出结果

@装饰器    ##用这个来连接目标程序与装饰器,当目标程序启动即可触发装饰器

def 目标程序():     ##老板给的目标程序,要你计算运行消耗时间   
    print('hello')
    time.sleep(1)   ##执行此函数,停止一秒,然后继续运行
    print('world!')

目标程序()              ##通过运行目标程序来启动装饰器







