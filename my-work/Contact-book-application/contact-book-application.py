import json
import os
import re

WELCOME_TEXT="Welcome to Your Contact Book\n" \
        "Commands: add, view, search, delete, exit"
FILE_NAME="contacts.json"
print(FILE_NAME)

def read_contacts(file_name):
    while True:
        if os.path.exists(file_name):
            if os.path.getsize(file_name) == 0:
                return []
            else:
                with open(FILE_NAME,"r") as file:
                    data=json.load(file)
                    return data
        else:
            file = open(FILE_NAME,"w")
            json.dump([],file)
            file.close()
            continue

def enter_name():
    while True:
        name=input("Enter Name: ")
        if not any(char.isdigit() for char in name):
            name=name.title()
            return name
        else:
            print("Please Enter Only Alphabets")
            continue


class InvalidNumberError(Exception):
    def __init__(self,number,message="Number Must Contain 10 digits"):
        self.number = number
        self.message = message
        super().__init__(f"{message}: {number}")

def enter_number():
    while True:
        try:
            number=int(input("Enter Mobile Number: "))
            if len(str(number))!=10:
                raise InvalidNumberError(number)
            return number
        except ValueError:
            print("Please Entry Only Numeric Characters")
        except InvalidNumberError as e:
            print(e)
            
def enter_email():
    return  #pending

def add_contacts(file_name):
    name=enter_name()
    number=enter_number()
    email=input("Enter Email ID: ")
    new_contact={"Name":name,"Number":number,"Email":email}
    contacts=read_contacts(file_name)
    contacts.append(new_contact)

    with open(FILE_NAME,"w") as file:
        json.dump(contacts,file,indent=1)

def view_contacts(file_name):
    data=read_contacts(file_name)
    count = 1
    for contact in data:
        print(f"-----{count}-----")
        for key,value in contact.items():
            print(f"{key}: {value}")
        print()
        count +=1



def main():
    print(WELCOME_TEXT)
    while True:
        user_choice=input("Enter a Command: ")
        print()
        if user_choice.lower()=="add":
            add_contacts(FILE_NAME)
        elif user_choice.lower()=="view":
            view_contacts(FILE_NAME)
        elif user_choice.lower()=="search":
            # search_contact()
            return
        elif user_choice.lower()=="delete":
            # delete_contact()
            return
        else:
            continue
main()

