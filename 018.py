'''
str="welcome"
for i in range(len(str)):
    print(i," ",str[i])
'''



'''
str="Welcome"
for i,ch in enumerate(str):
    print(i," ",ch)
'''



'''
str="Welcome"
str[1]="r"                       # TypeError: 'str' object does not support item assignment 
str[1]="r"                      
print(str)    
'''



'''
str="welcome"
str=str+"home"
print(str)
'''



'''
str="Welcome"
print(id(str))
str=str+"home"
print(id(str))
'''



'''
a="welcome"
b="welcome"        # TypeError: 'str' object does not support item assignment
a[1]='x'
'''




'''
a="Welcome"
b="Welcome"
print(id(a))
print(id(b))
'''



'''
a="Welcome"
del a[2]              # TypeError: 'str' object doesn't support item deletion
'''



'''
a="Welcome"
print(a)
del(a)
'''




'''
a="Welcome"
print(a)
del(a)
print(a)            #NameError: name 'a' is not defined
'''




'''
a="Welcome"
b="Welcome"
del(a)
print(b)
'''


'''
a="Welcome"
print(a.upper())         # WELCOME
'''



'''
a="WELCOME"
print(a.lower())         # welcome
'''


'''
a="hello guys how are uu"
print(a.capitalize())            # Hello guys how are uu
'''



'''
a="Hello Guys How Are u"
print(a.capitalize())           # Hello guys how are u
'''



'''
a="Hello guys how Are u Aree sun rahe ho"
print(a.title())                              # Hello Guys How Are U Aree Sun Rahe Ho
'''



'''
a="Hello guyss HOW Are uU"
print(a.swapcase())                          # hELLO GUYSS how aRE Uu
'''



'''
a="hello guys how th life is going on"
print(a.find("e"))       # 1
print(a.find("guys"))    # 6
print(a.find("hw"))      #-1
'''



a="hello guys how the life is going on"
print(a.rfind("e"))  #22
print(a.rfind("o"))  #33