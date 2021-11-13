'''
def fun(n):
    c=0
    while n:
        d=n%10
        n=n//10
        c+=1
    return c
        

num=int(input())
res=print(fun(num))



above prgm with ****recursionssssssss


def fun(n):
    if n==0:
        return 0
    return 1+fun(n//10)
n=int(input())
print(fun(n))
    '''

def fun(n):
    if n==0:
        return 0
    return n%10+fun(n//10)
n=int(input())
print(fun(n))
