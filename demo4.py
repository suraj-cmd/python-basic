class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfun(self):
        print("hello my name is " + self.name)
p1 = Person("john",36)
p1.myfun()
