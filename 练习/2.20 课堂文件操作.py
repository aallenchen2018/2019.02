
def file(file_path):
    with open(file_path,'w') as f:
        f.write('buting ! 110')
        f.close()
    

file(r'C:\GitHub\2019.02代码\练习\测试.txt')
file(r'C:\GitHub\2019.02代码\练习\测试2.txt')




# with open(r'C:\GitHub\2019.02代码\练习\测试.txt','w') as f:
#         f.write('buting !')

file=open(r'C:\GitHub\2019.02代码\练习\测试.txt','r')
for i in file.readlines():

    i=i.strip('\n')
    a=i.split(' ')
    if a[-1]=='110':
        print('tel is here!')
file.close()
