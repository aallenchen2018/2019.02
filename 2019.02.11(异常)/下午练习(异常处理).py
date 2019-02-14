#捕获异常
while 1:
    try:
        num=int(input('please enter a num'))
        num2=num/2
        print(num2)


    except ZeroDivisionError:

        print('please not use 0')
     
        pass

#捕获未知异常
    except Exception as result:
        print('未知错误 %s '% result)

    else:
        print('没有异常')

    finally:

        print('无论有没有异常,都会执行的代码')


