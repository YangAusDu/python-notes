
#class method  
# 1.@classmethod 
# 2.parameter is a class 
# 3.class methods are independent from objects.
# 4.can you run function in class method?:  NO

#Use of class method
#actions that needs to be done before the creation of object.

class Dog:

    __tag = 101

    def __init__(self, name):
        self.name = name
        

    def run(self):
        print("{} is running {}".format(self.name, Dog.__tag))
        pass

    def eat(self):
        print("{} is eatting".format(self.name))
        self.run() #need a self. ahead

    @classmethod
    def update_tag(cls, tag):   #cls = class  self is no needed
        cls.__tag = tag
        print("New tag: ", cls.__tag)
        pass


d1 = Dog("d1")
d1.run()
Dog.update_tag(99)
d1 = Dog("d2")
d1.run()