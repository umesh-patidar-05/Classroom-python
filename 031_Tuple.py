print("04/june/2026")


'''
t=(1,2,3)
print(t) #(1, 2, 3)
'''


'''
t1=1,2,3
print(t1)  #(1, 2, 3)
'''


'''
t=()
print(t)  #()
'''


'''
t=tuple([1,2,3])
print(t)        #(1, 2, 3)
print(type(t))  #<class 'tuple'>
'''



'''
t=tuple("umesh")
print(t)        #('u', 'm', 'e', 's', 'h')
print(type(t))  #<class 'tuple'>
'''



'''
t=(10)
print(t)        #10
print(type(t))  #<class 'int'>
'''


'''
t1=(10,)
print(t1)       #(10,)
print(type(t1)) #<class 'tuple'>
'''


'''
t=(10,20,30)
print(t[0])    #10
print(t[-1])   #30
print(t[1:3])  #(20,30)
'''


'''
t=(10,20,30)
t[0]=99
print(t)
#TypeError: 'tuple' object does not support item assignment
'''


'''
t=([10,20],30)
print(id(t))    #140182602036416
t[0].append(4)
print(t)        #([10, 20, 4], 30)
print(id(t))    #140182602036416
'''


'''
t=10,20,30
print(t)  #(10, 20, 30)
'''


'''
a,b,c=(10,20,30)
print(a)  #10
print(b)  #20
print(c)  #30
'''


'''
a,*b=(10,20,30)
print(a)  #10
print(b)  #[20, 30]
'''



'''
a,*b,c=(10,20,30,40,50)
print(a)  #10
print(b)  #[20, 30, 40]
print(c)  #50
'''



'''
t=(10,10,30,40,50)
print(t)            #(10, 10, 30, 40, 50)
print(t.count(10))  #2
'''



'''
t=(10,20,30,40,50)
print(t)            #(10, 20, 30, 40, 50)
print(t.index(20))  #1
print(max(t))       #50
print(min(t))       #10
print(sum(t))       #150
'''



'''
t=(10,20,30,40,50)
print(t)
for i in t:
    print(i)

#output
#10
#20
#30
#40
#50
'''



'''
t=(10,20,30,40,50)
print(t)
for i in range(len(t)):
    print(t[i])

#(10, 20, 30, 40, 50)
#10
#20
#30
#40
#50
'''    



'''
t1=(10,20,30,40,50)
t2=(39,100)
print(t1+t2)  #(10, 20, 30, 40, 50, 39, 100)
'''


'''
t1=(10,20)
print(t1*3)  #(10, 20, 10, 20, 10, 20)
'''



'''
t1=((10,20),(30,40))
print(t1)    #((10, 20), (30, 40))
print(t1[0]) #(10, 20)
print(t1[1]) #(30, 40)
'''



'''
id=int(input("Enter id "))
name=input("Enter name ")
salary=float(input("Enter salary "))
employee=(id,name,salary)
print("Employee details: ")
print("ID",employee[0])
print("NAME",employee[1])
print("Salary",employee[2])
'''



'''
t=(10,20,30,40)
print(20 in t)     #True
print(50 not in t) #True
'''


'''
t1=(1,2,8)
t2=(1,2,4)
print(t1<t2)  #False
'''


'''
t1=(1,2,8)
del t1
print(t1)  #NameError: name 't1' is not defined
'''



'''
t1=(1,2,8)
print(t1)
l=list(t1)
print(l)
'''



'''
t1=(11,22,8)
print(t1)          #(11, 22, 8)
print(sorted(t1))  #[8, 11, 22]
'''



import sys 
t1=("abc","xyz","www")
print(t1)
print(sys.getsizeof (t1))
t2=["abc","xyz","www"]
print(t2)
print(sys.getsizeof (t2))
 