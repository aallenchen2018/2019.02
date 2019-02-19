#列表

s='apple12345'
'''
l=list(s)
l.reverse()
print(''.join(l))

#步长法

b=s[::-1]
print(b)

#d递归

def func(s):
    if len(s)<=1:
        return s
    else:
        return func(s[1:])+s[0]
result=func(s)
print(result)

#for index

def func(s):
    result=''
    max_index=len(s)-1
    for index,value in enumerate(s):
        result+=s[max_index-index]
    return result
re=func(s)
print(re)

'''
l=list(s)
l.reverse()
print(''.join(l))

b=s[::-1]
print(b)

def func(s):
    while 1:

        if len(s)<=1:
            return s
            
        else:
            return s[-1]+func(s[:-1])
result=func(s)
print(result)


