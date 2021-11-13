def Big_count(n):
    c=0
    b=0
    while n:
        d=n%10
        n=n//10
        if(d>b):
            b=d
            c=0
        if b==d:
            c+=1
    return c
    
n=int(input())
print(Big_count(n))
        
