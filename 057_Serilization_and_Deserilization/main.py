print("03/august/2026")






'''
import pickle
student = {
    "id": 101,
    "name": "ajay",
    "course": "python"
}

file = open("student1.dat", "wb")
pickle.dump(student, file)
file.close()
print("object serialize successfully")
'''
# object serialize successfully






'''
import pickle
file = open("student1.dat", 'rb')
s1 = pickle.load(file)
file.close()
print(s1)
print(s1["name"])
print("object deserialize successfully")
'''
# {'id': 101, 'name': 'ajay', 'course': 'python'}
# ajay
# object deserialize successfully






'''
import pickle
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID is ", self.id)
        print("NAME is ", self.name)
        print("SALARY is ", self.salary)

e1 = Employee(101, "umesh", 900000)
file = open("empdata.dat", "wb")
pickle.dump(e1, file)
file.close()
print("serilization done")

file = open("empdata.dat", "rb")
newobj = pickle.load(file)
file.close()
print(newobj)
newobj.display()
print("done")
'''
# serilization done
# <__main__.Employee object at 0x00000201044DDF90>
# ID is  101
# NAME is  umesh
# SALARY is  900000
# done








import pickle
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID is ", self.id)
        print("NAME is ", self.name)
        print("SALARY is ", self.salary)

empolyees = [
    Employee(101, "umesh", 900000),
    Employee(102, "ABC", 800000),
    Employee(103, "XYZ", 700000)
]

file = open("empsdata.dat", "wb")
pickle.dump(empolyees, file)
file.close()
print("serilization done")


file = open("empsdata.dat", "rb")
emplist = pickle.load(file)
file.close()
for e in emplist:
    print(e.id, " and ", e.name)
print("done")

# serilization done
# 101  and  umesh
# 102  and  ABC
# 103  and  XYZ
# done