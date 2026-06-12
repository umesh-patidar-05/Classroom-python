print("12/june/2026")




'''
def hello():
    print("this is first function")
    
hello()  #this is first function
hello()  #this is first function
'''


'''
hello() #NameError: name 'hello' is not defined. Did you mean: 'help'?
def hello():  
    print("this is first function")
    
hello() 
'''



'''
def sum():
    a=10 
    b=20
    c=a+b
    print("sum is ",c)
    
sum()   
'''


'''
def sum(a,b):
    c=a+b
    print("sum is ",c)
    
sum(10,20)   
'''


'''
def sum(a,b):
    c=a+b
    print("sum is ",c)
    
a=int(input("Enter a "))    
b=int(input("Enter b "))    
sum(a,b)   
'''



'''
def sum(x,y):
    c=x+y
    print("sum is ",c)
    
a=int(input("Enter a "))    
b=int(input("Enter b "))    
sum(a,b)   
'''


'''
def welcome():
    print("Welcome guys")
    
def hello():
    print("hello guys ")
    welcome()
def sum(x,y):
    hello()
    c=x+y    
    print("sum is ",c)
sum(10,20)   
'''


'''
def welcome(name):
    print("welcome ",name)
def hello(name):
    print("hello",name)
    welcome(name)
    print("good byee") 
hello("deepika")    
'''


'''
def hello(name,age):
    print("name is ",name,"and age is",age)
hello("deepika",30)    #name is  deepika and age is 30
'''


'''
def hello(name,age):
    print("name is ",name,"and age is",age)
hello("deepika")     #TypeError: hello() missing 1 required positional argument: 'age'
'''




'''
def sum(a,b):
    c=a+b
    print("sum is",c)
 
def mul(a,b):
    c=a*b
    print("multi is",c)   

def mainlogic():
    sum(10,20)    
    mul(3,4)
mainlogic()

#OUTPUT:
#sum is 30
#multi is 12
'''



'''
def sum(a,b):
    c=a+b
    return c
 
def mul(a,b):
    c=a*b
    return c   

def mainlogic():
    x=sum(10,20)    
    y=mul(3,4)
    print("sum is ",x)
    print("multi is ",y)
mainlogic()

#OUTPUT:
#sum is  30
#multi is  12
'''
