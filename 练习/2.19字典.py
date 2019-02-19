dic={'小明':'123'}
键=dic.keys()
count=3

while 1:
    username=input('请输入用户')
    if username in 键:
        while count>=0:
            pwd=input('请输入密码')
            if pwd==dic[username]:
                print('密码对了')
                break
            else:
                print('密码错了')
                count-=1
                print('你还有%d次机会'%count)
        print('你的次数没有了')
        break
    else:
        print('用户名错了')
