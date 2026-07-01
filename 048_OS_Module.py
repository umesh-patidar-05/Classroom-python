'''
import os
print(os.getcwd())   #C:\\Users\\HP\\Desktop\\PYTHON\\ClassRoom
'''


'''
import os
os.chdir(r"C:\\Users\\HP\\Desktop\\PYTHON\\Assignment")
print(os.getcwd())     #C:\\Users\\HP\\Desktop\\PYTHON\\Assignment
'''


'''
import os
print(os.listdir())
'''
# ['.git', '.mypy_cache', '001.py', '002.py', '003.py', '004.py', '005.py', '006.py', '007.py', '008.py', '009.py', '010.py', '011.py', '012.py', '013.py', '014.py', '015.py', '016.py', '017.py', '018.py', '019.py', '020.py', '021.py', '022.py', '023.py', '024.py', '025_Lists.py', '026_Lists.py', '027_Lists.py', '028_List.py', '029_Matrix(list).py', '030_Matrix_Lists.py', '031_Tuple.py', '032_named_Tuple.py', '033_Set_and_frozenset.py', '034_Dictonary.py', '035_Dictonary.py', '036_Dictonary.py', '037_Functions.py', '038_arguments_or_parameters.py', '039_arguments.py', '040_Lambda_and_Map_and_Filter.py', '041_Reduce_LambdaSorting_Recursion.py', '042_NestedFunctions_LEGB_HigherOrderFunctions.py', '043_Closures_Decorators_TypeHints_DocString.py', '044_Built_In_Module.py', '045_User_defined_Modules', '046_Package', '047_Class_Object.py', '048_OS_Module']



'''
import os
os.mkdir("PythonNotes")
'''
# Creates a new directory.


'''
import os
os.makedirs("Folder1/Folder2/Folder3")
'''


'''
import os
os.rmdir("PythonNotes")
'''


'''
import os
os.remove("test.txt")
'''


'''
import os
os.rename("old.txt", "new.txt")
'''



# Checks whether a file or directory exists
'''
import os
print(os.path.exists("test.txt"))  #False
'''



# Checks whether the given path is a file.
'''
import os
print(os.path.isfile("test.txt")) #False
'''


'''
import os
print(os.path.isdir("PythonNotes"))   #False
'''


'''
import os
print(os.getpid())   #13300
'''


'''
import os
print(os.getlogin())
'''


'''
import os
print(os.environ)
'''

'''
import os
os.system("dir")    
'''



import os
os.system("cls")      # Clear screen (Windows)