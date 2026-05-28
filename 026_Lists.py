print("28/may/26")



'''
data=input("enter").split()   #10 5.5 umesh patel
print(data)                   #['10', '5.5', 'umesh', 'patel']       
data[0]=int(data[0])          
data[1]=float(data[1])           
print(data)                   #[10, 5.5, 'umesh', 'patel']   
'''




'''
print("Enter id, name and marks ")  
id,name,marks=input().split()       
data=[int(id),name,float(marks)]    #20 umesh 4.5
print(data)   #[20, 'umesh', 4.5]
'''





'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)

sum=0
for i in arr:
    sum=sum+i
print(sum)    
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)

sum=0
i=0 
while i<len(arr):
    sum=sum+arr[i]
    i+=1
print(sum)    

    #Enter the size of 5
    #Enter element 1
    #Enter element 2
    #Enter element 3
    #Enter element 4
   #Enter element 5
   #[1, 2, 3, 4, 5]

'''



'''
n=int(input("Enter the size of list "))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)    

sum=0
i=0
while i<len(arr):
   sum=sum+arr[i]
   i+=2
print(sum)   
'''




'''
n=int(input("Enter the size of list "))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)    

sum=0
for i in range(0,n,2):
    sum=sum+arr[i]
print(sum)    
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)    

sum=0
for i in range(n):
    if arr[i]%2==0:
        sum=sum+arr[i]
print(sum)
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)

max=arr[0]
i=1
while i<len(arr):
    if arr[i]>max:
        max=arr[i]
    i+=1    
print(max)
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)

max=0
for i in arr:
    if i>max:
        max=i
print(max)        
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)

max=0
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)        
'''




'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)
max=0
for i in arr:
    if i>max:
        max=i
print(max)        
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)        
arr=unique
print(arr)
'''




'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)
unique=[]
i=0
while i<len(arr):
    if arr[i] not in unique:
        unique.append(arr[i])
    i+=1    
print(unique)        
arr=unique
print(arr)
'''



'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>1:
        arr.remove(i)
print(arr)                
'''




'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)        
arr=unique
arr.sort()
print(arr)
print(arr[-2])
'''





'''
n=int(input("Enter size of list: "))
arr=[]
for i in range(n):
    x=int(input("enter element "))
    arr.append(x)
print(arr)
even=[]
odd=[]
for i in arr:
   if i%2==0:
       even.append(i)
   else:
       odd.append(i)    
print(even)
print(odd)
'''



'''
n1=int(input("Enter size of list1: "))
arr1=[]
for i in range(n1):
    x1=int(input("enter element "))
    arr1.append(x1)
print(arr1)


n2=int(input("Enter size of list2: "))
arr2=[]
for i in range(n2):
    x2=int(input("enter element "))
    arr2.append(x2)
print(arr2)


res=[]
for i in arr1:
    if i in arr2:
        res.append(i)
print(res)            
'''


