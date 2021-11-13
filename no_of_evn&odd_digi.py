'''
def fun(n):
    e=0
    o=0
    while n:
        d=n%10
        n=n//10
        if d%2==0:
            e+=1
        else:
            o+=1
    print(e,o)
        

num=int(input())
fun(num)


******above prgm with global variables and through recursion***********
'''
ec=0
oc=0
def dc(n):
    global ec,oc
    if n==0:
        print(ec)
        return oc
    d=n%10
    if d%2:
        oc+=1
    else:
        ec+=1
    return dc(n//10)
n=int(input())
print(dc(n))
