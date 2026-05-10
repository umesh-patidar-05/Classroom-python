
'''
i=1
while i<=5:
    print(i)
    i=i+1
print("Out of loop")
'''




'''
i=10
while i>=1:
    print(i)
    i=i-1
print("out of loop")
'''




'''
i=20
while i>=10:
    print(i)
    i=i-3
print("out of loop")
'''




'''
n=int(input("Enter value of n"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("Sum of n natural number is ",sum)
'''



'''
n=int(input("Enter value of n "))
i=2
while i<=n:
    print(i,end=" ")
    i+=2
print("out of loops")
'''




'''
n=int(input("Enter the value of n"))
i=1
while i<=10:
    print(n*i)
    i+=1
print("Out of loop")
'''






'''
n=int(input("enter value of n "))
sum=0
while n>0:
    rem=n%10
    sum = sum+rem
    n=n//10
print("sum of digits is ",sum)
'''






'''
n=int(input("enter value of n "))
count=0
while n>0:
    count=count+1
    n=n//10
print("Count is ",count)
'''




'''
n1= int(input("enter the value of n1 "))
n2 = int(input("enter the value of n2 "))
if n1<n2:
    while n1<=n2:
        print(n1)
        n1=n1+1
else:
    while n1>=n2:
        print(n1)
        n1=n1-1
print("Out")
'''





'''
s="deepika padukone"
for x in s:
    print(x,end="")
print("out of loop")
'''





'''
s = input("enter string ")
count=0
for  x in s:
    count=count+1
print("count of characters ",count)
'''




'''
s=input("enter String = ")
i=0
for x in s:
    print("the character present at ",i,"is",x)
    i=i+1
print("done")
'''






'''
for i in range(10):
    print(i)
print("done")
'''







'''
for i in range(10,20):
    print(i)
print("done")
'''




'''
for i in range(3,9,2):
    print(i)
print("done")
'''





'''
for i in range(2.5,9,2):
    print(i)
print("done")
'''
                                                           # TypeError: 'float' object cannot be interpreted as an integer







'''
for i in range(10,2,-1):
    print(i)
print("done")
'''







'''
for i in range(10,2,-3):
    print(i)
print("done")
'''




'''
n=int(input("Enter number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum is ", sum)
'''






'''
n=int(input("enter number"))
for i in range(1,11):
    print(n*i)
print("out of loop")
'''






