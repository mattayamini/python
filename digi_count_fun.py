def digi_count(n):
    c=0
    while n:
        d=n%10
        if d==m:
            c+=1
        n=n//10
    return c
    
n,m=map(int,input().split())
print("🪔deepavali subhakankshalu🪔")
print(digi_count(n))
        
