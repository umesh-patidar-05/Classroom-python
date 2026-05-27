'''
a=[10,20,30,40,10]
print(a)    #[10, 20, 30, 40, 10] 
a.remove(10)
print(a)    #[20, 30, 40, 10]
'''




'''
a=[10,20,30,40,10]
print(a)   #[10, 20, 30, 40, 10]
a.pop()
print(a)   #[10, 20, 30, 40]
a.pop(1)
print(a)   #[10, 30, 40]
'''



'''
a=[10,20,30,40,10]
a.pop(7)    #IndexError: pop index out of range
'''



'''
a=[10,20,30,40,10]
print(a)     #[10, 20, 30, 40, 10]
x=a.pop(1)  
print(a)     #[10, 30, 40, 10]
print(x)     #20
'''




'''
a=[10,20,30,40,10]
y=a.remove(30)
print(y)      #None
'''




'''
a=[10,20,30,40,10]
print(a)        #[10, 20, 30, 40, 10]
print(len(a))   #5
a.clear()
print(a)        #[]
print(len(a))   #0
'''





'''
a=[10,20,30,40,10]
print(a)   #[10, 20, 30, 40, 10]
del a[1]
print(a)   #[10, 30, 40, 10]
'''




'''
a=[10, 20, 30, 40, 10]
print(a)       #[10, 20, 30, 40, 10]
del a[1:4]
print(a)       #[10, 10]
'''




'''
a=[10, 20, 30, 40, 10]
print(a)   #[10, 20, 30, 40, 10]
del a
print(a)   #NameError: name 'a' is not defined
'''




'''
#wrong method
a=[10, 20, 30, 40]
for i in a:
    if i%2==0:
        a.remove(i)
print(a) #[20, 40]        
'''




'''
a=[10, 21, 30, 41, 43]
for i in a[:]:
    if i%2==0:
        a.remove(i)
print(a)     #[21, 41, 43]        
'''



'''
a=["abe","axy","www","rrr"]
for i in a[:]:
    if i.startswith("a"):
        a.remove(i)
print(a)     #['www', 'rrr']
'''



'''
a=["deepika", "rashmika", "www", "rrr"]
name=input("Enter name ")  #deepika
if name in a:
    a.remove(name)
else:
    print("name not found")
print(a)    #['rashmika', 'www', 'rrr']
'''



'''
a=["deepika", "rashmika", "www", "rrr"]
b=a
name=input("Enter name ")
if name in a:
    a.remove(name)
else:
    print("name not found")
print(a)   #['rashmika', 'www', 'rrr']
print(b)   #['rashmika', 'www', 'rrr'] 
'''




'''
a=["deepika", "rashmika", "www", "rrr"]
b=["deepika", "rashmika", "www", "rrr"]
name=input("Enter name ")
if name in a:
    a.remove(name)
else:
    print("name not found")
print(a)   #['rashmika', 'www', 'rrr']
print(b)   #['deepika', 'rashmika', 'www', 'rrr'] 
'''



'''
a=["deepika", "rashmika", "www", "rrr"]
print(a.index("deepika"))  #0
print(a.index("deepika1")) #ValueError: list.index(x): x not in list
'''



'''
a=["deepika", "rashmika", "www", "rrr", "deepika"]
print(a.count("deepika"))  #2
'''




'''
b=[10,20,30,10,10]
print(b.count(10))    #3
'''




'''
a=["deepika", "rashmika", "www", "rrr", "deepika"]
a.sort()
b=[15, 2, 30, 10, 10]
b.sort()
print(a)  #['deepika', 'deepika', 'rashmika', 'rrr', 'www']
print(b)  #[2, 10, 10, 15, 30]
'''




'''
a=["deepika", "rashmika", "www", "rrr", "deepika"]
a.sort(reverse=True)
b=[15, 2, 30, 10, 10]
b.sort(reverse=True)
print(a)  #['www', 'rrr', 'rashmika', 'deepika', 'deepika']
print(b)  #[30, 15, 10, 10, 2]
'''




'''
a=["deepika",10,20,15.34,"rashmika","www","rrr","deepika"]
a.sort()
print(a)  #TypeError: '<' not supported between instances of 'int' and 'str'
'''



'''
a=["deepika123", "rashika", "www1", "rrr","deepika"]
a.sort(key=len)
print(a)   #['rrr', 'www1', 'rashmika', 'deepika', 'deepika123']
'''



'''
a=[-10, -30, 5, 6, 7, -8]
a.sort(key=abs)
print(a)  #[5, 6, 7, -8, -10, -30]
'''



'''
a=[-10, -30, 5, 6, 7, -8]
a.sort(key=abs,reverse=True)
print(a)  #[-30, -10, -8, 7, 6, 5]
'''


'''
a=["Deepika", "deepika", "Rashmika"]
a.sort(key=str.lower)
print(a)  #['Deepika', 'deepika', 'Rashmika']
'''



'''
a=[11,3,4,24,9]
b=sorted(a)
print(a)   #[11, 3, 4, 24, 9]
print(b)   #[3, 4, 9, 11, 24]
'''



'''
a=["deepika", "rashmika", "www", "rrr", "deepika"]
b=sorted(a)
c=[15, 2, 30, 10, 10]
d=sorted(c)
print(a)  #['deepika', 'rashmika', 'www', 'rrr', 'deepika']
print(b)  #['deepika', 'deepika', 'rashmika', 'rrr', 'www']
print(c)  #[15, 2, 30, 10, 10]
print(d)  #[2, 10, 10, 15, 30]
'''



'''
a="deepika"
b=sorted(a)
print(b)
'''


'''
a=[11,3,4,24,9]
a.reverse()
print(a)
'''



'''
a=[11,3,4,24,9]
b=a.copy()
print(a)     #[11, 3, 4, 24, 9]
print(b)     #[11, 3, 4, 24, 9]
a[0]=99
print(a)     #[99, 3, 4, 24, 9]
print(b)     #[11, 3, 4, 24, 9]
print(id(a)) #1708417856256
print(id(b)) #1708417740736
'''



'''
a=[11,3,4,24,9]
print(max(a))    #24
'''



'''
a=["aaaaa", "bb", "ccc"]
print(max(a))  #ccc
'''



'''
a=[10,8,77]
print(min(a))   #8
'''



'''
a=[10,8,77]
print(sum(a))   #95
'''



'''
a=[10,8,77]
print(sum(a,100)) #195
'''



'''
a=["abc","xyz"]
print(sum(a))     #TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''



'''
a=[0,False,None]
print(any(a))    #False
b=[1,False,None]
print(any(b))    #True
'''



'''
a=[0,False,None]
print(all(a))      #False
b=[1,True,"hello"]
print(all(b))      #True
'''





'''
names=["abc", "xyz", "www"]
for index,value in enumerate(names):
    print("index is",index,"and",value)
                  #index is 0 and abc
                  #index is 1 and xyz
                  #index is 2 and www
'''



'''
names=["abc", "xyz", "www"]
marks=[80,90,76]
for n,m in zip(names,marks):
    print("Names ",n,"and marks ",m)
                    #Names  abc and marks  80
                    #Names  xyz and marks  90
                    #Names  www and marks  76    
'''



'''
names=["abc", "xyz", "www"]
names1=["abc","xyz","www1"]
for n,m in zip(names,names1):
    if n==m:
        print("same")
    else:
        print("Not same")
                    #same
                    #same
                    #Not same
'''




'''
names=["abc", "xyz", "www"]
price=[300,400] 
for n,m in zip(names,price):
    print(n,"->",m)
                  #abc -> 300
                  #xyz -> 400
'''


'''
a="deepika"
print(list(a))    #['d', 'e', 'e', 'p', 'i', 'k', 'a']
'''




'''
a=list(map(int,input("Enter numbers").split()))
print(a)
'''


'''
a=list(map(int,input("Enter numbers").split(",")))
print(a)
'''


'''
n=int(input("areee bhaiya enter number of elements "))
marks=[]
print("plz enter all elements")
for i in range(n):
    x=int(input())
    marks.append(x)
print(marks)    
'''


'''
n=int(input("areee bhaiya enter number of elements "))
marks=[]
print("plz enter all elements")
for i in range(n):
    x=input()
    marks.append(x)
print(marks)    
'''



n=int(input("areee bhaiya enter number of elements "))
marks=[]
print("plz enter all elements")
for i in range(n):
    x=input()
    if x.isdigit():
        x=int(x)
        marks.append(x)
    else:
        marks.append(x)
print(marks)    