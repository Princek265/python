
b=int(input("n: "))
x=0
z=0
s=0
for i in range(b):
    s=x+z
    z=s
    print(s,end=" ")
    if z==1:
        x=0
    else:
        x=z
    s=0
    if z==0:
        z=1
    
