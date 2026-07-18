print("08/july/2026")



'''
class Myclass:
    x = 10
print(type(Myclass))  #<class 'type'>
'''




'''
class Student:
    name = "deepika"
Student.age = 30
s1 = Student()
print(s1.name) #deepika
print(s1.age) #30
'''





'''
class Student:
    name = "deepika"
Student.age = 30
s1 = Student()
del Student.age
print(s1.age) #AttributeError: 'Student' object has no attribute 'age'
'''




'''
class Student:
    name = "deepika"
Student.age = 30
s1 = Student()
del s1
print(s1.name) #NameError: name 's1' is not defined
'''




'''
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def displayname(self):
        print("name is", self.name)

    def displaymarks(self):
        print("marks",self.marks)

    def displayall(self):
        self.displayname()
        self.displaymarks()

s1 = Student("deepika", 90)        
s1.displayall()
'''
# name is deepika
# marks 90





'''
class Student:
    def __init__(self,name):
        self.name = name
        self.marks = 0

    def set_marks(self, marks):
        self.marks = marks
        return self
    
    def hello(self):
        print("heyyy",self.name)
        return self
    
    def display(self):
        print("marks",self.marks)
        return self

s1 = Student("deepika")
s1.hello().set_marks(80).display()
'''    
# heyyy deepika
# marks 80    





'''
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("umesh")
print(s1.name)  #umesh
'''




'''
class Student:
    def __init__(self, name):
        self._name = name

s1 = Student("deepika")
print(s1._name)   #deepika
'''




'''
class Student:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

s1 = Student("deepika", 500000)
print(s1.name)  #deepika
'''
    




'''
class Student:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

s1 = Student("deepika", 500000)
print(s1.__salary)  #AttributeError: 'Student' object has no attribute '__salary'
'''




'''
class Student:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

s1 = Student("deepika", 500000)
print(s1.name)  #deepika
print(s1._Student__salary) #500000
'''





'''
class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_salary(self):
        return self.__salary 

    def set_salary(self, salary):
        if salary > 1000:
            self.__salary = salary      
        else:
            print("invalid salary")

    def get_name(self,):
        return self.__name        

    def set_name(self, name):
        if name.strip() != "":
            self.__name = name
        else:
            print("name cannot be empty")

s1 = Employee(101, "deepika", 500000) 
print(s1.get_id())               
print(s1.get_name())               
print(s1.get_salary())               
'''
# 101
# deepika
# 500000




'''
class Student:
    def __init__(self):
        self.__salary = 100000

s1 = Student()
print(s1.__salary)   #AttributeError: 'Student' object has no attribute '__salary'     
'''




'''
class Student:
    def __init__(self):
        self.__salary = 100000

s1 = Student()
print(s1._Student__salary)
'''





class Bankbalance:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, money):
        self.__balance = self.__balance + money

    def withdrawl(self, money):
        if money > self.__balance:
            print("No sufficient balance")
        else:
            self.__balance = self.__balance - money

c1 = Bankbalance()
c1.set_balance(10000)
print(c1.get_balance())
c1.deposit(5000)
print(c1.get_balance())
c1.withdrawl(500)
print(c1.get_balance())

# 10000
# 15000
# 14500



