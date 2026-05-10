'''
a=int(input("Enter the choice: "))
match a:
    case 3:
        print("Three")
    case 1:
        print("One")
    case _:
        print("Wrong")
print("Out of match case")        
'''



'''
a=int(input("Enter the choice"))
match a:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2|3|4:
        print("two three or four")
    case _:
        print("Wrong")
print("Out of match case")    
'''







'''
a=int(input("Enter the choice"))
match a%2:
    case 0:
        print("Even")
    case 1:
        print("Odd")
    case _:
        print("Wrong")
print("Out of match case")   
'''



'''
day=input("Enter the choice ")
match day:
    case "monday":
        print("Start")
    case "sunday":
        print("rest")
    case _:
        print("Wrong")
print("out of match case")
'''



'''
a=int(input("Enter first number "))
b=int(input("Entert second number "))
op=input("Enter operator(+,-,*,/)")
match op:
    case "+":
        print("result is ",(a+b))
    case "-":
        print("result is ",(a-b))
    case "*":
        print("result is ",(a*b))
    case "/":
        if b!=0:
            print("result is ",(a/b))
        else:
            print("avoid zero")
print("Out of the match case")            
'''




'''
ch=input("Enter vowel or conso.").lower()
match ch:
    case "a"|"e"|"i"|"o"|"u":
        print("Vowel")
    case "#"|"$"|"&":
        print("special")
    case _: 
        print("Conso")
print("Out of the match case")        
'''







'''
age=int(input("Enter age: "))
match age:
    case x if x<13:
        print("child")
    case x if x<20:
        print("teen")
    case x if x<50:
        print("adult")
print("out of match case")        
'''



'''
n=int(input("Enter age"))
match n:
    case x if x%2==0:
        print("Even")
    case x:
        print("Odd")
print("out of match case ")        
'''




'''
n=int(input("Enter age"))
match n:
    case n if n%2==0:
        print("Even")
    case n:
        print("Odd")
print("out of match case ")        
'''




while True:
    print("MENU")
    print("1. Add to numbers")
    print("2. Check even or odd")
    print("3. find square")
    print("4. Exit")
    choice=int(input("Enter the choice "))
    match choice:
        case 1:
            a=int(input("Enter first number "))
            b=int(input("Enter second number "))
            print("Sum is ",(a+b))
        case 2:
            a=int(input("Enter the number "))
            if a%2==0:
                print("Even")
            else:
                print("Odd")
        case 4:
            print("existing code")
            break    