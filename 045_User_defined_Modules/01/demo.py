'''
import mymath
print(mymath.add(10,20))   #30
print(mymath.sub(20,15))   #5
'''


'''
from mymath import add
print(add(10,20))  #30
#print(sub(20,5))  #NameError: name 'sub' is not defined. Did you mean: 'sum'?
'''


'''
import mymath as m
print(m.add(10,20)) #30
print(m.sub(10,20)) #-10
'''


'''
import mymath as m
import hello
print(m.add(10,20))  #30
print(hello.marks)   #90
'''



import hello,employee
import mymath as m
print(m.add(10,20))
print(m.sub(10,20))
print(hello.pi)
print(hello.marks)
print(employee.companyname)
print(employee.calculatesalry(500000))