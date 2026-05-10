'''
n=int(input("Enter the number"))
f=1
for i in range(1,n+1):
    f=f*i
print("factorial is ",f)
'''




'''
n=int(input("Enter the number"))
f=1
for i in range(n,0,-1):
    f=f*i
print("factorial is ",f)
'''




'''
import math
n=int(input("enter the number"))
print("factorial is ",math.factorial(n))
'''





'''
n=int(input("enter the number"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print("sum is ", sum)
'''




'''
n=int(input("enter the number"))
sum=0
i=1
while i<n:
    if n%i==0:
        sum=sum+i
    i+=1
if n==sum:
    print(n,"is perfect")
else:
    print(n,"is not perfect")
'''





'''
n=int(input("enter the number"))
sum=0
i=1
while i<=n//2:
    if n%i==0:
        sum=sum+i
    i+=1
if n==sum:
    print(n,"is perfect")
else:
    print(n,"is not perfect")
'''





'''
n=int(input("enter the number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print(n,"is perfect")
else:
    print(n,"is not perfect")
'''



'''
n=int(input("Enter the number"))
count=0
for i in str(n):
    count=count+1
print("count is ",count)
'''




'''
n=int(input("enter the number"))
rev=0
while n>0:
    rem=n%10
    rev = rev*10+rem
    n=n//10
print("reverse number is ",rev)
'''






'''
n=int(input("Enter the number"))
rev=0
while n>0:
    rem=n%10
    print(rem,end="")
    n=n//10
'''
				  # not good approach




'''
n=input("enter the number ")
rev=""
for d in n:
    rev=d+rev
print("reverseal number is ",rev)
'''                                 






'''
n=int(input("enter the number"))
rev=0
temp = n
while n>0:
    rem=n%10
    rev = rev*10+rem
    n=n//10
if rev==temp:
    print("palindrome")
else:
    print("Not palindrome")
'''




'''
n=int(input("Enter the number"))
temp=n
sum=0
while n>0:
    rem=n%10
    sum= sum+rem**3
    n=n//10
if sum==temp:
    print("armstrong")
else:
    print("Not armstrong")
'''





n=int(input("Enter the number"))
t=len(str(n))
temp=n
sum=0
while n>0:
    rem=n%10
    sum= sum+rem**t
    n=n//10
if sum==temp:
    print("armstrong")
else:
    print("Not armstrong")