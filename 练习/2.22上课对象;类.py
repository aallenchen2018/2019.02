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

########



    

