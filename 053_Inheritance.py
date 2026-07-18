print("10/july/2026")




'''
class Parent:
    def fun1(self):
        print("this is parent")

class Child(Parent):
    def fun2(self):
        print("this is child") 

obj = Child()
obj.fun1()               
obj.fun2()               
'''
# this is parent
# this is child






'''
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def showrole(self):
        print(self.name,"is a employee")

obj = Employee("deepika")
obj.showrole()                
'''
# deepika is a employee





'''
class Grandparent:
    def fun1(self):
        print("from grandparent")

class Parent(Grandparent):
    def fun2(self):
        print("from parent")

class Child(Parent):
    def fun3(self):
        print("from child")                

obj = Child()
obj.fun1()        
obj.fun2()        
obj.fun3()        
'''
# from grandparent
# from parent
# from child




'''
class Person:
    def __init__(self):
        print("person constructor is called")

class Employee(Person):
    def __init__(self):
        print("employee constructor is called")

emp = Employee()                
'''
# employee constructor is called







'''
class Person:
    def __init__(self):
        print("person constructor is called")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("employee constructor is called")

emp = Employee()  
'''
# person constructor is called
# employee constructor is called






'''
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("person constructor is called")

class Employee(Person):
    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary
        print("Employee consructor")


emp = Employee("deep", 30, "mumbai", 90000)
print(emp.name)
print(emp.age)            
print(emp.address)            
print(emp.salary)            
'''
# person constructor is called
# Employee consructor
# deep
# 30
# mumbai
# 90000







'''
class Person:
    def show(self):
        print("person")

class Child(Person):
    def show(self):
        super().show()
        print("child")

c = Child()
c.show()                
'''
# person
# child






'''
class Father:
    def house(self):
        print("father has house")

class Mother:
    def laptop(self):
        print("mother has laptop")  

class Child(Father, Mother):
    def nothing(self):
        print("child has nothing")

c = Child()                      
c.house()
c.laptop()
c.nothing()    
'''
# father has house
# mother has laptop
# child has nothing





'''
class Father:
    def house(self):
        print("father has house")

    def laptop(self):
        print("father has laptop")    

class Mother:
    def laptop(self):
        print("mother has laptop")  

class Child(Father, Mother):
    def nothing(self):
        print("child has nothing")

c = Child()                      
c.house()
c.laptop()
c.nothing()    
'''
# father has house
# father has laptop
# child has nothing





'''
class Father:
    def house(self):
        print("father has house")

    def laptop(self):
        print("father has laptop")    

class Mother:
    def laptop(self):
        print("mother has laptop")  

class Child(Mother, Father):
    def nothing(self):
        print("child has nothing")

c = Child()                      
c.house()
c.laptop()
c.nothing()    
'''
# father has house
# mother has laptop
# child has nothing





'''
class Father:
    def __init__(self):
        print("father constructor")

class Mother:
    def __init__(self):
        print("mother constructor")

class Child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("child constructor")

c = Child()        
'''                
# father constructor
# child constructor






'''
class Father:
    def __init__(self):
        print("father constructor")

class Mother:
    def __init__(self):
        print("mother constructor")

class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        print("child constructor")

c = Child()
'''
# mother constructor
# child constructor






'''
class Father:
    def show(self):
        print("father show method constructor")

class Mother:
    def show(self):
        print("mother show method constructor")        

class Child(Father, Mother):
    def show(self):
        super().show()        
        print("child show")

c = Child()
c.show()        
print(Child.mro())
'''
# father show method constructor
# child show
# [<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]






'''
class Father:
    def show(self):
        print("father show method constructor")

class Mother:
    def show(self):
        print("mother show method constructor")        

class Child(Mother, Father):
    def show(self):
        super().show()        
        print("child show")

c = Child()
c.show()        
print(Child.mro())
'''
# mother show method constructor
# child show
# [<class '__main__.Child'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>]






'''
class Person:
    def __init__(self, name):
        self.name = name
        print("person constructor")

class Employee(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary
        print("employee constructor")

obj = Employee("umesh", 900000)        
'''
# person constructor
# employee constructor






'''
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class c(B,A):
    def show(self):
        A.show(self)
        B.show(self)
        print("C")        

obj = c()
obj.show()
'''
# A
# B
# C






'''
class A:
    def show1(self):
        print("A")

class B(A):
    def show2(self):
        print("B")

class C(A):
    def show3(self):
        print("C")

obj = C()
obj.show1()
# obj.show2() #AttributeError: 'C' object has no attribute 'show2'. Did you mean: 'show1'?
obj.show3()

obj1 = B()
obj1.show1()
obj1.show2()
'''
# A
# C
# A
# B





class A:
    def show1(self):
        print("A")

class B(A):
    def show2(self):
        print("B")

class C(A):
    def show3(self):
        print("C")

class D(B,C):
    def show4(self):
        print("D")

obj1 = D()
obj1.show1()        
obj1.show2()        
obj1.show3()        
obj1.show4()        
print(D.mro())

# A
# B
# C
# D        
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]