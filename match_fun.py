def match(n):
    while n:
        d=n%10
        if d==m:
            return True
        else:
            n=n//10
    return False
    
n,m=map(int,input().split())
print(match(n))
    
