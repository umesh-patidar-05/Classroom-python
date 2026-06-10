print("10/june/2026")

'''
se={i:i*i for i in range(1,11)  if  i%2==0}
print(se)  #{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
'''



'''
words={"deepika", "thapaji", "krishna"}
print(type(words))  #<class 'set'>
d={word:len(word) for word in words}
print(d) #{'deepika': 7, 'krishna': 7, 'thapaji': 7}
print(type(d))  #<class 'dict'>
'''


'''
numbers=[1,2,3,4,5]
r={x:"Even" if x%2==0 else "odd" for x in numbers}
print(r)   #{1: 'odd', 2: 'Even', 3: 'odd', 4: 'Even', 5: 'odd'}
'''


'''
keys=["name", "age", "city"]
values=["deepika", 30 , "chennai"]
d={keys[i]:values[i] for i in range(len(keys))}
print(d)   #{'name': 'deepika', 'age': 30, 'city': 'chennai'}
'''


'''
{
key1:{inner key1:value1, innerkry2:value2},
key2:{inner key1:value1, innerkry2:value2}

'''


'''
students={
101:{"name":"dipu", "age":30},
102:{"name":"virat", "age":35}
}
print(students)  #{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 35}}
print(students[101])   #{'name': 'dipu', 'age': 30}
print(students[101]["name"])   #dipu
'''


'''
students={
101:{"name":"dipu", "age":30},
102:{"name":"virat", "age":35}
}
print(students)   #{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 35}}
students[102]["age"]=25
print(students)  #{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 25}}
'''


'''
students={
101:{"name":"dipu", "age":30},
102:{"name":"virat", "age":35}
}
students[103]={"name":"rashmika", "age":30}
print(students)
'''



'''
students={
101:{"name":"dipu", "age":30},
102:{"name":"virat", "age":35}
}
students[103]={"name":"rashmika", "age":30}
print(students)  #{101: {'name': 'dipu', 'age': 30}, 102: {'name': 'virat', 'age': 35}, 103: {'name': 'rashmika', 'age': 30}}
for k,v in students.items():
    print("Id",k)
    for k1,v1 in v.items():
        print(k1 ,"=",v1)
        
 
output: 
  Id 101
  name = dipu
  age = 30
  Id 102
  name = virat
  age = 35
  Id 103
  name = rashmika
  age = 30        
'''


'''
company={
"emp1":{"name": "deepika", "skills":["python", "java", "react"]},
"emp2":{"name": "virat", "skills":["python", "java", "react"]},
}

print(company)  #{'emp1': {'name': 'deepika', 'skills': ['python', 'java', 'react']}, 'emp2': {'name': 'virat', 'skills': ['python', 'java', 'react']}}
'''


'''
student = {
    "name": "Umesh",
    "address": {
        "city": "Bhopal",
        "state": "MP"
    }
}

print(student)  #{'name': 'Umesh', 'address': {'city': 'Bhopal', 'state': 'MP'}}
del student["address"]["city"]

print(student)  #{'name': 'Umesh', 'address': {'state': 'MP'}}
'''


'''
company={
"emp1":{"name": "deepika", "skills":["python", "java", "react"]},
"emp2":{"name": "virat", "skills":["python", "java", "react"]},
}

print(company)  #{'emp1': {'name': 'deepika', 'skills': ['python', 'java', 'react']}, 'emp2': {'name': 'virat', 'skills': ['python', 'java', 'react']}}
del company["emp1"]["skills"][0]
print(company)  #{'emp1': {'name': 'deepika', 'skills': ['java', 'react']}, 'emp2': {'name': 'virat', 'skills': ['python', 'java', 'react']}}
'''



'''
response={
"user":{
"id":101,
"profile":{"name":"dipu", "email":"d@gmail.com"}

}
}

print(response["user"]["profile"]["email"])  #d@gmail.com
'''




'''
d=eval(input("enter dictionary"))  #{"name":"umesh", "age":21}
print(type(d))  #<class 'dict'>
print(d)  #{'name': 'umesh', 'age': 21}

a=eval(input("Enter number "))  #12.8
print(type(a))  #<class 'float'>
print(a)   #12.8

l1=eval(input("Enter list "))  #[1,2,3,4,65]
print(type(l1))  #<class 'list'>
print(l1)  #[1, 2, 3, 4, 65]
'''



'''
d=eval(input("Enter dictonary: "))  #{"a":10, "b": 20, "c":30, "d":40}
print(type(d))  #<class 'dict'>
print(d)  #{'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(d.values())  #dict_values([10, 20, 30, 40])
s=sum(d.values())
print(s)  #100
'''




n=int(input("Enter number of items: "))
d={}
for i in range(n):
    key=input("Enter key ")
    value=int(input("Enter value "))
    d[key]=value
print(type(d)) 
print(d)
s=sum(d.values())
print(s)


'''
INPUT:
Enter number of items: 4
Enter key a
Enter value 1
Enter key b
Enter value 2
Enter key c
Enter value 3
Enter key d
Enter value 4

OUTPUT:
<class 'dict'>
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
10
'''