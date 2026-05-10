'''
a=10
b=5
c=15
print(a>b and a<c)
print(a>b or a<c)
print(not a==b)
'''





'''
a=True
b=False
c=True
print(not a and b)
print(a or b and c)
print((a or b) and c)
'''




'''
x=5
y=10
z=15
print(x<y and y<z or z==20)
'''




'''
a=True
b=False
print(a or 1/0)			# True
print(a and 1/0)		# IndentationError: unexpected indent
print(1/0 or a)			# IndentationError: unexpected indent
'''






'''
print(0 and 20)
print(1 and 20)
print(10 and 20)
print(-5 and 20)
print(1 and "deepika")
print(10 and 0 and 30)
print("" and "katappa")
print("deepika" and "katappa")
print(True and "katappa")
print(False and "katappa")
'''








'''
print(10 or 20)
print(-5 or 20)
print(0 or 20)
print(True or 20)
print(False or 20)
print("hello" or "world")
print("" or "world")
print([10,20] or [30,20])
print([] or [])
print(None or 10)
'''






'''
print(not 10)
print(not 0)
print(not "")
print(not[])
print(not None)
'''




'''
print("welcome")
if True:
print("welcome")
'''
			# IndentationError: expected an indented block after 'if' statement on line 99



'''
print("Welcome")
if True:
    print("Welcome")
print("done")
'''



'''
print("welcome")
a=10
b=20
if a>b:
    print("a is greater")
    print("a is greater than 5 also")
if b>a:
    print("b is greater")
    print("b is also positive")
print("done")
'''



'''
print("Welcome")
a=int(input("Enter the number"))
if a%2==0:
    print("a is even")
if a%2!=0:
    print("a is odd")
print("done")
'''




print("welcome")
a= int(input("Enter the number"))
if True:
    print("a is even")
     print("a is even")

				# IndentationError: unexpected indent