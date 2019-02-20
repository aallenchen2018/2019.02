#coding=utf-8
import csv
import pandas

with open(r'C:\GitHub\2019.02代码\练习\工作簿2.csv',encoding='utf-8') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)
    
    

with open(r'C:\GitHub\2019.02代码\练习\工作簿2.csv','w') as f2:
    file=csv.writer(f2,dialect='excel')
    file.writerow([1,2,3,4])
    file.writerow([5,6,7,8])

