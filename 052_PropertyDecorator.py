print("09/july/2026")



'''
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

e = Employee(1000)
print(e.get_salary()) #1000
'''





'''
class Employee:

    def __init__(self, salary):
       self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

e = Employee(1000)
print(e.salary)   #1000
'''





'''
class Employee:

    def __init__(self, salary):
       self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

e = Employee(1000)
print(e.salary)   #1000
e.salary = 555
print(e.salary)   #555
'''





'''
class Student:
    def __init__(self, rollno, name, marks):
        self.__rollno = rollno
        self.__name = name
        self.__marks = marks

    @property
    def rollno(self):
        return self.__rollno
    @rollno.setter
    def rollno(self, rollno):
        self.__rollno = rollno

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self, marks):
        self.__marks = marks

s1 = Student(101, "umesh", 90)
print(s1.rollno)   #101     
print(s1.name)     #umesh  
print(s1.marks)    #90

s1.rollno = 102          
s1.name  = "kushal"   
s1.marks = 100

print(s1.rollno)   #102    
print(s1.name)     #kushal    
print(s1.marks)    #100
'''






'''
class Product:
    def __init__(self, p_id, p_title, p_price):
        self.__p_id = p_id
        self.__p_title = p_title
        self.__p_price = p_price

    @property
    def p_id(self):
        return self.__p_id

    @property
    def p_title(self):
        return self.__p_title
    @p_title.setter
    def p_title(self, p_title):
        self.__p_title = p_title

    @property
    def p_price(self):
        return self.__p_price
    @p_price.setter
    def p_price(self, p_price):
        self.__p_price = p_price

p = Product(101, "iphone", 60000)

print(p.p_id) #101
print(p.p_title) #iphone
print(p.p_price) #60000

p.p_title = "laptop"
p.p_price = 90000

print(p.p_id) #101
print(p.p_title) #laptop
print(p.p_price) #90000
'''





class Book:

    def __init__(self, book_no, book_name, book_writer):

        self.__book_no = book_no
        self.__book_name = book_name
        self.__book_writer = book_writer

    @property
    def book_no(self):
        return self.__book_no

    @property
    def book_name(self):
        return self.__book_name

    @book_name.setter
    def book_name(self, book_name):
        self.__book_name = book_name

    @book_name.deleter
    def book_name(self):
        del self.__book_name

    @property
    def book_writer(self):
        return self.__book_writer

    @book_writer.setter
    def book_writer(self, book_writer):
        self.__book_writer = book_writer

    @book_writer.deleter
    def book_writer(self):
        del self.__book_writer

b = Book(10001, "the secret", "abc")
print(b.book_no)
print(b.book_name)
print(b.book_writer)

'''
output:

10001
the secret
abc
'''

del b.book_name
#print(b.book_name)

'''
AttributeError: 'Book' object has no attribute '_Book__book_name'. Did you mean: '_Book__book_no'?

'''

del b.book_writer
#print(b.book_writer)
'''
AttributeError: 'Book' object has no attribute '_Book__book_writer'
'''