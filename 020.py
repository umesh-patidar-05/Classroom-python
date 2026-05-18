'''
str="python java react AI aree samjhe"
result=str.split(" ",2)
result1=str.rsplit(" ",2)
print(result)                  #['python', 'java', 'react AI aree samjhe']
print(result1)                 #['python java react AI', 'aree', 'samjhe']
'''



'''
str="Python is language"
print(str.center(20))            # Python is language
print(str.center(20,"*"))        #*Python is language*      
str1=str.center(20)                    
print(len(str1))                 #20  
print(str.center(40,"*"))        #***********Python is language***********
'''




'''
str="python"
print(str.ljust(20))              #python
print(str.ljust(20,"*"))          #python**************    
'''



'''
str="python"
print(str.rjust(20))             #              python
print(str.rjust(20,"*"))         #**************python   
'''



'''
str="python"
print(dir(str))
print(len(dir(str)))    #81

                                ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'''





'''
str="python is nice language"
print(str.startswith("python"))            #True
print(str.startswith("ppython"))           #False
'''



'''
str="python is nice language"
print(str.endswith("python"))     #False
print(str.endswith("language"))   #True
'''


'''
name="bahubali"
age=40
print("my name is {} and age is {} years".format(name,age))

                               #my name is bahubali and age is 40 years
'''



'''
print("first: {1}, second: {0}".format("java","python"))

                              #first: python, second: java
'''




'''
print("name is: {name}, age is: {age}".format(name="bahu",age=30))
   
                                   #name is: bahu, age is: 30
'''



'''
str="bahubali"
print(sorted(str))
result="".join(sorted(str))   #['a', 'a', 'b', 'b', 'h', 'i', 'l', 'u']
print(result)                 #aabbhilu
'''


'''
str=input("Enter string ")
n=len(str)
print(n)                          #7
i=0
while i<n:
    print(str[i],end="")          #deepika
    i+=1 
    
    
print()
i=n-1
while i>=0:
    print(str[i],end="")         #akipeed
    i-=1
    
    
print()
i=-1
while i>=-n:
    print(str[i],end="")         #akipeed
    i=i-1
    
print()    
for i in str:
    print(i,end="")              #deepika
    
print()    
print("aree ye last haii")       #aree ye last haii
for i in range(len(str)):
    print(str[i],end="")         #deepika
    
print()    
print("umesh")                   #umesh
for i in range(n-1,-1,-1):
    print(str[i],end="")         #akipeed
'''


'''
str=input("Enter the string ")  #umesh patidar
result=""
i=0
while i<len(str):
    if i==0 or str[i-1]==" ":
        upper=ord(str[i])-32
        result=result+chr(upper)
    else:
        result=result+str[i]
    i+=1
print(result)    #Umesh Patidar
'''



'''
str=input("Enter the string ")  
result=""
i=0
while i<len(str):
    if str[i]>="a" and str[i]<="z":
        if i==0 or str[i-1]==" ":
            upper=ord(str[i])-32
            result=result+chr(upper)
        else:
            result=result+str[i]
        
    else:
        result=result+str[i]
    i+=1    
print(result)   
'''




'''
str=input("Enter the string ")
result=""
words=str.split()
for w in words:
    result=result+w.capitalize()+" "
print(result)    
'''


'''
str=input("Enter the string ")
result=str.title()
print(result)
'''



'''
s1=input("Enter first strung ")
s2=input("Enter second string ")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")
else:
    print("NOT ANAGRAM")
'''


s1=input("Enter first string ")
s2=input("Entetr second string ")
if len(s1)!=len(s2):
    print("NOT ANAGRAM")
else:
    f=1
    for ch in s1:
        if s1.count(ch)!=s2.count(ch):
            f=0
            break
    if f==1:
        print("ANAGRAM")
            
    else:
        print("NOT ANAGRAM")