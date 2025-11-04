a=input("word: ")
b=input("character: ")
c=-1
for i in a:
    c+=1
    if b in i:
        print(c)
if b not in a:
    print(-1)
