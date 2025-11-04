c=0
a=int(input("num: "))
while c<1 :
    z=a%10
    x=a//10%10
    w=a//100%10
    s=a//1000
    print("reverse: %d%d%d%d"%(z,x,w,s))
    c+=1
