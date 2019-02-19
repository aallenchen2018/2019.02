# 1.设计一个小程序，需求如下：
# 定义一个很长的字符串，如：
str="apple12345678tyuiopfghjkl"
# 把该字符串按照反向的顺序打印出来，结果如下：
# lkjhgfpoiuyt87654321elppa
# a.通过reverse()的方法
str=list(str)
str.reverse()
print(str)

# b.不通过reverse()的方法
str2=str[::-1]
print(str2)
# 2.通过列表方式实现：
#     1. 提示用户输入内容，如果为空则提示！
enter=input('请输入东西')
if len(enter)==0:
    print('!!!')
#     2. 判断用户输入的字符串首字母是否为元音（A、E、I、O、U）
#     3. 如果为元音，则在字符串后加上'ay'
#         eg. 如果用户输入'apple'->'appleay'
#     4. 如果首字母为辅音字母，则将该字符串首字母移动结尾，并加上'ay'
#         eg. 如果用户输入'hello'->'ellohay'。
# 3.创建一个列表，包含学员名字，接受键盘输入，输入学员名称，判断名称是否存在于列表中，
# 如果存在，打印名字已经存在列表中，如果不存在，则添加信息到列表中，并且打印已经添加新信息
slist=[]
sname=input('please enter sname')
if sname in slist:
    print(sname,'存在')
else:
    slist.append(sname)
    print(slist)