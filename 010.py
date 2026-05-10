                # BREAK

'''
i=1
while i<10:
    print(i)
    if i==5:
        print("Banda mil gaya break keyword")
        break
    i+=1
'''


'''
for i in range(1,11):
    print(i)
    if i==5:
        print("Use of break")
        break
'''



'''
while True:
    password=input("Enter password ")
    if password=="admin":
        print("access granted")
        break
    else:
        print("Enter password again")
'''



'''
n=int(input("Enter the number"))
if n<=1:
    print("Not Prime")
else:
    x=0
    i=2
    while i<n:
        if n%i==0:
            x=1
            break
        i+=1
if x==0:
    print("prime")
else:
    print("Not prime")    
'''




'''
n=int(input("Enter the number"))
for i in range(1,11):
    if n*i>50:
        break
    print(n*i)
'''




'''
while True:
    print("1 say hello")
    print("2 good bye")
    print("3 Exit")    
    choice=int(input("Enter the choice"))
    if choice==1:
        print("Hello deeika")
    elif choice==2:
        print("Good bye deepika")
    else:
        print("wrong choice")
        break
'''





                # continue
                
                
      

'''      
i=0
while i<=10:
    i+=1
    if i==5:
        print("aree continue is there ")
        continue
    print(i)
print("Done with the loop")
'''




'''
i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)
print("Done with the loop")
'''




while True:
    n=int(input("Enter the number"))
    if n<0:
        continue
    elif n==10:
        break
    else:
        print("Entered number is ",n)
print("done with loop")