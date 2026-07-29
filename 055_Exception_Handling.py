print("28/july/2026")



'''
print("welcome")
a = 10
b = 0
c = a/b
print(c)
print("rest of the code")
'''
# welcome
# Traceback (most recent call last):
#   File "/home/foundation/Desktop/CLASSROOM/28_july.py", line 8, in <module>
#     c = a/b
# ZeroDivisionError: division by zero





'''
print("welcome")
try: 
    a = 10
    b = 0
    c = a/b
    print(c)

except:
    print("do not give zero")    
print("rest of the code")    
'''
# welcome
# do not give zero
# rest of the code



'''
print("welcome")
try:
    x = int("abc")
    print("inside try only")

except: 
    print("somethig went wrong")
print("rest of code")        
'''
# welcome
# somethig went wrong
# rest of code





'''
print("welcome")
try:
    x = int("10")
    print("inside try only")

except: 
    print("somethig went wrong")
print("rest of code")        
'''
# welcome
# inside try only
# rest of code





'''
print("welcome")
try:
    print("try start")
    print(10/2)
    print("Zero issue")
    x = int("xyz")
    print("try end")

except ZeroDivisionError:
    print("do not provide zero")

except ValueError:
    print("plz check integer value in string")

print("rest of code")            
'''
# welcome
# try start
# 5.0
# Zero issue
# plz check integer value in string
# rest of code





'''
print("welcome")
try:
    print("try start")
    print("hello" + 5)
    print("try end")

except TypeError:
    print("wrong operation")

except ValueError:
    print("plz check") 

print("rest of code")           
'''
# welcome
# try start
# wrong operation
# rest of code





'''
print("welcome")
try:
    print("try start")
    l = [1, 2, 3, 4]
    print(l[4])
    print("try end")

except IndexError:
    print("plz check index")
'''
# welcome
# try start
# plz check index





'''
print("welcome")
try:
    print("try start")
    d = {"a": 1}
    print(d["b"])
    print("try end")

except TypeError:
    print("wrong operation")    

except KeyError:
    print("plz check key existance")

print("rest of code")    
'''
# welcome
# try start
# plz check key existance
# rest of code






'''
print("welcome")
try:
    print("try start")
    print(y)
    print("try end")

except NameError:
    print("plz create variable")

print("rest of code")        
'''
# welcome
# try start
# plz create variable
# rest of code






'''
try:
    import xyz
except ModuleNotFoundError:
    print("module name check")

print("rest of code")        
'''
# module name check
# rest of code





'''
import math
try:
    print(math.exp(100000))

except OverflowError:
    print("use small value")

print("rest of code")        
'''
# use small value
# rest of code







'''
print("welcome")
try:
    x = int(input("enter value "))
    print(10/x)
    print("try end")

except Exception:
    print("some issue is there")

except ValueError:
    print("plz give integer value")

print("rest of code")
'''

#1        
# welcome
# enter value 2
# 5.0
# try end
# rest of code

#2
# welcome
# enter value 0
# some issue is there
# rest of code

#3
# welcome
# enter value abc
# some issue is there
# rest of code







'''
print("welcome")
try:
    x = int(input("enter value "))
    print(10/x)
    print("try end")

except ValueError:
    print("plz give integer value")

except Exception:
    print("some issue is there")

print("rest of code") 
'''

# 1
# welcome
# enter value 2
# 5.0
# try end
# rest of code

# 2
# welcome
# enter value 0
# some issue is there
# rest of code

# 3
# welcome
# enter value abc
# plz give integer value
# rest of code




'''
print("welcome")
try:
    x = int(input("enter value "))
    print(10/x)
    print("hii" + 5)
    print("try end")

except(ValueError, TypeError):
    print("some value or type error")

except Exception:
    print("some issue is there")

print("rest of code")        
'''

# 1
# welcome
# enter value 2
# 5.0
# some value or type error
# rest of code

# 2
# welcome
# enter value 0
# some issue is there
# rest of code

# 3
# welcome
# enter value abc
# some value or type error
# rest of code




'''
print("welcome")
try:
    x = int(input("Enter value "))
    print(10/x)
    print("try end")

except ValueError as v:
    print("some value or type error", v)

except Exception as e:
    print("some issue is there", e)
print("rest of code")        
'''
# 1
# welcome
# Enter value 2
# 5.0
# try end
# rest of code

# 2
# welcome
# Enter value 0
# some issue is there division by zero
# rest of code

# 3
# welcome
# Enter value abc
# some value or type error invalid literal for int() with base 10: 'abc'
# rest of code




'''
print("welcome")
try:
    x =int(input("enter value "))
    print(10/x)
    print("try end")

except ValueError as v:
    print("some value or type error", v)

except Exception as e:
    print("some issue is there ", e)

else:
    print("try block executed completely")

print("rest of code")
'''
# 1
# welcome
# enter value 2
# 5.0
# try end
# try block executed completely
# rest of code

# 2
# welcome
# enter value 0
# some issue is there  division by zero
# rest of code

# 3
# welcome
# enter value abc
# some value or type error invalid literal for int() with base 10: 'abc'
# rest of code





'''
try:
    x = int(input("enter value "))
    print(10/x)
    print("try end")

except ValueError as v:
    print("some value or type error", v)   

except Exception as e:
    print("some issue is there ", e)

else:
    print("try block executed completely")

finally:
    print("always execute")    

print("rest of code")
'''
# 1
# enter value 2
# 5.0
# try end
# try block executed completely
# always execute
# rest of code

# 2
# enter value 0
# some issue is there  division by zero
# always execute
# rest of code

# 3
# enter value abc
# some value or type error invalid literal for int() with base 10: 'abc'
# always execute
# rest of code






'''
print("welcome")
try:
    print("try")

finally:
    print("always executes")

print("rest of code")        
'''
# welcome
# try
# always executes
# rest of code




'''
print("welcome")
try:
    print("try")
print("rest of code")    
'''
#   File "c:\Users\HP\Desktop\PYTHON\ClassRoom\055_Exception_Handling.py", line 491
#     print("rest of code")    
#     ^^^^^
# SyntaxError: expected 'except' or 'finally' block




'''
def test():
    try:
        return "from try"

    finally:
        print("finally executed")

print(test())     
'''
# finally executed
# from try




'''
def test():
    try:
        return "from try"
    finally:
        return "from finally"
print(test())
'''
# from finally



'''
def test():
    try:
        return 10/0
    
    except ZeroDivisionError:
        return "error handled"

    finally:
        print("from finally")
    print("end of function")
print(test())        
'''
# from finally
# error handled





'''
import os
try:
    print("try block")
    os._exit(0)

finally:
    print("finally block")    
'''
# try block




'''
class AgeError(Exception):
    pass

age = int(input("Enter the age "))

if age<18:
    raise AgeError("you are not eligible")

print("eligible")
'''
# 1
# Enter the age 15
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PYTHON\ClassRoom\055_Exception_Handling.py", line 571, in <module>
#     raise AgeError("you are not eligible")
# AgeError: you are not eligible

# 2
# Enter the age 20
# eligible



'''
def Withdraw(amount):
    balance = 5000
    if amount > balance:
        raise Exception("insufficient balance")
    return balance - amount

try:
    print(Withdraw(6000))

except Exception as e:
    print("Error", e)

print("rest of code")        
'''
# Error insufficient balance
# rest of code





'''
def Withdraw(amount):
    balance = 5000
    if amount > balance:
        raise Exception("insufficient balance")
    return balance - amount

try:
    print(Withdraw(3000))

except Exception as e:
    print("Error", e)

print("rest of code")        
'''
# 2000
# rest of code






'''
class DotException(Exception):
    pass

class AtTheRateException(Exception):
    pass

def validate(email):
    if email.count("@") != 1:
        raise AtTheRateException("invalid @ usage")

    if "." not in email or email.endswith("."):
        raise DotException("invalid dot usage")

email = input("enter email ")

try:
    validate(email)
    print("valid email")

except AtTheRateException as e:
    print("AtTheRateException", e)
    print("invalid e mail address")

except DotException as e:
    print("DotException", e)
    print("invalid e mail address")
'''
# 1
# enter email umesh@gmail.com
# valid email

# 2
# enter email umesh@gmailcom
# DotException invalid dot usage
# invalid e mail address

# 3
# enter email umeshgmail.com 
# AtTheRateException invalid @ usage
# invalid e mail address

# 4
# enter email umesh@gmailcom.
# DotException invalid dot usage
# invalid e mail address






class InsufficientBalanceException(Exception):
    pass

class NegativeDepositException(Exception):
    pass

class BankAcount:
    def __init__(self, actnumber, acholder, balance):
        self.actnumber = actnumber
        self.acholder = acholder
        self.balance = balance

    def deposit(self, amount):
        if amount<0:
            raise NegativeDepositException("deposit amount can not be negative")
        self.balance = self.balance + amount
        print("deposite successful") 
        print("current balance", self.balance) 

    def withdraw(self, amount):
        if amount>self.balance:
            raise InsufficientBalanceException("insufficient balance")
        self.balance = self.balance - amount
        print("withdraw successful")
        print("current balance", self.balance) 

actnumber = int(input("Enter account number "))
actholder = input("Enter account holder name ") 
balance = float(input("Enter balance "))

acc = BankAcount(actnumber, actholder, balance)

try:
    amount = float(input("Enter deposit amount "))
    acc.deposit(amount)

except NegativeDepositException as e:
    print("negative", e)

try:
    amount = float(input("Enter withdraw amount "))
    acc.withdraw(amount)

except InsufficientBalanceException as e:
    print("insufficient", e)

# 1
# Enter account number 101
# Enter account holder name umesh
# Enter balance 1000
# Enter deposit amount 200
# deposite successful
# current balance 1200.0
# Enter withdraw amount 500
# withdraw successful
# current balance 700.0
    
# 2
# Enter account number 101
# Enter account holder name umesh
# Enter balance 1000
# Enter deposit amount -500
# negative deposit amount can not be negative
# Enter withdraw amount 200
# withdraw successful
# current balance 800.0

# 3
# Enter account number 101
# Enter account holder name umesh
# Enter balance 1000
# Enter deposit amount 300
# deposite successful
# current balance 1300.0
# Enter withdraw amount 1500
# insufficient insufficient balance

# 4
# Enter account number 101
# Enter account holder name umesh
# Enter balance 1000
# Enter deposit amount -500
# negative deposit amount can not be negative
# Enter withdraw amount 1500
# insufficient insufficient balance