"""
Whenever there are similar properties in multiple classes
create a general class for those general (same) properties
then make the classes inherit from it
"""



class Pet:  # A general class which have common stuff in it to reduce redundancy
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I dont know what to say")

class Dog(Pet): # Inheriting from general class which gives access to its resources
    def speak(self): # Due to this we dont have to write code for name and age for both classes separatly
        print("Bark")

class Cat(Pet):
    def __init__(self,name,age,colour):
        super().__init__(name,age)
        self.colour = colour
        """
        Instead rewriting self.name = name and self.age = age
        We can just use super() function which refers to the super class or the class we inherit from
        then we can write the name of the method/function to get the values from them

        """

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.colour}.")

    def speak(self):
        print("meow")

class Fish(Pet):
    def speak(self):
        print("ghok ghok ghok ghok")
        
p = Pet("Tom",22)
p.show()
p.speak()
c = Cat("Butch",11,"Black")
c.show()
c.speak()
d = Dog("Roku",12)
d.show()
d.speak()
f = Fish("Guss",6)
f.show()
f.speak()