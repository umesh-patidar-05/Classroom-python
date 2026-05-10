'''
z= 3+4j
print(z)
print(type(z))
'''


'''
x= 3+4j
y = -1+2j
z = 12.5
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
'''



'''
y = 4j
print(y)
print(type(y))
'''


'''
x= 3+4j
print(x.real)
print(x.imag)
'''


'''
x = complex(input("Enter the complex value"))
print(x.real)
print(x.imag)
'''


'''
x= 3+4i
print(x.real)
print(x.imag)
'''

				
                                #     x= 3+4i
                                #           ^
                                #      SyntaxError: invalid decimal literal
				



'''
x= 0B1111 + 4j
print(x.real)
print(x.imag)
'''



'''
x = 0B1111 + 0B1111j
print(x.real)
print(x.imag)
'''
				#  SyntaxError: invalid binary literal









'''
x= 3+4j
y = 9+5j
print(x+y)
'''




'''
x= 3+4j
y= 9+5j
print(x-y)
print(x*y)
print(x/y)
'''




'''
x = True
print(x)
print(type(x))
'''


'''
y = true
print(y)
print(type(y))
'''
				# NameError: name 'true' is not defined. Did you mean: 'True'?


'''
print(True)
print(False)
'''


'''
print(True + True)
print(False + True)
print(False + False)
print(True*10)
'''



'''
x='True'
print(x)
print(type(x))
'''



'''
import sys
a=10999999999999999999999999999999999999999
b=10.5
c=True
d=""
e=None
f= "Umesh"
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))
print(sys.getsizeof(f))
'''



'''
import sys
a="A"
b="A"*100
print(sys.getsizeof(a))
print(sys.getsizeof(b))
'''



'''
x=10
y=10
z=10
print(id(x))
print(id(y))
print(id(z))
'''


'''
x=True
y=True
z='true'
print(id(x))
print(id(y))
print(id(z))
'''



'''
x=10
print(id(x))
x = x*5
print(id(x))
'''



'''
str="Umesh"
print(id(str))
str = str + "jiiiiiiiiiiiiiii"
print(id(str))
'''



'''
a=10
b=2.5
c=a+b
print(c)
print(type(c))
'''


'''
a=10
b=2.5
d=a*b
print(d)
print(type(d))
'''


'''
a=int(10.5)
print(a)
print(type(a))
'''


'''
a=int("10")
print(a)
print(type(a))
'''


'''
a=int(True)
print(a)
print(type(a))
'''

'''
a=int("10.9")
print(a)
print(type(a))
'''
 					# ValueError: invalid literal for int() with base 10: '10.9'


'''
a= int(float("10.9"))
print(a)
print(type(a))
'''



'''
a= float(10)
print(a)
print(type(a))
'''


'''
a=float("10.5")
print(a)
print(type(a))
'''


'''
a=float("umesh")
print(a)
print(type(a))
'''
			# ValueError: could not convert string to float: 'umesh'




'''
print(float(True))
print(float(False))
'''



'''
x=float(10+2j)
print(x)
print(type(x))
'''
      		# TypeError: float() argument must be a string or a real number, not 'complex'




'''
a=10
b=12.56
c=True
d=3+4j
print(str(a))
print(type(a))
print(str(b))
print(type(b))
print(str(c))
print(type(c))
print(str(d))
print(type(d))
'''




a=str(10)
b=str(12.56)
c=str(True)
d=str(3+4j)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))

