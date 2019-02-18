
def abc():

    global 总额
    上班天数=int(input('enter workday'))
    加班天数=int(input('enter over bussiness day'))

    日薪=月薪/22.5
    加班日薪=日薪*1.5
    总额=日薪*上班天数+加班天数*加班日薪
    if 上班天数<10:
        print('no payment')
        
    else:
        
        print(总额)



月薪=int(input('enter month Payment'))
if 5000<月薪 and 月薪<10000:
    
    abc()
    总额=总额*0.9-666

elif 10000<月薪<20000:
    abc()
    总额=总额*0.8

else:
    abc()
    总额=总额*0.7
