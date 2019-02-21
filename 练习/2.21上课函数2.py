# def report():
#     x=int(input('enter x'))
#     y=int(input('enter y'))
#     re1=int((x+1)/y)
#     re2=int(x+y)
#     return re1,re2

# while True:
#     result=report()
#     print(result)

# def ret(a,b):
#     a*=10
#     b*=10
#     return a,b
# num=ret(5,7)
# print(num)
# print(type(num))

# num1,num2=ret(30,50)
# print(num1,num2)


# 函数的传递
def print_name(pet1='科科',pet2='饭饭',*arg):
    print('pet2 is %s, pet1 is %s;%s'%(pet2,pet1,arg))

print_name('keke','fanfan','喜欢打架')
print_name()
print('*'*16)
def print_name2(pet1='科科',pet2='饭饭',**arg):
    print('pet2 is %s, pet1 is %s;%s'%(pet2,pet1,arg))

print_name2('keke','fanfan',城市='深圳')

def print_name3(pet1='科科',pet2='饭饭',*arg):
    print('pet2 is %s, pet1 is %s;%s'%(pet2,pet1,arg))

print_name3('keke','fanfan',"城市='深圳'")


