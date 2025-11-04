class dog:
    def __init__(self, name ,age): 
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    
d = dog("Roku",2) #object  or instance of of a class
d.set_age(int(input("Enter age of the dog: ")))
age=d.get_age()
print(age)