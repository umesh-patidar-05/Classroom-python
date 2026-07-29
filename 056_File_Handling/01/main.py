print("29/july/2026")




'''
f = open("introduction.txt")
print(f)
'''
# <_io.TextIOWrapper name='introduction.txt' mode='r' encoding='cp1252'>




'''
f = open("C:/Users/HP/Desktop/PYTHON/ClassRoom/056_File_Handling/introduction.txt")
print(f)
'''
# <_io.TextIOWrapper name='C:/Users/HP/Desktop/PYTHON/ClassRoom/056_File_Handling/introduction.txt' mode='r' encoding='cp1252'>





'''
f = open("introductionnotcreate.txt")
print(f)
'''
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PYTHON\ClassRoom\056_File_Handling\01\main.py", line 24, in <module>
#     f = open("introductionnotcreate.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'introductionnotcreate.txt'




'''
f = open("introduction.txt")
print(f)
f.close()
'''
# <_io.TextIOWrapper name='introduction.txt' mode='r' encoding='cp1252'>




'''
f = open("introduction.txt")
print(f)
print("File name: ", f.name)
print("mode is: ", f.mode)
print("is closed?: ", f.closed)
f.close()
print("is closed?: ", f.closed)
'''
# File name:  introduction.txt
# mode is:  r
# is closed?:  False
# is closed?:  True





'''
f = open("introduction.txt", "r")
data = f.read()
print(data)
f.close()
'''
# hii 
# my name is umesh patidar




# dream.txt me content pehle = full satck web developer with AI ML
'''
f = open("dream.txt", "w")
f.write("web developer umesh")
print("plz open and check file")
f.close()
'''
# plz open and check file

# ab file content = web developer umesh





'''
f = open("xyyz.txt", "w") #ye file exists nhi hai
f.write("heyyy guysss")
print("plz open and check file")
f.close()
'''
# plz open and check file

# xyyz.txt name se file create hogi or content = heyyy guysss





'''
with open("xyyz.txt", "r") as f:
    data = f.read()
    print(data)
    print(f.closed)
print(f.closed)    
'''
# heyyy guysss
# False
# True




'''
try:
    with open("xyyz.txt", "r") as f:
        data = f.read()
        print(data)
        print(f.closed)
except FileNotFoundError as e:
    print(e)
print("rest of code")  
print(f.closed)
'''
# heyyy guysss
# False
# rest of code
# True





'''
try:
    with open("abbc.txt", "w") as f:
        f.write("areeeeeeeee")
        print(f.closed)
except FileNotFoundError as e:
    print(e)
print("rest of code")  
print(f.closed)
'''
# False
# rest of code
# True




'''
try:
    with open("abbc.txt", "a") as f:
        f.write(" umesh patidar")
        print(f.closed)

except FileNotFoundError as e:
    print(e)

print("rest of code")        
'''
# False
# rest of code





'''
try:
    with open("magic.txt", "x") as f:
        f.write("sun rahe hooo")
        print(f.closed)
except FileNotFoundError as e:
    print(e)
print("rest of code")  
print(f.closed)
'''
# False
# rest of code
# True




try:
    with open("magic.txt", "r+") as f:
        data = f.read()
        print(data)
        f.write("python is going")
        print(f.closed)
except FileNotFoundError as e:
    print(e)
print("rest of code")  
print(f.closed)

# sun rahe hooo
# False
# rest of code
# True