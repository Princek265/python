def Odd_index_values():
    b=[]
    a=input("Enter string: ")
    for i in range(len(a)):
        if i%2!=0:
            b.append(a[i])
            
    return "".join(b)

print("odd index values are: ",Odd_index_values())
