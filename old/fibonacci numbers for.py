a=int(input("start: "))
b=int(input("End: "))
x=0
z=1
s=0
while a<=b:
    s=x+z
    print(s,end=" ")
    x=z
    z=s
    s=0
    a+=1
    
