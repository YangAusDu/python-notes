

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{} is eating".format(self.name))
    
    def run(self):
        print("{} is running".format(self.name))

    def sleep(self):
        print("{} is sleeping".format(self.name))

class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid
    
    def __str__(self):
        return "{}   {}    {}".format(self.name, self.age, self.sid)

    def study(self):
        print("{} is studying".format(self.name))
        

s = Student("Lily", 10, 10082)
s.study()
print(s)


