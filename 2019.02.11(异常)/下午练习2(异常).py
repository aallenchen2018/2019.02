#异常传递(一次性解决异常)利用异常的传递性,在主程序捕获异常.  虽然主程序的错误是有上级引起的,但是我们只要在主程序搞异常捕获就行


def demo1():
    return int(input('enter num:   '))

def demo2():
    return demo1()

try:

    print(demo2())
except Exception   as result:
    print('错误位置 %s' % result)

