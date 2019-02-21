import csv
with open(r'C:\GitHub\2019.02代码\练习\工作簿3.csv','r') as f:
    #用全球变量定义file
    global file
    #让它成为list
    file=[]
    reader=csv.reader(f)
    #将文件添加进list
    for i in reader:
        i=''.join(i)
        file.append(i)
    print(file)

def mod():
    name=input('请输入名字')
    num=(input('请输入学号'))
    #当有这个名字的时候删除名字学号,
    #这里用了 del list[] 和list.index()这两个函数
    if name in file:
        del file[file.index(name)]
    #当没有名字的时候添加名字和学号,
    #这里用了list.insert(index,内容)这个函数
    elif name not in file:
        add=name+' '+num
        file.insert(0,add)
        

# with open(r'C:\GitHub\2019.02代码\练习\工作簿2.csv','w') as f2:
#     write=csv.writer(f2,dialect='excel')
#     write.writerow(file)

    



#1.删除功能
# def delete1():
#     name=str(input('请输入要删除的名字:'))
#     with open(r'C:\GitHub\2019.02代码\练习\工作簿3.csv','w') as d:
#         file=csv.writer(d,dialect='excel')
#         reader=csv.reader(d)
#         for i in reader:
#             file.writerow([234,33])
    
# delete1()
# #3.新增
# name3=input('请输入新增的用户名:')
# num3=input('请输入新增的号码: ')
# with open(r'C:\GitHub\2019.02代码\练习\工作簿2.csv','w') as x:
#         file=csv.writer(x,dialect='excel')
#         reader=x.readlines()
#         for p in reader:
#                 p=p.strip('\n')
#                 p=p.split(',')
#                 file.writerow(p)
#         pd=[name3,num3]
#         file.writerow(pd)