import math
n=int(input())
b=int(math.sqrt(n))
for i in range(2,b+1):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("prime")
        
