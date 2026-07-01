print("01/july/2026")

'''
class Employee:
    def hello(self):
        print("hello from employee")

e1=Employee()
e1.hello()
print(type(e1))        
'''
# hello from employee
# <class '__main__.Employee'>



'''
class Student:
    def set(self):
        print("set is called")
    def display(self):
        print("display is called")

s1=Student()
s1.set()
s1.display()   
'''
# set is called
# display is called





'''
class Student:
    def set(self):
        print("set is called")
        self.id=101
        self.name="deepika"
        self.address="chennai"

    def display(self):
        print("display is called") 
        print("ID is",self.id)
        print("Name is",self.name)
        print("Address is",self.address)

s1=Student()
s1.set()
s1.display()

s2=Student()
s2.set()
s2.display()
'''
# set is called
# display is called
# ID is 101
# Name is deepika
# Address is chennai
# set is called
# display is called
# ID is 101
# Name is deepika
# Address is chennai




'''
class Student:
    def set(self,id,name,address):
        print("set is called")
        self.id=id
        self.name=name
        self.address=address

    def display(self):
        print("display is called")
        print("ID is",self.id)    
        print("Name is",self.name)    
        print("Address is",self.address)

s1=Student()
s1.set(101, "deepika", "chennai")
s1.display()

s2=Student()
s2.set(102, "rashmika", "hyd")
s2.display()
'''
# set is called
# display is called
# ID is 101
# Name is deepika
# Address is chennai
# set is called
# display is called
# ID is 102
# Name is rashmika
# Address is hyd




'''
class Student:
    def set(self,id,name,address):
        print("set is called")
        self.id=id
        name=name
        self.address=address

    def display(self):
        print("display is called")
        print("ID is",self.id)    
        print("Name is",name)    
        print("Address is",self.address)

s1=Student()
s1.set(101, "deepika", "chennai")
s1.display()
'''
# NameError: name 'name' is not defined






'''
class Addition:
    def set(self,a,b):
        print("set called")
        self.a = a
        self.b = b

    def add(self):
        print("add called")    
        self.c=self.a+self.b

    def display(self):
        print("display called")
        return self.c

a1=Addition()
a1.set(10,20)
a1.add()
result=a1.display()
print(result)        
'''
# set called
# add called
# display called
# 30




'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name ",self.name,"and age is",self.age)    

s1=Student("deepika",30)
s1.display()        
'''
#Name  deepika and age is 30





class Student:
    def __init__(self):
        print("default constuctor")
        self.name="deepika"
        self.age=30

    def display(self):
        print("Name",self.name,"and age is",self.age)    

s1=Student()
s1.display()        

s2=Student()
s1.display()

# default constuctor
# Name deepika and age is 30
# default constuctor
# Name deepika and age is 30