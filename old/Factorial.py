i=int(input("Factorial: "))
p=1
for a in range(1,i+1):
    p*=a
print("By For loop")
print(p)
x=1
z=1
n=int(input("Factorial: "))
while x<=n:
   z*=x
   x+=1
print("While")
print(z)
