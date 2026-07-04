print("3/july/2026")




'''
class Test:
    a=10
    def __init__(self):
        print(self.a)  #10
t1=Test()
print(t1.__dict__)  #{}
'''




'''
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

t1=Test()
t2=Test()
del t1.c
del t2.b

print(t1.__dict__)  # {'a': 10, 'b': 20}
print(t2.__dict__)  # {'a': 10, 'c': 30}
'''




'''
def get_marks(self):
    return self.marks
'''


'''
def set_marks(self,marks):
    self.marks = marks
'''



'''
class Student:
    def setmarks(self,marks):
        self.marks = marks

    def getmarks(self):
        return self.marks
    
s1 = Student()
s1.setmarks(80)
print(s1.getmarks())  #80
'''




'''
class Student:
    college = "NIT"
    def __init__(self,name):
        self.name = name

    @classmethod
    def change_college(cls,new):
        cls.college = new

s1 = Student("deepika")
print(s1.name)    #deepika
print(s1.college)   #NIT
Student.change_college("IIT")
print(s1.college)   #IIT           
'''




'''
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    
c1 = Calculator()
print(c1.add(10,20))  #30
print(Calculator.add(10,20))  #
print(c1.__dict__)  #{}
print(Calculator.__dict__)  #{'__module__': '__main__', '__firstlineno__': 85, 'add': <staticmethod(<function Calculator.add at 0x0000020A5D933530>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Calculator' objects>, '__weakref__': <attribute '__weakref__' of 'Calculator' objects>, '__doc__': None}
'''




'''
class Demo:
    a = 10
    @staticmethod
    def display():
        print(a) #NameError: name 'a' is not defined

c1=Demo()
c1.display()
'''



'''
class Demo:
    a = 10
    @staticmethod
    def display():
        print(Demo.a)  #10

c1=Demo()
c1.display()
'''



'''
class Demo:
    a=10
    @staticmethod
    def display(self):
        print()

c1 = Demo()
c1.display()   #TypeError: Demo.display() missing 1 required positional argument: 'self'
'''




class Student:
    college = "IIT"
    def set(self,name):
        self.name = name
    @staticmethod
    def display(x):
        print(Student.college)  #IIT
        #print(name)  #NameError: name 'name' is not defined
        #print(self.name)  #NameError: name 'self' is not defined
        print(x.name)  #deepika

c1 = Student()
c1.set("deepika")
c1.display(c1)