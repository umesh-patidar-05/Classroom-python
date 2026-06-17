print("17/june/2026")



'''
def hello(name,*marks):
    print("Name is",name) #Name is deepika
    print("Marks is",marks) #Marks is (10, 20, 30)
    print("Marks is",*marks)  #Marks is 10 20 30
hello("deepika",10,20,30)    
'''


'''
def average(*n): 
    return sum(n)/len(n)
print(average(10,20,30,40)) #25.0
'''




'''
list1=[1,2,3,4,5]
def add(a,b,c,d,e):
    return a+b+c+d+e
print(add(*list1))       #15
'''



'''
def add(*l1):
    s=0
    for i in l1:
        s=s+i
    return s
print(add(10,20,30,40,50))   #150       
'''



'''
l1=[10,20,30,40]
def add(*l2):
    return sum(l2)
print(add(*l1))  #100
'''




'''
l1=[10,20,30,40]
def add(l2):
    return sum(l2)
print(add(l1))  #100  
'''



'''
def display(**kwargs):
    print(kwargs)  #{'name': 'deepika', 'age': 30, 'address': 'chennai'}
display(name="deepika", age=30, address="chennai")    
'''



'''
def display(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
display(name="deepika", age=30, address="chennai")    
'''
'''
name deepika
age 30
address chennai

'''



'''
def display(name,**details):
    print(name,details)  #deepika {'age': 30, 'address': 'chennai'}
display("deepika", age=30, address="chennai")    
'''




'''
def profile(**info):
    if "name" in info:
        print("Welcome",info["name"])
    if "email" in info:
        print("Email",info["email"])
    if "address" in info:
        print("Address",info["address"])  
profile(name="deepika", email="dee@gmail.com", address="chennai")
'''
'''
Welcome deepika
Email dee@gmail.com
Address chennai
'''




'''
def display(name,age,/):
    print(name,age)
display("Deepika",30)   # Deepika 30
'''




'''
def display(name,age,/):
    print(name,age)
display(name="Deepika",age=30)    #TypeError: display() got some positional-only arguments passed as keyword arguments: 'name, age'
'''



'''
def add(a,b,c,/):
    print(a+b+c)  #60
add(10,20,30)    
'''



'''
def add(a,b,c,/):
    print(a+b+c)
add(a=10,b=20,c=30)    #TypeError: add() got some positional-only arguments passed as keyword arguments: 'a, b, c'
'''



'''
def show(name,*,age,address):
    print(name)
    print(age)
    print(address)
show("deepika",age=30,address="chennai")    
'''



'''
def show(name,*,age,address):
    print(name)
    print(age)
    print(address)
show("deepika",30,"chennai")    #TypeError: show() takes 1 positional argument but 3 were given
'''



'''
def show(id,name,/,salary,*,age,address):
    print(id)
    print(name)
    print(salary)
    print(age)
    print(address)
show(101,"deepika",3000,age=30,address="chennai")    
'''
'''
deepika
3000
30
chennai
'''


'''
def show(id,name,/,salary,*,age,address):
    print(id)
    print(name)
    print(salary)
    print(age)
    print(address)
show(id=101,"deepika",3000,age=30,address="chennai")    #SyntaxError: positional argument follows keyword argument
'''



'''
def show(id,name,/,salary,*,age,address):
    print(id)
    print(name)
    print(salary)
    print(age)
    print(address)
show(101,"deepika",salary=3000,30,address="chennai") #SyntaxError: positional argument follows keyword argument
'''



'''
def show(id,name,/,salary,*,age,address):
    print(id)
    print(name)
    print(salary)
    print(age)
    print(address)
show(101,"deepika",salary=3000,age=30,address="chennai")
'''
'''
101
deepika
3000
30
chennai
'''



'''
fun= lambda n:n*n
print(fun(5))   #25
'''


'''
add = lambda a,b:a+b
print(add(5,10))
'''


'''
add = lambda a,b:print(a+b)
add(10,20) #30
'''


'''
max=lambda a,b:a if a>b else b
print(max(10,20))  #20
'''



def sq(x):
    return x*x
l1=[10,20,30,40]
print(list(map(sq,l1)))    #[100, 400, 900, 1600]

