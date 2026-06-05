print("05/june/2026")


'''
from collections import namedtuple
student=namedtuple("student",["name","age","city"])
s1=student("abc",24,"mumbai")
print(s1.name)  #abc
print(s1.age)   #24
print(s1.city)  #mumbai 
'''



'''
from collections import namedtuple
#account=namedtuple("account",["accno","holdername","balance"])
account=namedtuple("kuch_bhi_name",["accno","holdername","balance"])
ano=int(input("enter account number "))
name=input("Enter holder name ")
b=float(input("enter balance "))
acc=account(ano,name,b)
print(acc.accno)
print(acc.holdername)
print(acc.balance)
print(acc)
'''

	

'''
from collections import namedtuple
student=namedtuple("student",["rollno","name","marks"])
n=int(input("Enter number of students "))

students=[]
for i in range(n):
    print("Enter details ")
    r=int(input("Enter rollno "))
    n=input("enter name")
    m=float(input("enter marks"))
    students.append(student(r,n,m))
print(students)

for s in students:
    print(s)
    
for s in students:
    print(s.rollno)
    print(s.name)
    print(s.marks)
'''


'''
from collections import namedtuple
student=namedtuple("student",["rollno","name","marks"])
s1=student(121,"umesh",99)
print(student._fields)
print(s1._fields)        
'''


'''
from collections import namedtuple
student=namedtuple("student",["rollno","name","marks"])
s1=student(121,"umesh",99)
print(s1._asdict())
'''



'''
from collections import namedtuple
student=namedtuple("student",["rollno","name","marks"])
s1=student(121,"umesh",99)
print(s1)
s2=s1._replace(marks=30)
print(s1)
print(s2)
print(id(s1))
print(id(s2))
'''


'''
from collections import namedtuple
student=namedtuple("student",["rollno","name","marks"])
data=[101,"umesh",77]
s1=student._make(data)
print(s1.rollno)
print(s1.name)
print(s1.marks)
'''

'''
s={1,2,3,4,2}
print(s)
'''

'''
s={1,2,3,4,2,11,22,23,44,44}
print(s)
'''

'''
s=set([33,44,22,11])
print(s)
'''


'''
s=set()
print(s)
'''


'''
s={10,20,30,10,40}
print(s[0])    #TypeError: 'set' object is not subscriptable
'''


'''
s={10,20,30,10,40}
print(s)
for i in s:
    print(i)
'''


'''
s={10,20,30,10,40}
print(20 in s)
print(40 not in s)    
'''

'''
s={10,20,30,10,40}
print(s)
s.add(90)
print(s)
'''


'''
s={10,20,30,10,40}
print(s)
s.update([3,4,5,6])
print(s)
'''


'''
s={10,20,30,10,40}
print(s)
s.remove(20)
print(s)
'''


'''
s={10,20,30,10,40}
print(s) 
s.remove(22)
print(s)
'''


'''
s={10,20,30,10,40}
print(s)
s.discard(22)
print(s)
'''


'''
s={10,20,30,10,40}
print(s)
s.pop()
print(s)
'''


s=set()
s.pop()
print(s)  #KeyError: 'pop from an empty set'
