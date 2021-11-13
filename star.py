n=int(input())
s='*'
a=' '
n1=n-2
for i in range(1,n):
    print(a*n1,end='')
    print(i*s)
    n1-=1
