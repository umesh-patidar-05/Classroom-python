'''
a=[10,20,30]
a.insert(-10,9999)
a.insert(10,7777)
print(a)            #[9999, 10, 20, 30, 7777]
'''



'''
a=[10,20,30]
a.insert(-10,9999)
a.insert(10,7777)
print(a)
print(a.index(9999))   #0
print(a.index(7777))   #4
'''



'''
a=[10,20,30]
a.extend([40,50,60])
print(a)      #[10, 20, 30, 40, 50, 60]
'''
  


'''
a=[10,20,30]
b=[40,50]
a.extend(b)
print(a)    #[10, 20, 30, 40, 50]
print(b)    #[40, 50]
'''




'''
a=[10,20,30]
a.append([40,50])
print(a)             #[10, 20, 30, [40, 50]]
'''	




'''
a=[10,20,30]  
a.append("hello")
print(a)              #[10, 20, 30, 'hello']
'''


'''
a=[10,20,30]
a.extend("hello")
print(a)           #[10, 20, 30, 'h', 'e', 'l', 'l', 'o']
'''




'''
a=["deepika","rashmika","katappa"]
b=["deepika","rashmika","katappa"]
c=["DEEPIKA","RASHMIKA", "KATAPPA"]
print(a==b)   #True
print(a==c)   #False
print(a!=c)   #True

print(a is b) #False

print(id(a))  #140100110000256
print(id(b))  #139945042162176

print(id(a[0]))   #140375743002480
print(id(b[0]))   #140375743002480


print(a[0] is b[0])  #True
'''



'''
a=[50,40,30]
b=[200,24,100,30]
print(a>b)          #False
'''


'''
a=[50,40,30]
b=[50,240,100,30]
print(a>b)        #False
'''



'''
a=["deepika","rashmika"]
b=["DEEPIKA","RASHMIKA"]
print(a>b)  #True
'''



'''
a=[10,20,30,40]
a[1]=100
print(a)  #[10, 100, 30, 40]
'''



'''
a=[10,20,30,40]
print(id(a))    #140396765580480
a[1]=100
print(a)        #[10, 100, 30, 40]
print(id(a))    #140396765580480
'''



'''
a=[10,20,30,40]
a[-1]=100
print(a)    #[10, 20, 30, 100]
'''


'''
a=[10,20,30,40]
a[-10]=100
print(a)   #IndexError: list assignment index out of range
'''



'''
a=[10,20,30,40,50]
a[1:3]=[200,300]
print(a)           #[10, 200, 300, 40, 50]
'''


'''
a=[1,2,3,4,5]
a[1:4]=[10,20]
print(a)       #[1, 10, 20, 5]
'''



'''
a=[1,2,3,4,5]
print(id(a))        #140270051114176
a[:]=[10,20,30,40]
print(id(a))        #140270051114176
print(a)            #[10, 20, 30, 40]
'''



'''
a=[1,2,3,4,5,8,9]
for i in range(len(a)):
    a[i]=a[i]*2
print(a)        #[2, 4, 6, 8, 10, 16, 18]    
''' 



'''
a=[1,2,3,4,5,8,9]
i=0
while i<len(a):
    a[i]=a[i]*2
    i+=1
print(a)        #[2, 4, 6, 8, 10, 16, 18]
'''



'''
marks=[80,90,70]
print(marks)
index=int(input("Enter the index to update "))
value=int(input("Enter new marks "))
marks[index]=value
print(marks)
'''



'''
students=["deepika","rashmika","katappa"]
marks=[40,50,60]
name=input("Enter the student name ")
if name in students:
    index=students.index(name)
    newmarks=int(input("Enter new marks "))
    marks[index]=newmarks
    print(marks)
else:
    print("student not found")
'''



'''
students=["umesh","kushal","deepak","kanak"]
name=input("Enter the student name")
if name in students:
    index=students.index(name)
    newname=name.upper()
    students[index]=newname
    print(students)
else:
    print("Not name found")    
'''





a=[10,20,30]
print(id(a))    #139984162270336
print(a)        #[10, 20, 30]
a=[10,20,30]    
print(id(a))    #139984161920832
print(a)        #[10, 20, 30]  


