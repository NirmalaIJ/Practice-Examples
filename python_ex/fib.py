""" 18th fib """

""" n=18

a, b= 0, 1
for i in range(3, 19):
    c = a+ b
    print(c)
    a, b = b, c
print(c)


 """
""" n = 2
def fib(a, b):
    global n
    global c
    c =a + b
    
    while(n<19):
        print(c)
        n+=1
        a, b = b, c
        fib(a, b)
    return c
print(fib(0,1))
 """

def fib(n):
    if n ==0 or n== 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
    
print(fib(5))    
