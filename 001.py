                                                                         # OUTPUT FUNCTIONS IN PYTON

'''
print("hello")
print(10)
print(12.5)
print("True")
'''

'''
name = "Umesh"
age = 30
print(name, age)
'''

'''
name = "deepika"
age = 30
print(name, age, sep="->")
print(10,20,30,40, sep=",")
print("A","B","c", sep="\n")
'''

'''
print("hello", end="__")
print("guys")
'''

'''
print("hello \n guys")
print("hello \t guys")
'''

'''
name = "deepika"
print("Name of a person is", name)
print(f"Name of a person is {name}")
'''

'''
age = 30
print(f"Next year age is {age+1}")
'''
'''
name = "deepika"
age = 30
print(f"hello {name + " Welcome"}")
print(F"hello {name + " welcome"} your age is {age}")
'''
'''
name = "deepika"
age = 30
print(F'address is {address}')        
'''                                 
                            # output = NameError: name 'address' is not defined    

'''
name = "deepika"
age = 30
print(f'address is {}') 
'''
                            #output  SyntaxError: f-string: valid expression required before '}'               
'''
name = "Depika"
age = 30
print('age is {}'.format(age))
'''

'''
name = "deepika"
age = 30
address = 'chennai'
print('Name is {} age is {} and address is {}'.format(name, age, address))
'''

                                                                 # INPUT FUNCTIONS IN PYTON
'''
name = input("enter the name of a person ")
print('name is', name)
'''


'''
a = input("Enter first number")
b = input("Enter second number")
print(a+b)
print(type(a))
'''

'''
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(type(a))
print(a+b)
'''

'''
salary1 = float(input("Enter first salary"))
salary2 = float(input("Enter second salary"))
print("total salary is ",(salary1 + salary2))
'''

'''
name, address = input("enter name and address").split()
print("name is", name)
print("address is", address)
'''

'''
name, address = input("enter name and address").split(",")
print("name is", name)
print("address is", address)
'''

'''
id,name,address = input("enter id, name and address").split(maxsplit=2)
print("id is", id)
print("name is", name)
print("address is", address)
'''

'''
name,age = input("enter name and age").split()
print("name is",name)
print("age is", age)
age = int(age)
print("next year age is", age+1)
'''

'''
marks1,marks2 = input("Enter both marks").split()
print(marks1)
print(marks2)
marks1 = int(marks1)
marks2 = int(marks2)
print(marks1 + 5)
print(marks2 + 10)
'''

'''
marks1, marks2 = map(int, input("enter both marks").split())
print(marks1)
print(marks2)
print(marks1 + 5)
print(marks2 +10)
'''

'''
data = input("Enter both marks").split()
print(data)
print(data[0])
print(data[1])
'''

'''
m1, m2 = int(input("enter both marks").split())
print(m1)
print(m2)
'''
                                #output TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'


m1, m2 = map(float,input("Enter both marks").split())
print(m1)
print(m2)
