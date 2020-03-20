
#__init__ initialization

#__new__ instantiation

#__call__ call as a function

#__del__ deletion of reference

import sys


class Person:
    def __init__(self, name):
        self.name = name
        print("INIT")

    def __new__(cls, *args, **kwargs):   #*args <class tuple>  *kargs< dict>  making space for __init__
        print("NEW")
        position = object.__new__(cls)#, *args, **kwargs)
        print("posiiton: ",position)
        return position
    
    def __call__(self, name):
        print("CALL")
        self.name = name

    def __del__(self):
        print("DEL")

# p = Person("Peter")
# print(p.name)
# p("Lily")  # run __call  when you run object as a function
# print(p.name)

p1 = Person("Ada")
p2 = p1              #all p1 p2 p3 pointing to the same address
p3 = p1              # when a address has no reference/the program has reached its end, del would be excuted automatically by default               
#print(sys.getrefcount(p1))
#del p3
#del p2
#print(p2)