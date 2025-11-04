a=int(input("start: " ))
b=int(input("End: "))
s=0
while a<=b:
    if a%2==0:
        s+=a
    a+=1
print("Sum of even: ",s)
