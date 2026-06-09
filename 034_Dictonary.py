print("09/june/2026")


'''
d={1:"deepika",2:"rashmika",3:"virat"}
print(d) #{1: 'deepika', 2: 'rashmika', 3: 'virat'}
'''


'''
d={1:"deepika",2:"rashmika",3:"virat"}
print(d) #{1: 'deepika', 2: 'rashmika', 3: 'virat'}
d1=dict(a="abc",b="hjdg", c="www")
print(d1)    #{'a': 'abc', 'b': 'hjdg', 'c': 'www'}
'''



'''
student={
"name":"mahesh",
"age":33,
"city":"hyderabad"
}
print(student)   #{'name': 'mahesh', 'age': 33, 'city': 'hyderabad'}
'''



'''
student={ 
"name":"mahesh",
"age":33,
"city":"hyderabad"
}
print(student)
print(student["name"])
print(student.get("name"))
print(student["city"])
print(student.get("age"))
'''


'''
student={ 
"name":"mahesh",
"age":33,
"city":"hyderabad"
}
print(student["salary"])   #KeyError: 'salary'
'''


'''
student={ 
"name":"mahesh",
"age":33,
"city":"hyderabad"
}
print(student.get("salary"))   #None
'''


'''
student={ 
"name":"mahesh",
"age":33,
"city":"hyderabad"
}
print(student.get("address","not found"))  #not found
'''




'''
d={}
n=int(input("Enter numbear of students "))
i=1
while i<=n:
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    d[name]=marks
    i+=1
print("name of student","\t"," % of marks")
for x in d:
   print(x,"\t\t",d[x])
'''




'''
d={1:"dipu", 2:"rashmika"}
print(d) #{1: 'dipu', 2: 'rashmika'}
d[3]="virat"
print(d)    #{1: 'dipu', 2: 'rashmika', 3: 'virat'}
'''



'''
d={1:"dipu", 2:"rashmika"}
d[1]="vaibhav"
print(d)  #{1: 'vaibhav', 2: 'rashmika'}
'''


'''
d={1:"dipu", 2:"rashmika", 1:"vaibhav"}
print(d)
'''



'''
d={1:"dipu", 2:"rashmika", 3:"dipu"}
print(d)  #{1: 'dipu', 2: 'rashmika', 3: 'dipu'}
'''


'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student) #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
print(student.pop("city"))  #chennai
print(student)   #{'name': 'dipu', 'age': 30}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
print(student.pop("address"))
print(student)  #KeyError: 'address'
'''



'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
print(student.popitem())  #('city', 'chennai')
print(student)  #{'name': 'dipu', 'age': 30}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai", 30:"areeee"}
print(student)   #{'name': 'dipu', 'age': 30, 'city': 'chennai', 30: 'areeee'}
while student:
    print(student.popitem())   
#     (30, 'areeee')
#     ('city', 'chennai')
#    ('age', 30)
#    ('name', 'dipu')
'''



'''
student={"name":"dipu", "age":30, "city":"chennai", 30:"areeee"}
print(student)    #{'name': 'dipu', 'age': 30, 'city': 'chennai', 30: 'areeee'}
del student["age"]
print(student)   #{'name': 'dipu', 'city': 'chennai', 30: 'areeee'}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai", 30:"areeee"}
del student["address"]
print(student)  #KeyError: 'address'
'''


'''
student={"name":"dipu", "age":30, "city":"chennai", 30:"areeee"}
del student
print(student)  #NameError: name 'student' is not defined
'''



'''
student={"name":"dipu", "age":30, "city":"chennai", 30:"areeee"}
print(student)    #{'name': 'dipu', 'age': 30, 'city': 'chennai', 30: 'areeee'}
student.clear()
print(student)    #{}
'''




'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
print(student.keys())  #dict_keys(['name', 'age', 'city'])
print(list(student.keys()))  #['name', 'age', 'city']
print(set(student.keys()))   #{'age', 'name', 'city'}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
print(student.values())  #dict_values(['dipu', 30, 'chennai'])
print(list(student.values()))   #['dipu', 30, 'chennai']
'''




'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student.items())  #dict_items([('name', 'dipu'), ('age', 30), ('city', 'chennai')])
print(list(student.items())) #[('name', 'dipu'), ('age', 30), ('city', 'chennai')]
'''



'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
student.update({"salary": 90000})
student.update({"city":"indore"})
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'indore', 'salary': 90000}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)   #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
s1=student.copy()
print(s1)   #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
s1.update({"salary":90000})
print(student)   #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
print(s1)    #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'salary': 90000}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai"}
print(student)    # {'name': 'dipu', 'age': 30, 'city': 'chennai'}
s1=student
print(s1)    #{'name': 'dipu', 'age': 30, 'city': 'chennai'}
s1.update({"salary":90000})
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'salary': 90000}
print(s1)       #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'salary': 90000}
'''




'''
student={"name":"dipu", "age":30, "city":"chennai", "marks":[87,66]}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1=student
print(s1)   #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1["marks"][0]=77
print(student)   #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66]}
print(s1)    #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66]}
'''


'''
import copy
student={"name":"dipu", "age":30, "city":"chennai", "marks":[87,66]}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1=copy.deepcopy(student)
print(s1)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1.update({"new":"areeee"})
s1["marks"][0]=77
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
print(s1)   #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66], 'new': 'areeee'}
'''




'''
student={"name":"dipu", "age":30, "city":"chennai", "marks":[87,66]}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1=student
print(s1)    #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1.update({"new":"areeee"})
s1["marks"][0]=77
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66], 'new': 'areeee'}
print(s1)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66], 'new': 'areeee'}
'''



'''
student={"name":"dipu", "age":30, "city":"chennai", "marks":[87,66]}
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1=student.copy()
print(s1)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [87, 66]}
s1.update({"new":"areeee"})
s1["marks"][0]=77
print(student)  #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66]}
print(s1)   #{'name': 'dipu', 'age': 30, 'city': 'chennai', 'marks': [77, 66], 'new': 'areeee'}
'''


'''
sq={}
for i in range(1,6):
    sq[i]=i*i
print(sq)    #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''


sq={i:i*i for i in range(1,6)}
print(sq)   #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

