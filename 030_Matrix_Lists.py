'''
r1=int(input("Enter row of first matrix: "))
c1=int(input("Enter column of first matrix: "))
matrix1=[]
print("Enter matrix1: ")
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    matrix1.append(row)     
    
    
r2=int(input("Enter row of second matrix: "))
c2=int(input("Enter column of second matrix: "))
matrix2=[]
print("Enter matrix2: ")   
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    matrix2.append(row)     

if c1!=r2:
    print("multiplication not possible")
else:
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        result.append(row)
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]=result[i][j]+matrix1[i][k]*matrix2[k][j]
    print("\nmatrix1:") 
    for i in range(r1):
        for j in range(c1):
            print(matrix1[i][j],end=" ")
        print()    
    print("\nmatrix2:") 
    for i in range(r2):
        for j in range(c2):
            print(matrix2[i][j],end=" ")
        print()        
    print("\n result:")
    for row in result:
        print(row)
'''        




'''
a=[1,2,[3,4,[5,6]]]
print(a)
print(len(a))
print(len(a[2]))
print(len(a[2][2]))
'''



'''
A=[
[
[1,2],
[3,4]
],
[
[7,8],
[9,10]
]
]
print(A)
print(len(A))
print(len(A[0]))
'''



'''
A=[
[
[1,2],
[3,4]
],
[
[7,8],
[9,10]
]
]
print(A)
for i in range(len(A)):
    print("layer",i)
    for j in range(len(A[i])):
        for k in range(len(A[i][j])):
            print(A[i][j][k],end=" ")
        print()
    print()    
'''


'''
layer=int(input("Enter layer: ")) 
rows=int(input("Enter rows: "))   
colm=int(input("Enter column: "))
matrix=[]
for i in range(layer):
    row1=[]
    for j in range(rows):
        row2=[]     
        for k in range(colm):
            row2.append(int(input()))
        row1.append(row2)    
    matrix.append(row1)    
print("matrix: ")
for i in matrix:
    print("layer")
    for  j in i:
        for k in j:
            print(k,end=" ")
        print()    
'''


'''
layer=int(input("Enter layer: ")) 
rows=int(input("Enter rows: "))   
colm=int(input("Enter column: "))
array=[]
for i in range(layer):
    row1=[]
    for j in range(rows):
        row2=[]     
        for k in range(colm):
            row2.append(int(input()))
        row1.append(row2)    
    array.append(row1)    
print("array: ")
for i in range(len(array)):
    print("layer",i+1)
    for  j in range(len(array[i])):
        for k in range(len(array[i][j])):
            print(array[i][j][k],end=" ")
        print()            
'''



arr=[1,1,1,1]
k=2
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
            count+=1
print(count)            