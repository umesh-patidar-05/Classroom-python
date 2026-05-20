'''
s1=input("Enter first string ")
s2=input("Enter second string ")
if len(s1)!=len(s2):
    print("strings are not anagrams")
else:
    visited=[]
    flag=1
    i=0
    while i<len(s1):
        ch=s1[i]
        if ch not in visited:
            c1=0
            c2=0
            j=0
            while j<len(s1):
                if s1[j]==ch:
                    c1=c1+1
                j=j+1
            j=0
            while j<len(s2):
                if s2[j]==ch:
                    c2=c2+1
                j=j+1
            if c1!=c2:
                flag=0
                break
            visited.append(ch)    
        i=i+1
    if flag==1:
        print("string are anagrams ")
    else:
        print("strings are not anagram")
'''



'''
s=input("Enter  the string ")        
s1=""
s2=""
result=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
       s2=s2+x
for x in sorted(s1):
    result=result+x
for x in sorted(s2):
    result=result+x
print(result)    
'''



'''
s=input("Enter the string")
result=""
for x in s:
    if x.isalpha():
        result=result+x
        previous=x
    else:
        result=result+previous*(int(x)-1)
print(result)        
'''



'''
s=input("Enter the string")
result=""
for x in s:
    if x.isalpha():
        result=result+x
        previous=x
    else:
        newch=chr(ord(previous)+int(x))
        result=result+newch
print(result)    
'''


#write a program to reverse a string.


'''
s=input("Enter the string ")
rev=""
i=len(s)-1
while i>=0:
    rev=rev+s[i]
    i=i-1
print(rev)    
'''



'''
s=input("Enter the string ")
rev=s[::-1]
print(rev)
'''



'''
s=input("enter the string ")
ls=s.split()
res=""
for i in range(len(ls)-1,-1,-1):
    res=res+ ls[i] + " "
print(res)    
'''


'''
s=input("Enter the string ")
ls=s.split(" ")
print(" ".join(ls[::-1]))
'''




#write a program to reverse each word.

'''
s=input("Enter the string ")
words=s.split()
i=0
while i<len(words):
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j=j-1
    print(rev,end=" ")
    i+=1   
'''


'''
s=input("Enter the string ")
words=s.split()
for word in words:
    print(word[::-1],end=" ")
'''



s=input("Enter the string ")
rev=s[::-1]
rev2=rev.split()
print(rev)
print(rev2)
print(" ".join(rev2[::-1]))