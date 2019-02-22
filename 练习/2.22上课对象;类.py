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

