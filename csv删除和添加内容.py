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
    num=input('请输入学号')
    add=name+' '+num
    #当有这个名字学号的时候删除名字学号,
    #这里用了 del list[] 和list.index()这两个函数
    if add in file:
        del file[file.index(add)]
    #当没有名字学号的时候添加名字和学号,
    #这里用了list.insert(index,内容)这个函数
    elif add not in file:       
        file.insert(0,add)
#运行函数，然后将file导回csv文件      
mod()
with open(r'C:\GitHub\2019.02代码\练习\工作簿3.csv','w') as f2:
    w=csv.writer(f2,dialect='excel')
    w.writerow(file)