"""
56 65 16 87 98 78

<35 fail          F
>=75 distinction  O
>=60 first        A
>=50 second       B
>=35 third        C

sub1 56 100 B
sub2 65 100 A
sub3 16 100 F
                                                                                                                                                                                                                                                               
total:350  per:67%   grade:Fail   bc=1
"""
a,b,c,d,e,f=map(int,input().split())
bc=0
if(a>=75 and a<=100):
    print("sub1 ", a,"/100\tgrade:O")
elif(a>=60 and a<75):
    print("sub1 ", a,"/100\tgrade:A")
elif(a>=50 and a<60):
    print("sub1 ", a,"/100\tgrade:B")
elif(a>=35 and a<50):
    print("sub1 ", a,"/100\tgrade:C")
else:
    print("sub1 ", a,"/100\tgrade:F")
    bc+=1
   
if(b>=75):
    print("sub2 ", b,"/100\tgrade:O")
elif(b>=60):
    print("sub2 ", b,"/100\tgrade:A")
elif(b>=50):
    print("sub2 ", b,"/100\tgrade:B")
elif(b>=35):
    print("sub2 ", b,"/100\tgrade:C")
else:
    print("sub2 ", b,"/100\tgrade:F")
    bc+=1

if(c>=75):
    print("sub3 ", c,"/100\tgrade:O")
elif(c>=60):
    print("sub3 ", c,"/100\tgrade:A")
elif(c>=50):
    print("sub3 ", c,"/100\tgrade:B")
elif(c>=35):
    print("sub3 ", c,"/100\tgrade:C")
else:
    print("sub3 ", c,"/100\tgrade:F")
    bc+=1

if(d>=75):
    print("sub4 ", d,"/100\tgrade:O")
elif(d>=60):
    print("sub4 ", d,"/100\tgrade:A")
elif(d>=50):
    print("sub4 ", d,"/100\tgrade:B")
elif(d>=35):
    print("sub4 ", d,"/100\tgrade:C")
else:
    print("sub4 ", d,"/100\tgrade:F")
    bc+=1

if(e>=75):
    print("sub5 ", e,"/100\tgrade:O")
elif(e>=60):
    print("sub5 ", e,"/100\tgrade:A")
elif(e>=50):
    print("sub5 ", e,"/100\tgrade:B")
elif(e>=35):
    print("sub5 ", e,"/100\tgrade:C")
else:
    print("sub5 ", e,"/100\tgrade:F")
    bc+=1

if(f>=75):
    print("sub6 ", f,"/100\tgrade:O")
elif(f>=60):
    print("sub6 ", f,"/100\tgrade:A")
elif(f>=50):
    print("sub6 ", f,"/100\tgrade:B")
elif(f>=35):
    print("sub6 ", f,"/100\tgrade:C")
else:
    print("sub6 ", f,"/100\tgrade:F")
    bc+=1

total=a+b+c+d+e+f
print("Total:",total)
per=(total/600)*100
print("Percentage:",per)
if(per>=75 and bc==0):
    print("Grade:O")
elif(per>=60 and per<75 and bc==0):
    print("Grade:A")
elif(per>=50 and per<60 and bc==0):
    print("Grade:B")
elif(per>=35 and per<50 and bc==0):
    print("Grade:C")
else:
    if(bc>=1):
        print("Grade:F")

print("bc=",bc)
