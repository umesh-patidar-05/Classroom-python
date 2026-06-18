print("18/june/2026")


'''
n=[2,4,6,7,8]
r=map(lambda x:x*x, n)
print(list(r))  #[4, 16, 36, 49, 64]
'''  


'''
l=["yogita", "vaishnavi", "thapaji", "deepesh"]
def convert(s):
    return s.capitalize()
r=map(convert,l) 
print(list(r))    #['Yogita', 'Vaishnavi', 'Thapaji', 'Deepesh']
'''



'''
l=["yogita", "vaishnavi", "thapaji", "deepesh"]
r=map(lambda a:a.capitalize(), l)
print(list(l))  #['yogita', 'vaishnavi', 'thapaji', 'deepesh']
'''


'''
l=["yogita", "vaishnavi", "thapaji", "deepesh"]
r=map(lambda a:a.upper(),l)
print(list(r))  #['YOGITA', 'VAISHNAVI', 'THAPAJI', 'DEEPESH']
'''


'''
l=["yogita", "vaishnavi", "thapaji", "deepesh"]
r=map(lambda a:len(a),l)
print(list(r))  #[6, 9, 7, 7]
'''


'''
l1=[10,20,30]
l2=[100,200,300]
def add(a,b):
    return a+b
r=map(add,l1,l2)
print(list(r))    #[110, 220, 330]
'''


'''
l1=[10,20,30]
l2=[100,200,300]
r=map(lambda a,b:a+b,l1,l2)
print(list(r))  #[110, 220, 330]
'''


'''
l1=[10,20,31,32]
r=map(lambda a:"even" if a%2==0 else "odd" ,l1)
print(list(r))   #['even', 'even', 'odd', 'even']
'''


'''
l1=[92,60,31,56]
r=map(lambda a: "A" if a>75else "B" if a>60 else "c" if a>=40 else "f",l1)
print(list(r))  #['A', 'c', 'f', 'c']
'''


'''
l=[92,60,31,56,77,43]
def fun(x):
    return x%2==0
r=filter(fun,l)
print(list(r))    #[92, 60, 56]
'''



'''
l=[92,60,31,56,77,43]
r=filter(lambda x: x%2==0,l)
print(list(r))  #[92, 60, 56]
'''



'''
l1=["deepika", "mashmika", "mahesh", "mahi"]
r=filter(lambda x: x.startswith("m"),l1)
print(list(r))  #['mashmika', 'mahesh', 'mahi']
'''



'''
l1=["deepika", "mashmika", "mahesh", "mahi"]
r=filter(lambda x: len(x)>5,l1)
print(list(r))  #['deepika', 'mashmika', 'mahesh']
'''



'''
l1=["deepika", "mashmika", "mahesh", "mahi"]
r=map(lambda x: len(x)>5,l1)
print(list(r)) #[True, True, True, False]
'''



'''
l=["1","2","3","4","5","6","7","8","9"]
r=map(lambda x:int(x), l)
print(list(r))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''



'''
l1=["deepika", "", "mashmika", "mahesh", "mahi", ""]
r=filter(lambda x: len(x)>0, l1)
print(list(r))   #['deepika', 'mashmika', 'mahesh', 'mahi']
'''


'''
l1=["deepika", "", "mashmika", "mahesh", "mahi", ""]
r=filter(lambda x:x ,l1)
print(list(r))  #['deepika', 'mashmika', 'mahesh', 'mahi']
'''



'''
l1=[1,2,3,4]
r=filter(lambda x:x%2==0, (map(lambda a:a*a, l1)))
print(list(r))  #[4, 16]
'''




l=["ranu", "shanu", "bhola"]
r=map(lambda x:x[::-1],l)
print(list(r))  #['unar', 'unahs', 'alohb']



