# class Person:

#     number_of_people = 0

#     def __init__(self,name):
#         self.name = name
#         Person.number_of_people+=1

# p1 = Person("Piko")
# print(p1.number_of_people)

# p2 = Person("Roko")
# print(p2.number_of_people)


class Person:

    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()
    
    @classmethod # with @classmethod we can directly call the method/function from the class withoud any object or an instance 
                 # it also has access to the things in the class and it can change things in the class
                 # similar behavior to functions in C which change the values at actual addresses and make change
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1




p1 = Person("Piko")
p2 = Person("Roko")
print(Person.number_of_people_())