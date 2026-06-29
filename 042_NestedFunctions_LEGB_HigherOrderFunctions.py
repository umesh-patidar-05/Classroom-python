print("23/june/2026")



'''
def hello(name):
    def message():
        return "heyyy guysss"
    print("hello",name)
    print(message())
hello("deepika")
'''
# hello deepika
# heyyy guysss




'''
def hello(name):
    def message():
        return "heyyy guysss"
    print("hello",name)
    print(message())
message()   #NameError: name 'message' is not defined
'''
# we cannot call inner function from outside the outer function





'''
def outer():
    x=10
    def inner():
        print("Value of",x)   # Value of 10 
    inner()
outer()        
'''
       



'''
def outer():
    x=10
    def inner():
        y=20
        print("value of",x)
    inner()
    print(y)  #NameError: name 'y' is not defined
outer()        
'''





'''
def outer():
    x=10
    def inner():
        x=20
        print("inner value",x)
    inner()
    print("inside outer",x) 
outer()        
'''
# inner value 20
# inside outer 10





'''
def outer():
    x=10
    def inner():
        nonlocal x
        x=100
        print("inner value of",x)
    inner()
    print("inside outer",x) 
outer()        
'''
# inner value of 100
# inside outer 100




'''
x=100
def test():
    x=10
    print("inside function",x)
test()
print("x is",x)   
'''
# inside function 10
# x is 100



'''
x=100
def outer():
    x=90
    def test():
        print("inside function",x)
    test()
outer()
print("x is",x)        
'''
# inside function 90
# x is 100




'''
x=100
def outer():
    def test():
        print("inside function",x)
    test()
outer()
print("x is",x)   
'''
# inside function 100
# x is 100





'''
def outer():
    def test():
        print("inside function")
        print(len([10,20,30]))
    test()
outer()    
'''
# inside function
# 3




'''
def total(price,taxrate):
    def calculatetax():
        return price*taxrate
    return price + calculatetax()
print(total(1000,0.18))    #1180.0
'''




'''
def bill(amount):
    def discount():
        if amount>10000:
            return amount*0.10
        return 0
    d=discount()
    finalamount=amount-d
    return finalamount
print(bill(15000)) #13500.0
print(bill(5000))   #5000
'''




'''
def hello(fun):
    return fun("heyyyyy")
def uppercase(x):
    return x.upper()
print(hello(uppercase))   #HEYYYYY
'''




def apply(fun,x):
    return fun(x)
def square(n):
    return n*n
print(apply(square,5))   #25