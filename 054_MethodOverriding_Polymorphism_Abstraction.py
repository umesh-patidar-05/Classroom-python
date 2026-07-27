print("23/july/2026")




'''
class A:
    pass

class B(A):
    pass

obj1 = B()
print(isinstance(obj1, B))  #True
print(isinstance(obj1, A))  #True

obj2 = A()
print(isinstance(obj2, B))  #False
'''




'''
class A:
    pass

class B(A):
    pass

obj1 = B()
print(issubclass(B,A))  #True
'''




'''
class Parent:
    def calculation(self):
        print("parent calculation")

class Child(Parent):
    def calculation(self):
        print("child calculation")   

obj1 = Child()
obj1.calculation()         #child calculation
'''




'''
class Parent:
    def calculation(self):
        print("parent calculation")

class Child(Parent):
    def calculation(self):
        super().calculation()
        print("child calculation")   

obj1 = Child()
obj1.calculation() 
'''
# parent calculation
# child calculation




'''
class Employee:
    def salary(self, basic, bonus):
        print("Total salary ", basic + bonus)

class Manager(Employee):
    def salary(self,basic, bonus):
        print("Manager salary ", basic + bonus + 5000) 

obj1 = Manager()
obj1.salary(50000, 3000)  #Manager salary  58000          
'''




'''
class Bird:
    def fly(self):
        print("bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

objects = [Bird(), Airplane()]

for obj in objects:
    obj.fly()
'''
# bird can fly
# Airplane can fly



'''
print(len("abcd"))     #4
print(len([1,2,3,4]))  #4
print(len((10,20,30))) #3
'''



'''
print(10 + 20)       # 30
print("wel" +"come") # welcome
print(5 * 3)         # 15
print("wel" * 3)     # welwelwel
'''




'''
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def intrest(self):
        pass

obj = Bank()    
obj.intrest()  
'''
# TypeError: Can't instantiate abstract class Bank without an implementation for abstract method 'intrest'




'''
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def interest(self):
        print("SBI interest 8.0")

class HDFC(Bank):
    def add(self):
        print("adddd")        

obj = SBI()
obj.interest()  #SBI interest 8.0
'''



'''
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def interest(self):
        print("SBI interest 8.0")

class HDFC(Bank):
    def add(self):
        print("adddd")         
obj1 = HDFC()
obj1.add()
'''
# TypeError: Can't instantiate abstract class HDFC without an implementation for abstract method 'interest'




'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, r):
        self.r = r

obj = Circle(5)
print(obj.area())    # 78.5
'''





'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Square(Shape):
    def __init__(self, r):
        self.r = r

obj2 = Square(5)  #TypeError: Can't instantiate abstract class Square without an implementation for abstract method 'area'
'''





'''
from abc import ABC, abstractmethod
class Payment(ABC):
    abstractmethod
    def pay(self, amount):
        pass


class Upipay(Payment):
    def pay(self, amount):
        print("using upi",amount)    
    
class Netbanking(Payment):
    def pay(self, amount):
        print("using netbanking ", amount)

class Creditcard(Payment):
    def pay(self, amount):
        print("using creditcard", amount)

upi = Upipay()    
upi.pay(300)

net = Netbanking()
net.pay(400)

credit = Creditcard()
credit.pay(500)
'''
# using upi 300
# using netbanking  400
# using creditcard 500  







'''
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculatebonus(self):
        pass
    def display(self):
        print("Employee Name",self.name)
        print("Employee salary",self.salary)


class Manager(Employee):
    def calculatebonus(self):
        bonus = self.salary*0.20
        print("Manager bonus",bonus)


class Developer(Employee):
    def calculatebonus(self):
        bonus = self.salary*0.10
        print("Developer bonus",bonus)

obj = Manager("xyz",1000)
obj.calculatebonus()
obj.display()

obj1 = Developer("abc",1000)
obj1.calculatebonus()
obj1.display()
'''
# Manager bonus 200.0
# Employee Name xyz
# Employee salary 1000
# Developer bonus 100.0
# Employee Name abc
# Employee salary 1000





from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salry = salary

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def display1(self):
        pass

class Child(Employee):
    def display(self):
        print("display")

class Child1(Child):
    def display1(self):
        print("child1") 

obj = Child1("abc", 89999)             
obj.display()        
obj.display1()        

# display
# child1     