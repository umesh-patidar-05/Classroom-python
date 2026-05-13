'''
s1="deepika"
s2='rashmika'
print(s1)
print(s2)
'''



'''
s1="""hello guys
    how are u"""
print(s1)
'''



#s2='''areeeee
#    sun rhe ho'''
#print(s2)    



'''
s1="deepika"
print(s1[0])
print(s1[3])
print(s1[-1])
print(s1[-2] )
print(s1[-7])
'''



'''                  #IndexError: string index out of range
s1="deepika"            
print(s1[8])
'''



'''
s1="hello world"
print(s1[0:5])
'''



'''
s1="hello world"
print(s1[6:14])
print(s1[6:11])
'''



'''
s1="hello world"
print(s1[14:15])
print(s1[:5])
print(s1[6:])
print(s1[1:10:2])
'''



'''
s1="heyyy guys how are u"
print(s1[1:10:3])
print(s1[::2])
'''



'''
s1="hello world"
print(s1[-5:])
print(s1[-8:])
print(s1[:-2])
'''



'''
s1="welcome home"
print(s1[::-1])
'''



'''
s1="welcome"
r=s1[::-2]
print(r)
print(s1)
'''



'''
s1=input("enter the string")
if s1==s1[::-1]:
    print("palindrome")
else:
    print("Not")
'''



'''
s1="Welcome"
for ch in s1:   
    print(ch)
'''



'''
s1="welcome"
count=0
for x in s1:
    count=count+1
print(count)    
'''



s1=input("Enter the string ")
i=0
while i<len(s1):
    print(i," ",s1[i])
    i+=1