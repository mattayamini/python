def form(n):
    e=0
    o=0
    r,s=0,0
    while n:
        d=n%10
        n=n//10             #0*1+4  4
        if(d%2==0):         #2*10+4  24
            e=e+d*10**r     #6*100+24 624
            r+=1
        else:
            o=o+d*10**s
            s+=1         
    print(e,o)


n=int(input())
form(n)
