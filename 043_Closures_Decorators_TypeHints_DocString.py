print("24/june/2026")



'''
def hello(name):
    message=f"hello {name}"
    def display():
        print(message)   #hello deepika
    return display

h=hello("deepika") 
h()
'''



'''
def counter():
    count=0
    def increment():
        nonlocal count
        count= count+1
        return count
    return increment
c=counter()
print(c())  #1
print(c())  #2
print(c())  #3
'''



'''
def cardmaker(greeting,name):
    def card():
        return f"{greeting}, {name}"
    return card
first=cardmaker("hiii", "deepika")
second=cardmaker("hello", "rashmika")
print(first())   #hiii, deepika
print(second())  #hello, rashmika
'''



'''
def cardmaker(greeting,name):
    def card():
        return f"{greeting}, {name}"
    return card
first=cardmaker("hiii", "deepika")
second=cardmaker("hello", "rashmika")
print(first())   #hiii, deepika
print(second())  #hello, rashmika
print(first.__closure__)   #(<cell at 0x0000019CC5E572E0: str object at 0x0000019CC5E56A00>, <cell at 0x0000019CC5E573A0: str object at 0x0000019CC5E56FD0>)
'''




'''
def mydesign(func):
    def wraper():
        print("before calling the code")
        func()
        print("after calling the function")
    return wraper
def hello():
    print("hello guyss how the life is going on") 
d=mydesign(hello)
d()
'''
# before calling the code
# hello guyss how the life is going on
# after calling the function





'''
def mydesign(func):
    def wraper():
        print("before calling the code")
        func()
        print("after calling the function")
    return wraper

@mydesign
def hello():
    print("hello guyss how the life is going on") 
hello()        
'''
# before calling the code
# hello guyss how the life is going on
# after calling the function





'''
loggedin=True
def loginrequired(func):
    def wraper():
        if loggedin:
            print("processing")
            func()
        else:
            print("plz login")
    return wraper

@loginrequired
def profile():
    print("Welcome to our page")        

@loginrequired
def transaction():
    print("transition done")

profile()
transaction()    
'''
# processing
# Welcome to our page
# processing
# transition done






'''
def mydecorators(func):
    def wrapper(*args,**kwargs):
        print("calculation starting")
        result=func(*args,**kwargs)
        print("calculation done")
        return result
    return wrapper

@mydecorators
def add(a,b):
    print("sum is",a+b)

@mydecorators
def product(a,b,c):
    print("Multiply is",a*b*c)

add(10,20)
product(5,4,3)        
'''
# calculation starting
# sum is 30
# calculation done
# calculation starting
# Multiply is 60
# calculation done



'''
def add(a:int, b:int) -> int:
    return a+b
result=add(5,10)
print(result)  #15
'''



'''
def add(a:int, b:int) -> int:
    return a+b
result=add(5.5,10)
print(result) #15.5
'''



#mypy
''' 
def add(a:int, b:int) -> int:
    return a+b
result=add(5.5,10)
print(result)   #Found 1 error in 1 file (checked 1 source file)
'''



'''
def add(a:int, b:int)-> int:
    return "hello"
result=add(5.5,"dipu")
print(result)   #Found 3 errors in 1 file (checked 1 source file)
'''


'''
def add(a,b):
    """this is add function used for addition"""
    return a+b
print(add(10,20))  #30
'''



'''
def add(a,b):
    """this is add function used for addition"""
    return a+b
print(add(10,20))
print(add.__doc__)
'''
# 30
# this is add function used for addition





'''
def add(a,b):
    return a+b
print(add(10,20))   
print(add.__doc__)   
'''
# 30
# None




'''
print(int.__doc__)
'''
# int([x]) -> integer
# int(x, base=10) -> integer

# Convert a number or string to an integer, or return 0 if no arguments
# are given.  If x is a number, return x.__int__().  For floating-point
# numbers, this truncates towards zero.

# If x is not a number or if base is given, then x must be a string,
# bytes, or bytearray instance representing an integer literal in the
# given base.  The literal can be preceded by '+' or '-' and be surrounded
# by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
# Base 0 means to interpret the base from the string as an integer literal.
# >>> int('0b100', base=0)
# 4




'''
def add(a,b):
    "this is add "
    return a+b
print(add(10,20))   
print(help(add))   
'''
# 30
# Help on function add in module __main__:                                                                                                                        

# add(a, b)
#     this is add

# None