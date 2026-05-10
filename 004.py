
'''
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Umesh"))
print(bool([]))
print(bool([1,2,3,4]))
'''




'''
print(bool(-10))
print(bool(0.0001))
print(bool(0.0))
'''



'''
print(bool(10+20j))
print(bool(0+0j))
'''



'''
print(complex(10))
print(complex(10,20))
'''


'''
print(complex(10+20j))
print(complex("10"))
'''




'''
print(int(" 10x "))
'''
						# ValueError: invalid literal for int() with base 10: ' 10x '





'''
print(bool("false"))
'''


'''
print(bool("0"))
print(bool(0))
'''



'''
print(complex(True))
print(complex(False))
'''


'''
print(complex("abc"))
'''
					# ValueError: complex() arg is a malformed string




'''
print(complex(True,False))
'''



'''
print(type(None))
'''



'''
x
print(type(x))
'''
       					# NameError: name 'x' is not defined



'''
x=None
print(type(x))
'''


'''
print(None==0)
print(None==False)
print(None==" ")
print(None==[])
'''



'''
print(None==null)
'''
					# NameError: name 'null' is not defined



'''
print(None=="null")
print(None=="None")
print(None==None)
'''



'''
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
'''



'''
a="10"
b="20"
print(a+b)
'''	




'''
a="10"
b="20"
print(a-b)
print(a*b)
'''
				# TypeError




'''
print("Umesh"*5)
'''



'''
print("Umesh"*5.5)
'''
			# TypeError: can't multiply sequence by non-int of type 'float'




'''
print(10/2)
print(7/2)
'''



'''
print(10/0)
'''
   				# ZeroDivisionError: division by zero





'''
print(10//3)
print(9//2)
print(-13//3)
print(-17//3)
'''



'''
print(2%5)
print(-5%2)
print(5%-2)
print(-5%-2)
'''



'''
print(197%10)
print(197//10)
'''



'''
x=164
y=x%10
print(y*y)
x=x//10
y=x%10
print(y*y)
x=x//10
y=x%10
print(y*y)
'''




'''
print(2**3)
print(5**3)
print(9**0.5)
print(16**0.25)
print(27**(1/3))
'''



'''
print(2**3**2)
'''


'''
x=2+3*4
print(x)
'''


'''
x=(2+3)*4
print(x)
'''


'''
x=3+16/2**3
print(x)
'''


print(-3**2)
print((-3)**2)
print(3**-2)
print(-2**3)
print((-2)**3)