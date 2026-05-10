
'''
a=10
b=-10
c=999999999999999999999999999999999999999999999
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
'''



'''
c=9999_99999999_99999999
print(c)
'''


'''
c=_999
print(c)
'''
                 # NameError: name '_999' is not defined

'''
c=99_45_597_
print(c)
'''                  # SyntaxError: invalid decimal literal



'''
a=0b1011
print(a)
print(type(a))
b=0B1111
'''


'''
b=-0b1111
print(b)
print(type(b))
'''



'''
a=0o137
print(a)
print(type(a))
b=0O17
print(b)
print(type(b))
'''

'''
a=0xABC
print(a)
print(type(a))
'''

'''
b=0XA
print(b)
print(type(b))
'''

'''
a=OXdeepika
print(a)
print(type(b))
'''                    
                       # NameError: name 'OXdeepika' is not defined

'''
print(bin(15))
print(bin(0o127))
print(oct(15))
print(hex(15))
'''


'''
x=3.14
y=-0.0012
z=0.0
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
'''


'''
x=9344_856.546_5646
print(x)
print(type(x))
'''


'''
x=0o154.65
print(x)
print(type(x))
'''
                      # SyntaxError: invalid syntax

'''
x=0x54.65
print(x)
print(type(x))
'''
                     # SyntaxError: invalid syntax



'''
x=5/2
print(x)
print(type(x))
'''


'''
x=5//2
print(x)
print(type(x))
'''


'''
import math
a=3.7
print(math.ceil(a))
print(math.floor(a))
b=-5.6
print(abs(b))
print(round(a))
'''

'''
import math
a=3.7466578678997
print(round(a,2))
print(round(a,3))
'''

'''
import math
a=1.2e2
print(a)
print(type(a))
'''


import math
a=1.2E3
print(a)
print(type(a))

