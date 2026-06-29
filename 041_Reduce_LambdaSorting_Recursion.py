print("22/june/2026")




'''
from functools import reduce
def add(x,y):
    return x+y
numbers= [1,2,3,4,5,6]
result=reduce(add,numbers)
print(result)   #21
'''




'''
from functools import reduce
def add(x,y):
    return x+y
numbers= [1,2,3,4,5,6]
result=reduce(add,numbers,100)
print(result)   #121
'''




'''
from functools import reduce
numbers= [1,2,3,4,5,6]
result=reduce(lambda x,y:x+y ,numbers)
print(result)   #21
'''




'''
from functools import reduce
numbers= [1,2,3,4,5,6]
result=reduce(lambda x,y:x*y ,numbers,10)
print(result)   #7200
'''




'''
from functools import reduce
numbers=[11,2,333,4,5,6]
result=reduce(lambda x,y: x if x>y else y, numbers)
print(result)   #333
'''




'''
numbers=[5,2,8,6,7]
a=sorted(numbers)
print(a)  #[2, 5, 6, 7, 8]

b=sorted(numbers, reverse=True)
print(b)   #[8, 7, 6, 5, 2]

x=sorted(numbers, key= lambda x:x) 
print(x)  #[2, 5, 6, 7, 8]
'''




'''
names=["hi","bye","deepika","rashmika","ab"]
a=sorted(names)
print(a)  #['ab', 'bye', 'deepika', 'hi', 'rashmika']

b=sorted(names, reverse=True)
print(b)  #['rashmika', 'hi', 'deepika', 'bye', 'ab']

x=sorted(names,key=lambda x:len(x))
print(x)   #['hi', 'ab', 'bye', 'deepika', 'rashmika']
'''



'''
students=[("deepika",30),("vaibhavi",15),("virat",35)]
s1=sorted(students)
print(s1)   #[('deepika', 30), ('vaibhavi', 15), ('virat', 35)]

s2=sorted(students, key=lambda student: student[1])
print(s2)   #[('vaibhavi', 15), ('deepika', 30), ('virat', 35)]
'''


'''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

def main():
    x=fact(5)
    print(x)  #120
main()    
'''




'''
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

def main():
    n=int(input("Enter n: "))  #5
    x=sum(n)
    print(x)  #15
main()    
'''




'''
def pow(b,p):
    if p==0:
        return 1
    return b*pow(b,p-1)

def main():
    x=pow(2,5)
    print(x)  #32
main()    
'''




def count(n):
    if n==0:
        return 0
    return 1+count(n//10)

def main():
    x=count(12345)
    print(x)  #5
main()    