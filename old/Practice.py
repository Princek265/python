print("1. Write a program to check if a person is eligible to vote. Assume the minimum voting age is 18.\n")
def Vote():
    age=int(input("Enter Age: "))
    if age>=18:
        print("Eligible for vote")
    else:
        print("Not eligible for vote")
    

print("2. Write a program that takes marks of a student as input and checks if the student has passed or failed. Assume the passing mark is 40.\n")
def PF():
    marks=int(input("Enter Marks: "))
    if marks>=40:
        print("Pass")
    else:
        print("Fail")
    

print("3. Write a program that takes two numbers as input and prints the larger number.\n")
def greater():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    if num1>num2:
        print("%d Greater than %d"%(num1,num2))
    else:
        print("%d Greater than %d"%(num2,num1))
    

print("""4. Write a program that takes marks as input and assigns a grade based on the following criteria:
• Marks >= 90: Grade A
• Marks >= 80: Grade B
• Marks >= 70: Grade C
• Marks >= 60: Grade D
• Marks < 60: Fail\n""")

def Grading():
    marks=int(input("Enter Marks: "))
    if marks>=90:
        print("Grade A")
    elif marks>=80:
        print("Grade B")
    elif marks>=70:
        print("Grade C")
    elif marks>=60:
        print("Grade B")
    elif marks<60:
        print("Fail")

    
print("""5. Write a program that reads a number and categorizes it as "Negative", "Zero", or "Positive" using if-elif-else.\n""")
def Zenepo():
    num=int(input("Num: "))
    if num>0:
        print("Positive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")
    
print("""6. Write a program that takes two numbers and a choice (1 for addition, 2 for subtraction, 3 for
    multiplication, 4 for division) from the user and performs the corresp  onding operation.\n""")

def Cal():
    
    a=int(input("Num1: "))
    b=int(input("Num2: "))
    c=int(input("Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division\n\nEnter Choice:"))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(a/b)
    else:
        pass

print("""7. Write a program that checks if a given year is a leap year or not using if-elif-else.
    A year is a leap year if it is divisible by 4 but not by 100, except when it is divisible by 400\n""")
def Leap():
    year=int(input("Enter Year: "))
    if year%4==0 and year%100!=0 or year%400==0:
        print("%d is a Leap year"%(year))
    else:
        print("%d is not a Leap year"%(year))


X=int(input(""" Enter Code Number: """))

if X==1:
    Vote()
elif X==2:
    PF()
elif X==3:
    greater()
elif X==4:
    Grading()
elif X==5:
    Zenepo()
elif X==6:
    Cal()
elif X==7:
    Leap()
else:
    print()
