'''
s=1
while s<=3:
    print("Student",s)
    subject=1
    while subject<=5:
        print("subject",subject,end=" ")
        subject=subject+1
    s=s+1
    print()
'''



'''
s=1
while s<=3:
    print("Student",s)
    subject=1
    while subject<=5:
        print("Subject",subject,end=" ")
        chapter=1
        while chapter<=4:
            print("chapter",chapter,end=" ")
            chapter=chapter+1
        print() 
        subject=subject+1
    s=s+1 
    print()
'''



'''
for s in range(1,4):
    print("student",s)
    for subject in range(1,6):
        print("Subject",subject,end=" ")
        for chapter in range(1,5):
            print("chapter",chapter,end=" ")
        print()
    print()    
'''



'''
for s in range(1,4):
    print("Student",s)
    subject=1
    while subject<=5:
        print("subject",subject,end=" ")
        subject+=1
    print()    
'''



'''
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
while x<=y:
    n=x
    flag=True
    if n>1:
        i=2
        while i<n:
            if n%i==0:
                flag=False
                break
            i+=1
        if flag==True:
            print(n)
    x+=1        
'''

    
    
 

'''
x=int(input("Enter first number "))
y=int(input("Enter second number "))
While x<=y:
    n=x
    if n>1:
        i=2
        while i<n:
            if n%i==0
                break
            i+=1
        else:
           print(n)
    x+=1       
'''



'''
x=int(input("Enter first number "))
y=int(input("Enter second number "))
for n in range(x,y+1):
    temp=n
    power=len(str(n))
    total=0
    while temp>0:
        digit=temp%10
        total=total+digit**power
        temp=temp//10
    if total==n:
        print(n)
'''





x=int(input("Enter first number "))
y=int(input("Enter second number "))
for n in range(x,y+1):
    i=1
    while i<11:
        print(n*i,end=" ")
        i+=1
    print()    