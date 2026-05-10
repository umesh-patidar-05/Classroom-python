'''
a=256
b=256
print(id(a))
print(id(b))
print(a is b)
'''


'''
a=257
b=257
print(id(a))
print(id(b))
print(a is b)
'''



'''
a=int("256")
b=int("256")
print(id(a))
print(id(b))
print(a is b)
'''



'''
a=int("257")
b=int("257")
print(id(a))
print(id(b))
print(a is b)
print(a==b)
'''




'''
a="bahu"+3
'''
					# TypeError: can only concatenate str (not "int") to str


'''
a="bahu"*3
print(a)
'''


'''
a="bahu"+"3"
print(a)
'''


'''
a="bahu"*"3"
print(a)
'''


'''
a="bahu"*3.0
print(a)
'''
					# TypeError: can't multiply sequence by non-int of type 'float'



'''
a=10%0
print(a)
'''
					# ZeroDivisionError: division by zero




'''
a=10
print(a)
10 =20
'''
							# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?





'''
a=10
a-=5
print(a)
'''



'''
a=10
a+=5
print(a)
'''



'''
a=10
a*=5
print(a)
'''




'''
a=10
a/=5
print(a)
'''


'''
a=b=c=d=10
print(a,b,c,d)
'''


'''
a=5
b=10
a+=b+=2
print(a,b)
'''
			# SyntaxError: invalid syntax




'''
a=5
b=2
a+=b*3
print(a,b)
'''



'''
a=17
a//=3+1
print(a)
'''



'''
a=5
b=2
c=3
a+=b*c**2//2%3
print(a)
'''



'''
a=5
a*=-2
print(a)
'''



'''
a=5
b=2
print(a===b)
'''
				# SyntaxError: invalid syntax



'''
a=5
b=2
print(a==b)
'''



'''
a=5
b=2
print(a==b)
print(a<b)
print(a>b)
print(a!=b)
c=5
print(a<c)
print(a<=c)
print(c>=a)
print(a!=c)
'''


'''
print(5==5.0)
print(3.5>2)
'''


'''
a="deepika"
b="rashmika"
print(a<b)
'''


'''
print(ord("a"))
print(ord("A"))
print(ord("@"))
'''


'''
print("apple"=="apple")
print("apple"=="Apple")
'''



'''
a="deepika"
b="rashmika"
print(a<b)
'''




'''
a="ydeepika"
b="rashmika"
print(a<b)
'''



'''
a="Bdeepika"
b="Arashmika"
print(a<b)
'''


'''
a="deeA"
b="deeB"
print(a<b)
'''


'''
a="dog"
b="cat"
print(a>b)
'''


'''
print(5=="5")
'''


'''
a="True"
b="False"
print(a>b)
'''


'''
a="True"
b=False
print(a>b)
'''
				# TypeError: '>' not supported between instances of 'str' and 'bool'




'''
print(5=="5")
print(5>"5")
'''



'''
print(True==True)
print(True==False)
print(False!=True)
print(True>False)
print(True<False)
print(False<=True)
print(True>=False)
print(0==False)
print(1==True)
print(2==True)
print(""==False)
print([]==False)
'''



'''
print(5>2==3)
'''

'''
print(10<20<30)
'''


'''
print(3<20!=2<5)
'''

'''
print(3<4!=2<5!=6==4>7!=3)
'''


'''
a=10==20==30==40
print(a)
'''


'''
a=10==5+5==3+7==2*5
print(a)
'''


'''
a="a"==97
print(a)
'''


'''
a=10==10.0
print(a)
'''



'''
a=5>2 and 3>1
print(a)
'''



a=5>20 and 3>1
print(a)