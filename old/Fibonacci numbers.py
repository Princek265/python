#a=int(input("start: " ))
b=int(input("End: "))
x=1
z=0
s=0
for i in range(0,b+1):
    s=x+z
    x=z
    z=s
    print(s,end=" ")
    s=0
