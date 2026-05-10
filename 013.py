'''
x=30 if 10<20 else 40
print(x)
'''


'''
x=30 if 101<20 else 40
print(x)
'''


'''
n=int(input("Enter the number "))
result="even" if n%2==0 else "odd"
print(result)
'''


'''
a=int(input("Enter first number"))
b=int(input("Enter second number"))
max=a if a>b else b
print(max) 
'''


'''
a=int(input("Enter first number "))
b=int(input("Enter seond number "))
print("a is greater") if a>b else print("b is greater")
'''


'''
x=10 if 20<30 else 40 if 50<60 else 70
print(x)
'''


'''
x=10 if 200<30 else 40 if 50<60 else 70
print(x)
'''


'''
x=10 if 200<30 else 40 if 500<60 else 70
print(x)
'''



'''
a=100
b=200
c=30
max=a if a>b and a>c else b if b>c else c
print(max,"is greater ")
'''



'''
a=int(input("Enter a "))
b=int(input("Enter b "))
print("equal" if a==b else "greater" if a>b else "small")
'''



'''
i=1
while i<=10:
    print(i,"Even") if i%2==0 else print(i,"Odd")
    i+=1
'''



'''
i=1
while i<=10:
    print(i,"Even" if i%2==0 else "Odd")
    i+=1
'''




a=int(input("input choice "))
match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Wrong choice")