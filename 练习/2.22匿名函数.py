#lambda 有自己的命名空间

sum=lambda x,y:x+y
print(sum(6,8))

stu=[{'name':'tb','num':34},{'name':'med','num':69},{'name':'xiaoyu','num':21}]

print(type(stu))
print(sorted(stu,key=lambda x:x['num'],reverse=True))



# def operation(x,y,opt):
#     re=opt(x,y)
#     return re
# num1=int(input('num1?'))
# num2=int(input('num2?'))
# result=operation(num1,num2,lambda x,y:x+y)
# print(result)

def operation(x,y)

