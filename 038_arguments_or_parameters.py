print("15/june/2026")



'''
def sum(a,b):
    c=a+b
    return c

def main():
    x=sum(10,20)    
    c=sum(11,22)
    print(sum(66,77))
    print(c)
    print(x)
main()
'''



'''
def sum(a,b):
    c=a+b
    return c

def main():
    sum(10,20)
    print(c)  #NameError: name 'c' is not defined
main()
'''



'''
def sum(a,b):
    c=a+b

def main():
    print(sum(10,20))
    x=sum(11,99)
    print(x)
main()
'''



'''
def hello():
    print("hello")
    return
    print("bye")

def main():
    print("welcome")
    hello()
    print("done")
main()
'''
'''
welcome
hello
done
'''




'''
def calculate(a,b):
    return a+b, a-b
def main():
    print("Welcome")
    result=calculate(10,5)
    print(result) 
    print("sum is", result[0])
    print("diff is", result[1])
main()    
'''
'''
Welcome
(15, 5)
sum is 15
diff is 5

'''




'''
def calculate(a,b):
    return a+b, a-b
def main():
    print("Welcome")
    sum,diff=calculate(10,5)
    print("sum is", sum)
    print("diff is", diff)
main()
'''    

'''
Welcome
sum is 15
diff is 5

'''



'''
def evenlist(n):
    evens=[]
    for i in range(1,n+1):
        if i%2==0:
            evens.append(i)
    return evens
def main():
    print("Welcome")  #Welcome
    print(evenlist(10)) #[2, 4, 6, 8, 10]
    x=evenlist(10)
    print(x) #[2, 4, 6, 8, 10]
    print(type(x))   #<class 'list'>
main()        
'''





'''
def evenlist(n):
    return n
def main():
    print("Welcome")
    x=evenlist([10,20,30,40])
    print(x)  #[10, 20, 30, 40]
    print(type(x)) #<class 'list'>
main()        
'''


#function(parametername=value)



'''
def hello(name,age):
    print("name is",name)
    print("age is",age)
  
hello(age=20,name="deepika")  
'''
'''
15/june/2026
name is deepika
age is 20
'''




'''
def hello(name,age):
    print("name is",name)
    print("age is",age)
  
hello(age=20,name1="deepika")   #TypeError: hello() got an unexpected keyword argument 'name1'
'''

'''
def hello(age,name):
    print("name is",name)  #SyntaxError: positional argument follows keyword argument
    print("age is",age)
  
hello(age=20,"deepika")    
'''


'''
def hello(name,age,address,salary):
    print("name is",name)
    print("age is",age)
    print("address is",address)
    print("salary is",salary)
  
hello("deepika",30,address="chennai", salary=440000)  
'''

'''
def hello(name,age,address="indore",salary=500):
    print("name is",name)
    print("age is",age)
    print("address is",address)
    print("salary is",salary)
  
hello("deepika",30) 
hello("deepika",30,"chennai") 
hello("deepika",30,"chennai") 
hello("deepika",30,"chennai",3400000) 
'''



'''
def hello(name="dipu",age,address,salary=500):  #SyntaxError: parameter without a default follows parameter with a default
    print("name is",name)
    print("age is",age)
    print("address is",address)
    print("salary is",salary)
  
hello("deepika",30) 
hello("deepika",30,"chennai") 
hello("deepika",30,"chennai") 
hello("deepika",30,"chennai",3400000) 
'''





'''
def hello(name,age,address="indore",salary=500): 
    print("name is",name)
    print("age is",age)
    print("address is",address)
    print("salary is",salary)
  
hello("deepika",30) 
hello("deepika",30,address="chennai") 
hello("deepika",30,"chennai",3400000) 
'''
'''
name is deepika
age is 30
address is indore
salary is 500
name is deepika
age is 30
address is chennai
salary is 500
name is deepika
age is 30
address is chennai
salary is 3400000
'''



'''
def display(*args):
    print(args)  #(1, 2, 3, 4, 5, 6)
display(1,2,3,4,5,6)    
'''


'''
def display(*x):
    print(x)  #(1, 2, 3, 4, 5, 6)
display(1,2,3,4,5,6)  
'''



'''
def display(*x):
    print(x)  #(1, 2, 3, 4, 5, 6)
display(1,2,"umesh",4,"patidar",6)  
'''



'''
def sum(x,y):
    print(x+y)
sum(10,20,30)    #TypeError: sum() takes 2 positional arguments but 3 were given
'''


'''
def sum(*a):
    total=0
    for n in a:
        total+=n
    print(total)
sum(10,20,30)     #60
sum(10,20,30,60,70,80) #270
sum(10,20) #30
sum(10)    #10
sum()    #0
'''





'''
def main():
    a=int(input("Enter first number: "))
    b=int(input("Ente second number: "))
    
    def sum(a,b):
        c=a+b
        print(c)
        
    def sub(a,b):
        c=a-b 
        print(c)

    def mul(a,b):
        c=a*b 
        print(c)        
    print("1. sum\n2.subtract\n3. multiplication\n4. exit")    

    while True:
        choice=int(input("Enter choice: "))
        if choice==1:
            sum(a,b)
        elif choice==2:        
            sub(a,b)
              
        elif choice==3:
            mul(a,b)                                
        else:
            break    
main()                
'''


