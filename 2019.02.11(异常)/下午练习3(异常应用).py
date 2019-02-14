def input_password():
    #1提示用户输入密码
    pwd=input('enter password')
    #2判断密码长度>=8,返回用户输入的密码
    if len(pwd)>8:
        return pwd
    #3如果密码长度<8,抛出异常(自定义一个异常)
    print('主动抛出异常')
    #1> 创建异常对象
    ex=Exception('密码长度不够')
    #2> 主动抛出异常
    raise ex

try:

    input_password()

except Exception as result:
    print(result)
