print("29/may/2026")


'''
a=[1,2,3]
b=[3,4,5]
merged=a+b
print(merged)
result=[]
for i in merged:
    if i not in result:
        result.append(i)
print(result)     
'''


'''
a=[1,2,3,4,5,6]
a.reverse()
print(a)
''' 


'''
a=[1,2,3,4,5,6]
b=a[::-1]
print(b)
print(a)
'''


'''
a=[1,2,3,4,5,6,]
rev=[]
for i in a: 
    rev=[i]+rev
print(rev)    
'''




'''
a=[1,0,2,0,4,0,5]
nonzero=[]
zero=[]
for i in a:
   if i==0:
        zero.append(i)
   else:
        nonzero.append(i)
result=nonzero+zero
print(result)
'''




#PEAK ELEMENT
'''
n=int(input("Enter size "))
arr=[]
print("Enter elements one by one")
for i in range(n):
    arr.append(int(input()))
print(arr)


peakindex=-1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peakindex=i
            break
            
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peakindex=i
            break
            
            
    else:
       if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
           peakindex=i
           break                
            
if peakindex!=-1:
    print("peak elment index is ",peakindex,"and value",arr[peakindex])            
else:
   print("No peak element found ")
'''






#SUM OF LEADERS
'''
n=int(input("Enter size "))
arr=[]
print("Enter elements one by one")
for i in range(n):
    arr.append(int(input()))
print(arr)

sum=0
for i in range(n):
    isleader=True
    for j in range(i+1,n):
        if arr[i]<=arr[j]:
            isleader=False
            break
    if isleader:
        sum=sum+arr[i] 
print("Aree sum of leader is ",sum)               
'''



'''
n=int(input("Enter size "))
arr=[]
print("Enter elements one by one")
for i in range(n):
    arr.append(int(input()))
print(arr)
positive=[]
negative=[]

for i in arr:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)
        
res=positive+negative        
print(res)
'''




#CYCLIC RAOATE ARRAY BY ONE
'''
n=int(input("Enter size "))
arr=[]
print("Enter elements one by one")
for i in range(n):
    arr.append(int(input()))
print(arr) 
last=arr[n-1]
i=n-1
while i>0:
    arr[i]=arr[i-1]
    i=i-1   
arr[0]=last

print(arr)    
'''
