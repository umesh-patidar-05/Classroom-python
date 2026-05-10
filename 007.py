

'''
print("Welcome")
name = input("Enter the name: ")
if name:
    print("name entered is ", name)
print("done")
'''





'''
print("Welcome")
name = input("Enter the name ")
if name:
    print("name entered is ", name)
else:
    print("name not entered")
    print("plz enter")
print("done")
'''






'''
print("Welcome")
a = int(input("enter first number"))
b = int(input("enter second number"))
if a>b:
    print("a is greater")
else:
    print("b is greater")
print("done")
'''








'''
print("welcome")
a = int(input("enter first number"))
b = int(input("enter second number"))
if a>b:
    pass
else:
    print("b is greater")
print("done")
'''







'''
print("welcome")
a = int(input("enter first number"))
b = int(input("enter second number"))
if a>b:
    None
else:
    print("b is greater")
print("done")
'''






'''
print("Welcome")
ch = input("Enter character").lower()
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Vovel")
else:
    print("consonant")
print("done")
'''




'''
print("Welcome")
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
'''







'''
print("Welcome")
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
d = int(input("Enter fourth number"))
if a>b:
    if a>c:
        if a>d:
            print("a is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("c is greater")
        else:
            print("d is grater")
else:
    if b>c:
        if b>d:
            print("b is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("C is greater")
        else:
            print("d is greater")   
'''






'''
print("Welcome")
age = int(input("Enter age number "))
citizen = input("are u indian (yes/no) ")
if age>=18:
    if citizen.lower()=='yes':
        print("u can vote")
    else:
        print("must be indian")
else:
    print("under age")
print("done")
'''






'''
print("Welcome")
username = input("Enter username ")
password = input("Enter password ")
if username == "admin":
    if password == "1234":
        print("password is valid")
    else:
        print("invalid password")
else:
    print("invalid username")
print("done")
'''








'''
print("Welcome")
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number ")) 
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
print("done")
'''



print("Welcome")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
d=int(input("Enter fourth number"))
if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d:
    print("b is greater")
elif c>d:
    print("c is greater")
else:
    print("d is greater")
print("done")








