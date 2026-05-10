'''
s=input("Enter the string ")
for ch in s:
    if ch in "aeiouAEIOU":
        continue
    print(ch,end="")
'''



'''
s=input("Enter the string ").lower()
for ch in s:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" :
        continue
    print(ch,end="")
'''



'''
for i in range(1,11):
    if i==5:
        pass
    elif i==9:
        break
    elif i%2==0:
        continue
    else:
        print(i)
'''



'''
for i in range(1,10):
    print(i)
else:
    print("No break")
'''



'''
for i in range(1,10):
    print(i)
    if i==20:
        break
else:
    print("No Break")
'''



'''
for i in range(1,10):
    print(i)
    if i==5:
        break
else:
    print("No Break")
'''






'''
n=int(input("Enter the number"))
if n<=1:
    print("Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime hai")        
'''



'''
n=int(input("Enter the number"))
if n<=1:
    print("Not Prime")
else:
    for i in range(2,n//2+1):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime hai")   
'''




'''
number=[2,4,6,8,10]
target=5
for i in number:
    if i==target:
        print("banda mil gaya ")
        break
else:
     print("banda Not found")        
'''





attempts=0
while attempts<3:
    password=input("Enter the password")
    if password=="admin":
        print("granted")
        break
    attempts+=1
else:
    print("To many failed attempts ")



