a,b=map(int,input().split())
for i in range(1,b):
    if a==1:
        print(-1)
        break
    if a%2:
        a=a*3+1
    else:
        a=a//2
    if a==1 and i!=b-1:
        if i==b:
            print(a)
        else:
            print("-1")
            break
else:
    print(a)
