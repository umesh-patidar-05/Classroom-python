 #print("22/may/2026")



#CREATING LIST
'''
l=[10,"deepika",12.5]
l2=[10,20,30]
print(l)                 #[10, 'deepika', 12.5]
print(l2)                #[10, 20, 30]


'''



'''
l=list("Welcome")
print(l)              #['W', 'e', 'l', 'c', 'o', 'm', 'e']
'''


'''
l2=list((12,14,"deepika"))
print(l2)                    #[12, 14, 'deepika']
'''



'''
l=[2]*5
print(l)       #[2, 2, 2, 2, 2]
'''



'''
l=["deepika",4]*5
print(l)          #['deepika', 4, 'deepika', 4, 'deepika', 4, 'deepika', 4, 'deepika', 4]
'''



'''
l=list(range(1,6)) 
print(l)                 #[1, 2, 3, 4, 5]
'''



#ACCESSING LIST ELEMENTS

'''
l=[10,20,30,40,50]
print(l[0])         #10  
print(l[-1])        #50
print(l[1:4])       #[20, 30, 40]
'''



'''
l=[10,20,30,40,50]
for i in l:
    print(i,end=" ")    #10 20 30 40 50
'''



'''
l=[10,20,30,40,50]
print(len(l))
for i in range(len(l)):
    print("index is ",i,"and value is ",l[i])         #index is  0 and value is  10
                                                      #index is  1 and value is  20     
                                                      #index is  2 and value is  30
                                                      #index is  3 and value is  40
                                                      #index is  4 and value is  50
'''




'''
l=[10,20,30,40,50]
print(l[:3])        #[10, 20, 30]
print(l[2:])        #[30, 40, 50]
print(l[::2])       #[10, 30, 50]
'''







#ADDING ELEMENTS INTO THE LIST


'''
l=[10,20,30,40,50]
l.append(60)
print(l)            #[10, 20, 30, 40, 50, 60]
'''


'''
l=[]
for i in range(1,101):
    if i%2==0:
        l.append(i)
print(l)     
'''


'''
output 
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
'''






'''
l=[10,20,30]
l.insert(1,99)
print(l)               #[10, 99, 20, 30]
'''




l=[10,20,30]
l.insert(len(l),99)
print(l)              #[10, 20, 30, 99]
	
