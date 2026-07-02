print("2/july/2026")



'''
class Hello:
    def __init__(self):
        print("address of self", id(self))

obj=Hello()
print("address of self", id(obj))
'''
# address of self 139808591200016
# address of self 139808591200016





'''
class Counter:
    def __init__(self):
        self.count=0

    def increment(self):
        self.count=self.count+1

    def decrement(self):
        self.count=self.count-1
        
    def getcount(self):
        return self.count
    
c=Counter()
c.increment()
c.increment()
print(c.getcount())   #2
c.decrement()
print(c.getcount())   #1
'''



'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("deepika",30)
s2=Student("rashmika",33)
print(s1.name)   #deepika
print(s2.name)   #rashmika
s1.name="dipu"   
print(s1.name) #dipu
print(s2.name) #rashmika
'''                



'''
class Student:
    def set(self,name,age):
        self.name=name
        self.age=age
s1=Student()
s2=Student()
s1.set("deepika",30)
s2.set("rashmika",33)
print(s1.name)   #deepika
print(s2.name)   #rashmika
s1.name="dipu"   
print(s1.name) #dipu
print(s2.name) #rashmika
'''



'''
class Student:
    pass
s1=Student()
s1.name="deepika"
print(s1.name)  #deepika
'''
 


'''
class Student:
    college="IIT Delhi"
    def __init__(self,name):
        self.name=name 

s1=Student("deepika")
s2=Student("virat")
print(s1.name)  #deepika
print(s1.college)  #IIT Delhi
print(s2.name)   #virat
print(s2.college)   #IIT Delhi
Student.college="IIT Indore"
print(s1.college) #IIT Indore
print(s2.college) #IIT Indore          
'''




'''
class Student:
    college="IIT Delhi"
    def __init__(self,name,city):
        self.name=name
        self.city=city

s1=Student("deepika", "chennai")
s2=Student("virat", "delhi")
print(s1.__dict__)  #{'name': 'deepika', 'city': 'chennai'}
print(s2.__dict__)  #{'name': 'virat', 'city': 'delhi'}
s1.college="SAIT"
print(s1.__dict__)  #{'name': 'deepika', 'city': 'chennai', 'college': 'SAIT'}
print(s2.__dict__)  #{'name': 'virat', 'city': 'delhi'}
print(s1.college)  #SAIT
print(s2.college)  #IIT Delhi
'''




'''
class Test:
    x=10

t1=Test()
t2=Test()
t1.x=90
print(t1.x)  #90
print(t2.x)  #10
print(Test.x) #10
print(t1.__dict__) #{'x': 90}
Test.x=100
print(t1.x)  #90
print(t2.x)  #100
Test.y=900
print(t1.y)  #900
print(t2.y)  #900
'''



'''
class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30
        self.d=40

t1=Test()
t1.m1()
t1.e=900
print(t1.__dict__)  #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 900}
'''



'''
class Test:
    a=10
    def __init__(self):
        self.b=20
        self.c=30

    def m1(self):
        Test.d=100

t1=Test()
t1.m1()
t2=Test()
print(t1.__dict__)  #{'b': 20, 'c': 30}
print(t2.a)  #10
print(t2.c)  #30
print(t2.d)  #100
print(Test.__dict__)  #{'__module__': '__main__', '__firstlineno__': 152, 'a': 10, '__init__': <function Test.__init__ at 0x000001A90EA585C0>, 'm1': <function Test.m1 at 0x000001A90EA59640>, '__static_attributes__': ('b', 'c'), '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'd': 100}
'''





class Test:
    def __init__(self,a1,b1):
        self.a=a1
        self.b=b1
        c=self.a+self.b
        print(c)

t1=Test(10,20)   #30