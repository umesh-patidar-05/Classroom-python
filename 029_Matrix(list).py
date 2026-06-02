print("02/june/2026")




'''
rows=int(input("Enter rows: "))
cols=int(input("Enter colums: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)     
print("\nMATRIX: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")    
    print()
#print(len(matrix))
sum=0
for i in range(len(matrix)):
    sum=sum+matrix[i][i]
print("sum of diagonal element is ",sum)            
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
print("\nMATRIX: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")    
    print()
sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]%2!=0:
            sum=sum+matrix[i][j] 
print("sum of odd element is",sum)               
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
print("\nMATRIX: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")    
    print()
sum=0
for i in matrix:
    for j in i:
        if j%2!=0:
            sum=sum+j
print("sum of odd elements is",sum)
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
print("\nMATRIX: ")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")    
    print()
search=int(input("Enter element to search "))
x=0
for i in matrix:
    for j in i:
        if j==search:
            print("banda found")
            x=1
            break
if x==0:
    print("Not found")                
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
print("\nMATRIX: ")
for i in matrix:
    for j in i:
        print(j,end=" ")    
    print()
for dipu in matrix:
    dipu.reverse()
print("\nmatrix aftert reverse: ") 
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
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
print("\nMATRIX: ")
for i in matrix:
    for j in i:
        print(j,end=" ")    
    print()
for dipu in matrix:
    print(dipu[::-1])
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
print("\nMATRIX: ")
for i in matrix:
    for j in i:
        print(j,end=" ")    
    print()
for row in matrix:
    i=0
    j=len(row)-1
    while i<j:
        t=row[i]
        row[i]=row[j]
        row[j]=t
        i+=1
        j-=1
print("\nmatrix after reverse: ")
for i in matrix:
    for j in i:
        print(j,end=" ")

    print()    
'''    
    
    
    
    
    
'''    
rows=int(input("Enter rows: "))
cols=int(input("Enter colums: "))

matrix1=[]
print("Enter matrix1")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row)     

matrix2=[]
print("Enter matrix2")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row)     

print("\nMATRIX1: ")
for i in matrix1:
    for j in i:
        print(j,end=" ")    
    print()

print("\nMATRIX2: ")
for i in matrix2:
    for j in i:
        print(j,end=" ")    
    print()    
    
    
matrix3=[]
print("\nEnter matrix3")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(0)
    matrix3.append(row)     
    

print("\nMATRIX3: ")
for i in matrix3:
    for j in i:
        print(j,end=" ")    
    print()     
    
for i in range(rows):
    for j in range(cols):    
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
        
print("\nAreeee matrix3 idhar haiiiiiiii......")        
for i in matrix3:
    for j in i:
        print(j,end=" ")
    print()  
'''






 
    
rows=int(input("Enter rows: "))
cols=int(input("Enter colums: "))

matrix1=[]
print("Enter matrix1")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row)     

matrix2=[]
print("Enter matrix2")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row)     

print("\nMATRIX1: ")
for i in matrix1:
    for j in i:
        print(j,end=" ")    
    print()

print("\nMATRIX2: ")
for i in matrix2:
    for j in i:
        print(j,end=" ")    
    print()    
    
    
matrix3=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(row)     
        
print("\nAreeee sum idhar haiiiiiiii......")        
for i in matrix3:
    for j in i:
        print(j,end=" ")
    print()        