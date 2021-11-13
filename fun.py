"""def fun(n):
    if n==1:
        print(n)
        return
    fun(n-1)
    print(n)
fun(8)
"""
def fun(n):
    if n==0:
        #print(n)
        return 0
    return n+fun(n-1)
print(fun(5))
