print("08/june/2026")



'''
s={1,2,3,3,4}
print(s)  #{1, 2, 3, 4}
s.clear()
print(s)  #set()
'''



'''
s1={1,2,3,3,4}
s2={3,4,6,7,8,9,9}
print(s1)           #{1, 2, 3, 4}
print(s2)           #{3, 4, 6, 7, 8, 9}
print(s1|s2)        #{1, 2, 3, 4, 6, 7, 8, 9}
print(s1.union(s2)) #{1, 2, 3, 4, 6, 7, 8, 9}
'''


'''
sports={"thapaji", "aman"}
cultr={"krishna", "kuldeep", "aman"}
print(sports|cultr)   #{'krishna', 'aman', 'thapaji', 'kuldeep'}
'''



'''
a={1,2,3}
b={2,3,4,5}
print(a & b)   #{2, 3}
print(a.intersection(b))  #{2, 3}
'''


'''
sports={"thapaji", "aman"}
cultr={"krishna", "kuldeep", "aman"}
print(sports & cultr)  #{'aman'}
'''



'''
a={1,2,3}  
b={2,4}
print(a-b)   #{1, 3}
print(a.difference(b))  #{1, 3}
'''


'''
a={1,2,3}
b={2,4}
print(a-b)  #{1, 3}
print(b-a)  #{4}
'''


'''
s={"thapaji", "aman","kuldeep"}
c={"krishna", "aman"}
print(s - c)    #{'kuldeep', 'thapaji'}
'''


'''
s={"thapaji", "aman","kuldeep"}
c={"krishna", "aman"}
print(s^c)   #{'kuldeep', 'krishna', 'thapaji'}
print(s.symmetric_difference(c))  #{'kuldeep', 'krishna', 'thapaji'}
'''




'''
s={"thapaji","aman", "kuldeep"}
c={"krishna", "aman", "deepika", "rashmika", "KANAK"}
print(s<=c)            #False
print(s.issubset(c))   #False
'''



'''
s={"thapaji","aman", "kuldeep"}
c={"krishna", "aman", "deepika", "rashmika", "KANAK", "thapaji", "kuldeep"}
print(s<=c)   #True
print(s.issubset(c))  #True
'''




'''
s={"thapaji","aman", "kuldeep"}
c={"krishna","thapaji", "aman", "deepika", "kuldeep", "rashmika", "KANAK"}
print(c>=s)   #True
print(c.issuperset(s))  #True
'''



'''
s={"thapaji","aman", "kuldeep", "dipu"}
c={"krishna","thapaji", "aman", "deepika", "kuldeep", "rashmika", "KANAK"}
print(c>=s)   #False
print(c.issuperset(s)) #False
'''



'''
s={1,2}
c={3,4}
print(s.isdisjoint(c))  #True
'''



'''
s={1,2,3}
c={3,4,5}
s.update(c)
print(s)  #{1, 2, 3, 4, 5}
print(c)  #{3, 4, 5}
'''



'''
s={1,2,3}
s.update({3,4},{5,6})
print(s)  #{1, 2, 3, 4, 5, 6}
'''



'''
s={1,2,3}
c={3,4,5}
s|=c
print(s)  #{1, 2, 3, 4, 5}
'''



'''
s={1,2,3}
c={3,4,5}
s.intersection_update(c)
print(s)  #{3}
'''



'''
s={1,2,3}
c={3,4,5}
s&=c
print(s)  #{3}
'''



'''
a={1,2,3}  
print(id(a))  #1834598999968
b={2,4}
a-=b
print(a)  #{1, 3}
print(id(a)) #1834598999968
'''



'''
s={"thapaji", "aman","kuldeep"}
c={"krishna", "aman"}
s-=c
print(s)    #{'kuldeep', 'thapaji'}
'''


'''
s={"thapaji", "aman","kuldeep"}
c={"krishna", "aman"}
s.difference_update(c)
print(s)  #{'thapaji', 'kuldeep'}
'''



'''
s={"thapaji", "aman","kuldeep"} 
c={"krishna", "aman"}
s^=c
print(s)  #{'kuldeep', 'krishna', 'thapaji'}
'''



'''
a={1,2,3}  
b={2,4}
a^=b
print(a) #{1, 3, 4}
print(b) #{2, 4}
'''



'''
s={1,2,3,(88,77)}
print(s) #{(88, 77), 1, 2, 3}
'''



'''
s={[2,3,4,5]}
print(s)   #TypeError: cannot use 'list' as a set element (unhashable type: 'list')
'''



'''
s={1,2,3,4}
print(id(s))    #2615456310528
s={1,2,3,4,5}
print(id(s))    #2615456310976
'''


'''
f=frozenset([1,2,3,4,5,5,11,88,77,345,3])
print(f)  #frozenset({1, 2, 3, 4, 5, 11, 77, 88, 345})
print(type(f))  #<class 'frozenset'>
'''


'''
f1=frozenset((1,2,3,4,5,5,4,8,88,77,345,3))
print(f1)    #frozenset({1, 2, 3, 4, 5, 11, 77, 88, 345})
'''


'''
f2=frozenset("umesh patidar")
print(f2)  #frozenset({'a', ' ', 'i', 'h', 'e', 'r', 'p', 'u', 't', 'm', 'd'})
'''



'''
s={1,2,3,3}
print(id(s))  #2070711116160
s.add(99)
print(s)      #{99, 1, 2, 3}
print(id(s))  #2070711116160
'''


'''
f=frozenset([6,7,8,9])
f.add(99)
print(f)  #AttributeError: 'frozenset' object has no attribute 'add'
'''


'''
f1=frozenset([6,7,8,9])
f2=frozenset([6,77,88,9])
print(f1|f2)    #frozenset({6, 7, 8, 9, 77, 88})
print(f1&f2)    #frozenset({9, 6})
print(id(f1))   #2049113727808
f1|f2
print(f1)       #frozenset({8, 9, 6, 7})
print(id(f1))   #2049113727808
'''


'''
str=input("Enter string: ")
print(str)
words=str.split()
print(words)
u=set(words)
print("unique words are ",u)
print(len(u))
another=list(u)
print(another)
'''




str=input("Enter string: ")
print(str)
print(set(str))
if len(str)==len(set(str)):
    print("no duplicates")
else:
    print("duplicates are there ")    