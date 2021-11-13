m=int(input())
l=[]
for _ in range(m):
    ele=int(input())
    l.append(ele)
gender=input()
n=0
if(gender=='g'):
    for i in range(m):
        if(i%2!=0):
            n+=l[i]
    print(n)
else:
    for i in range(m):
        if(i%2==0):
            n+=l[i]
    print(n)
