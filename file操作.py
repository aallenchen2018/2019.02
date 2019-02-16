# file=open('readme.txt',encoding='gbk')
# i=file.read()
# print(i)
# file.close

# file=open('readme.txt','a')
# file.write('不听不听')
# file.close

# with open('readme.txt',encoding='gbk') as f:
#     print(f.readlines())

# file=open('readme.txt',encoding='gbk')
# while 1:
#     text=file.readline()
#     #判断是否能读取内容,如果不能,就终止
#     if not text:
#         break

#     print(text)
# file.close


#复制文件到另一个
def copy():

    file_read=open('readme.txt')
    file_write=open('readme复件.txt','w')

    cont=file_read.read()
    file_write.write(cont)

    file_read.close()
    file_write.close()

# copy()

#用读取大文件,用循环来减少内存压力
def read():
    file_read=open('readme.txt')
    while 1:
        text=file_read.readline()
        if not text:
            break
        print(text)
    file_read.close

# read()

        

