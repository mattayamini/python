def order(n):
    c,s,r,b,m,g=0,0,0,0,0,0
    while n:
        d=n%10
        n=n//10
        g+=1
        if(d>b):
            c+=1
            #printdesc(c)
            b=d
        elif(d<b):
            s+=1
            #printasc(s)
            b=d
        else:
            m+=1
    #print(c,s)
    
    #print(g)
    if(c==g):
        return 0
    if(s==g-1):
        return 1
    if(m<g):
        return -1

n=int(input())
print(order(n))
