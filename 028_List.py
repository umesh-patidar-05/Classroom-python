print("01/june/2026")

 

'''
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i*2)
print(b)    
'''


'''
a=[1,2,3,4,5]
b=[i*2 for i in a]
print(b)
'''

'''
a=[1,2,3,4,5,6,7,8]
b=[i for i in a if i%2==0]
print(b)
'''


'''
a=[1,2,3,4,5,6,7,8]
b=[i for i in a if i%2==0 and i>3]
print(b)
'''



'''
a=[1,2,3,4,5,6,7,8]
b=["Even" if i%2==0 else "Odd" for i in a]
print(b)
'''


'''
a=["deepika", "virat", "RCB"]
b=[len(i) for i in a]
print(b)
'''


'''
a=["deepika", "virat", "RCB"]
b=[i for i in a if len(i)>3]
print(b)
'''


'''
a=["deepika", "virat", "RCB"]
b=[i.upper() for i in a]
print(b)
'''


'''
a=[11,2,3,4,5,6]
b=[i*10 if i%2==0 else i for i in a]
print(b)
'''


'''
a=[1,2,[3,4],5]
print(a)
print(a[2])
print(a[2][1])
'''



'''
a=[1,"virat",[3.5,True],"vaibhav"]
print(a)
print(a[2])
print(a[2][1])
'''


'''
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
  ]
print(a[0])
print(a[1])
print(a[2])  
'''




'''
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
  ]
for i in a:
    for j in i:
        print(j)
'''



'''
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
  ]
for i in a:
    for j in i:
        print(j,end=" ")
    print()
'''



'''
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
  ]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()    
'''


'''
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
  ]
for i in range(len(a)):
    print(a[i])
'''



'''
a=[
    [10,"deepika"],
    [40,50,60],
    [70],
    ["abc","xyz"]
  ]    
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")     
    print()
'''
   
   
    
'''    
a=[ 
    [10,20],
    [40,50,60],
    [70],
    ["abc","xyz"]
  ]
print(a)
a[1][0]="virat"
print(a)
'''


'''    
a=[ 
    [10,20],
    [40,50,60],
    [70],
    ["abc","xyz"]
  ]
print(a)
a[2]=[9,9,9,9]
print(a)
'''


'''
a=[
    [10,20],
    [40,50,60]
  ]
print(a)
a.append([6,7,8])
print(a)  
'''


'''
a=[
    [10,20],
    [40,50,60]
  ]
print(a)
a[0].remove(20)
print(a)
'''


'''
a=[
    [10,20],
    [40,50,60]
  ]
print(a)
a.pop(1)
print(a)
'''



'''
a=[
   [10,20,30],
   [40,50,60]
  ]  
print(a)
for row in a:
    print(row)
'''


'''
a=[
   [10,20,30],
   [40,50,60]
  ]  
print(a)
for row in a:
    for v in row: 
        print(v,end=" ")
    print()    
'''


'''
rows=int(input("Enter rows: "))
cols=int(input("Enter colums: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
print("Elements are: ")        
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()        
'''



'''
rows=int(input("Enter rows: "))
cols=int(input("Enter colums: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)      

sum=0
for i in matrix:
    for j in i:
        sum=sum+j
print("sum is =",sum)        


'''


rows=int(input("Enter rows: "))
cols=int(input("Enter colums: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)      
sum=0
i=0
while i<len(matrix):
    j=0
    while j<len(matrix[i]):
        sum=sum+matrix[i][j]
        j+=1
    i+=1
print("sum",sum)          



'''
a=[
    [10,20],
    [40,50,60]
  ]
sum=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    i+=1
print(sum)          
'''




