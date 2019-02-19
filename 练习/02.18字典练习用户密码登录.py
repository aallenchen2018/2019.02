dic={'futian':'123','nanshan':'234'}
count=3
a=dic.keys()
while 1:
    username=input('please enter your name')
    if username in a:
        while count>0:
            pwd=input('please enter your passwd')
            if pwd==dic[username]:
                print('correct')
                break
            else:
                print('wrong passwd')
                count-=1
                print('your have %d chance to try' % count)
        print('你的次数没有了')
        break
    else:
        print('please enter right username.')

