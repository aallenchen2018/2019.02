class student:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('你的名字是%s' % self.name)

def studentinfo(s):
    s.info()

一中=student('流川枫')
studentinfo(一中)

print('*'*30)
class test:
    a=100           #类自身属性
    def __init__(self,b):    #实例的属性
        self.b=b

t=test(200)
#两种方式访问类自身的属性
print('t.a=%d' % t.a)
print('test.a=%d' % test.a)
#一种方式访问实例的属性
print('t.b=%d' % t.b)

print('*'*40)
#########类的私有化##############
# class student:
#     def __init__(self):
#         self.__number=30
# 五班=student()
# #__number就是私有化属性
# #不能直接访问私有化属性,间接访问
class student2:
    def __init__(self,num):
        self.__num=num
    def print_name(self):
        print('your age is %d' %self.__num)
    def __ask(self):
        self.print_name()
    def ask2(self):
        self.__ask()
age=student2(30)
age.print_name()
age.ask2()

##########类的方法###############
class people:
    country='china'
    @classmethod
    def getcountry(cls):
        return cls.country
p=people()
print(p.getcountry())
print(people.getcountry())

class people2:
    country='china'
    @classmethod
    def getcountry(cls):
        return cls.country
    @classmethod
    def setcountry(cls,country):
        cls.country=country
p=people2()
print(p.getcountry())
p.setcountry('USA')
print(p.getcountry())


#######继承#################
class dog:
    def __init__(self,name,color='black'):
        self.name=name
        self.color=color
    def run(self):
        print('狗富贵,互相汪!!!')

class keji(dog):
    def set_name(self,name):
        self.name=name
    def eat(self):
        print('i m eating!')

科科=keji('科科')
print('名字为 %s' % 科科.name)
科科.eat()
科科.set_name('饭饭')
print('新狗名:%s' % 科科.name)
科科.run()

##########多继承#############
class a:
    def printa(self):
        print('aaaaaa')
class b:
    def printb(self):
        print('bbbbbbbb')
class c(a,b):
    def printc(self):
        print('cccccccc')
c1=c()
c1.printa()
c1.printb()
c1.printc()

########多态##########

class animal2:
    def jiao(self):
        print('aowu...')
    
class dog2(animal2):
    def jiao(self):
        print('gaga')

class cat2(animal2):
    def jiao(self):
        print('miao!')

def test2(s):
    s.jiao()
a2=animal2()
a2.jiao()

b2=dog2()
c2=cat2()

test(b2)
test(c2)

########装饰器###########
#在不修改原来代码情况下赋予函数新的功能
#计算一个函数的运算时间
import time
def 计算(func): 
    def zsq():
        starttime=time.time()
        func()
        endtime=time.time()
        use=endtime-starttime
        print('消耗的时间为%d' % use)
    return zsq
@计算
def func():
    print('hello')
    time.sleep(1)
    print('world!')
# f=func
# f()
func()

#######装饰器例子2##############
# def dec(func2):
#     def jisuan(a,b):
#         startime=time.time()
#         func2(a,b)
#         endtime=time.time()
#         use=endtime-startime
#         print('time is %d'% use)
#     return jisuan


# @dec
# def func2(a,b):
#     print('a+b=?')
#     time.sleep(1)
#     print('its',a+b)

# f=func2
# f(4,5)

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



    






    

