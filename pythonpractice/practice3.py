a=1
b=2
c=3

def sum_function():
    print(a+b)
    print(b+c)
    print(c+a)

sum_function()
#一般的にこのような使い方は好ましくない

def sum_function2(d=4,e=5,f=6):
    print(d+e)
    print(e+f)
    print(f+d)

sum_function2()
#使い方としてはこちらがベター