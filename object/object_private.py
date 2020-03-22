#private vairable __variable. 
#can only be accessed from inside of class
# use get and set method
#@property 


class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    def __str__(self):
        return "{} is a {} years old {}".format(self.__name, self.__age, self.__gender)

    def setName(self, name):
        self.__name = name
        

    def getName(self, name):
        print(self.__name)

    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print("wrong age")

    def getAge(self, name):
        print(self.__age)

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self, name):
        print(self.__gender)

    @property
    def age(self):
        return self.__age

    @age.setter 
    def age(self, age):
        self.__age = age

   

p = Person("Lily",20,'Female')
print(p)
p.age = 35
print(p)

