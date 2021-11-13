a,b=map(int,input().split())
while a!=1:
    if a==b:
        print('true')
        break
    #print(n,end=" ")
    if a%2:
        a=a*3+1
    else:
        a=a//2
    if a==b:
        print('true')
        break
else:
    print('false')
          
 
