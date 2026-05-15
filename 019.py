'''
s="deepika"
print(s.index("a"))     # 6
'''



'''
s="deepika"
print(s.index("x"))      # ValueError: substring not found
'''


'''
s="deepika"
print(s.index("e"))  # 1
'''


'''
s="deepikae"
print(s.rindex("e"))     # 7
'''



'''
s="deepikae"
print(s.count("e"))    #3
'''


'''
s="deepikae"
print(s.count("x"))   #0
'''


'''
s="deepikae"
print(s.isalpha())    # True
print("rashmika123".isalpha())   # False
print("#$%".isalpha())    # False
print("hello guys".isalpha())    # False
'''



'''
s="deepika123"
print(s.isdigit())  # False
print("123".isdigit())   # True
print("#$%".isdigit())   # False
print("123 456".isdigit())  # False
'''


'''
s="deepika123"
print(s.isalnum())   #True
print("123".isalnum())  # True
print("#$%".isalnum())   # False
print("123 456".isalnum())  # False
print("abc".isalnum())   # True
'''



'''
s="deepika123"
print(s.islower())   #True
print("ABC".islower())  #False
print("Abc".islower())  #False
print("123".islower())  # False
print("@#$".islower())   # False
'''



'''
s="deepika123"
print(s.isupper())   # False
print("ABC".isupper())   # True
print("Abc".isupper())   # False
print("123".isupper())  #False
print("#%$".isupper())  # False
'''



'''
s="deepika123"
print(s.isspace()) # False
print("hello guys".isspace()) #False
print(" hello guys ".isspace())  # False
print(" ".isspace()) # True
print("".isspace())   # False
'''


'''
s="Hello Deepika How Are U"
print(s.istitle()) # True
print("Hello guys".istitle())  # false
print("Hello 123 Deepika".istitle())  # True
'''


'''
s="i like java"
print(s.replace("java","python"))   # i like python
'''



'''
s="  java  "
print(len(s))      #8
print(s)           #    java
print(s.strip())   #java
s1=s.strip()       
print(len(s1))     #4
print(s1)          #java 
'''




'''
s="    aree    java     "
print(len(s))              #21
print(s)                   #    aree    java     
print(s.strip())           #aree    java     
'''



'''
s="   java   "
print(len(s))       #10
print(s)            #   java   
print(s.lstrip())   #java   
s1=s.lstrip()       
print(len(s1))      #7
print(s1)           #java
'''



'''
s="  java  "
print(len(s))      #8
print(s)           #  java  
print(s.rstrip())  #  java
'''


'''
s="hello guys how are u"
print(s.split())     # ['hello', 'guys', 'how', 'are', 'u']
l1=s.split()
print(l1)            # ['hello', 'guys', 'how', 'are', 'u']
print(len(l1))    # 5
print(l1[0])    # hello
'''


'''
s="hello,guys,how,are,u"
print(s.split(","))     # ['hello', 'guys', 'how', 'are', 'u']
l1=s.split(",")
print(l1)            # ['hello', 'guys', 'how', 'are', 'u']
print(len(l1))    # 5
print(l1[0])    # hello
'''

'''
l1=["hello","guys","how"]
print("".join(l1))                   # helloguyshow
s1=" ".join(l1)
print(s1)                             #hello guys how
print(",".join(l1))                #hello,guys,how
'''



'''
password=input("Enter the password ")
upper=0
lower=0
digit=0
space=0
special=0
i=0
if len(password)>=8 and len(password)<=15:
    while i<len(password):
        ch=password[i]
        if ch>='A' and ch<='Z':
            upper=1
        elif ch>='a' and ch<='z':
            lower=1
        elif ch>='0' and ch<='9':
            digit=1
        elif ch==" ":
            space=1
        else:
            special=1
        i+=1
    if upper==1 and lower==1 and digit==1 and space==0 and special==1:
        print("Valid")
    else:
        print("Invalid")
    
else:
    print("Invalid")    
'''





'''
password=input("Enter the password ")
upper=0
lower=0
digit=0
space=0
special=0
i=0
if len(password)>=8 and len(password)<=15:
    while i<len(password):
        ch=password[i]
        if ch.isupper():
            upper=1
        elif ch.islower():
            lower=1
        elif ch.isdigit():
            digit=1
        elif ch.isspace():
            space=1
        else:
            special=1
        i+=1
    if upper==1 and lower==1 and digit==1 and space==0 and special==1:
        print("Valid")
    else:
        print("Invalid")
    
else:
    print("Invalid")    
'''    
    
    
    
    
password=input("Enter the password ")
upper=0
lower=0
digit=0
space=0
special=0
if len(password)>=8 and len(password)<=15:
    for ch in password:
        if ch>='A' and ch<='Z':
            upper=1
        elif ch>='a' and ch<='z':
            lower=1
        elif ch>='0' and ch<='9':
            digit=1
        elif ch==" ":
            space=1
        else:
            special=1
    if upper==1 and lower==1 and digit==1 and space==0 and special==1:
        print("Valid")
    else:
        print("Invalid")
    
else:
    print("Invalid")        
