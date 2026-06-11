print("11/june/2026")


'''
word=input("Enter word: ")  #ummeeesshhhh
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)  #{'u': 1, 'm': 2, 'e': 3, 's': 2, 'h': 4}
for k,v in d.items():
    print(k,"occurance", v, "times")    

'''    
'''
u occurance 1 times
m occurance 2 times
e occurance 3 times
s occurance 2 times
h occurance 4 times
'''



'''
word=input("Enter word: ")   # umeshuaaeeiioouu
d={}
vowels={"a", "e", "i", "o", "u"}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
print(d)  #{'u': 4, 'e': 3, 'a': 2, 'i': 2, 'o': 2}
for k,v in d.items():
    print(k,"occured",v,"times")
'''
'''
u occured 4 times
e occured 3 times
a occured 2 times
i occured 2 times
o occured 2 times
'''





'''
word=input("Enter word: ")   #umeshuaaeeiioouu
d={}
vowels={"a", "e", "i", "o", "u"}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
print(d)  #{'u': 4, 'e': 3, 'a': 2, 'i': 2, 'o': 2}
for k,v in sorted(d.items()):
    print(k,"occured",v,"times")
'''
'''
a occured 2 times
e occured 3 times
i occured 2 times
o occured 2 times
u occured 4 times
'''




'''
logins=["deepika", "rashmika", "deepika", "rashmika", "abc"]
c={}
for user in logins:
    c[user]=c.get(user,0)+1
print(c)    #{'deepika': 2, 'rashmika': 2, 'abc': 1}
'''




'''
words=["deepika", "rashmik", "virat", "abcde", "a", "b", "c"]
g={}
for w in words:
    l=len(w)
    if l not in g:
        g[l]=[]
    g[l].append(w)   
print(g)      #{7: ['deepika', 'rashmik'], 5: ['virat', 'abcde'], 1: ['a', 'b', 'c']}
'''




'''
d1={"goa":5, "nepal":3, "delhi":8}
d2={"goa":2, "hyd":6, "delhi":8}
merged=d1.copy()
for k,v in d2.items():
    merged[k]=merged.get(k,0)+v
print(merged)     #{'goa': 7, 'nepal': 3, 'delhi': 16, 'hyd': 6}
'''
