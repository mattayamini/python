def Big_count(n):
    b=0
    g=n
    while n:
        d=n%10
        n=n//10
        if(d>=b):
            b=d
    print(b)
    r=0
    while g:
        d1=g%10
        g=g//10
        if(b==d1):
            r+=1
    return r
n=int(input())
print(Big_count(n))
