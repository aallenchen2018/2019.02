l=[1,2,3,4]
print(l.index(3))

#从值大到小排序
l.sort(reverse=True)
print(l)

#列表推导式
a=[1,2,3,4]
print([5*x for x in a])

print([[x,y] for x in range(3) for y in range(2)])

str="apple12345678tyuiopfghjkl"
str2=str[::-1]
print(str2)  