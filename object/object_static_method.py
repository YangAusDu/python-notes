'''
#1. @staticmethod  very much like class method
#2. no parameter like clf or self for static method
#3. only visit class attribute
# 
# '''


class Dog:
    
    __tag = 101   #private variable

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

    @staticmethod
    def print_tag():
        print("static method: ", Dog.__tag)
        pass


d1 = Dog("d1")
d1.run()
Dog.update_tag(99)
Dog.print_tag()
d1 = Dog("d2")
d1.run()