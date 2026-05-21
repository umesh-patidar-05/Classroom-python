'''
s=input("Enter the string ")
word=""
i=0
while i<len(s):
    if s[i]!=" ":
        word=s[i]+word
    else:
        print(word,end=" ")
        word=""
    i+=1
print(word,end=" ")    
'''




'''
s=input("Enter the string ")
words=s.split()
i=len(words)-1
while i>=0:
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j=j-1
    print(rev,end=" ")
    i=i-1
'''




'''
s=input("Enter the string ")
words=s.split()
i=len(words)-1
r=""
while i>=0:
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j=j-1
    rev=rev+" "    
    r=r+rev + " "
    i=i-1
del(s)
s=r
print(s)    
'''




'''
s=input("Enter the string ")
i=0
f=0
while i<len(s):
    count=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            count=count+1
        j=j+1
    if count==1:
        print("First non repeat",s[i])
        f=1
        break
    i+=1
if f==0:
    print("No rep found")
'''



'''
s=input("Enter the string ")
words=s.split()
short=words[0]
i=1
while i<len(words):
    if len(words[i])<len(short):
        short=words[i]
    i+=1
print("shortest word is ",short)    
'''




'''
s=input("Enter string ")
c1=0
for ch1 in s:
    count=0
    for ch2 in s:
        if ch1==ch2:
            count+=1
    if count==1:
        c1+=1
print("unique characters in string =",c1)
'''




'''
s=input("Enter a string: ")
word=input("Enter the word: ")
count=0
i=0
while i<=len(s)-len(word):
    j=0
    match=1
    while j<len(word):
        if s[i+j]!=word[j]:
            match=0
            break
        j=j+1
    if match==1:
        count=count+1
    i=i+1
print("Number of occurences:",count)    
'''


