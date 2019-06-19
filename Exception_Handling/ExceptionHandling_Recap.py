"""
try:
    statement(s)
except:
    statement(s)
else:
    statement(s)
finally:
    statement(s)

>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

raise ----> exception 

x = 10

if x > 5:
    #print(f"{x} Its True")
    raise Exception(f"X Should not exceed 5. The Value of X {x}")

import sys
assert ('windows' in sys.platform), "This code runs on windows Only"

try:
    statement # RUN THIS CODE
except:
    statement # EXECUTE THIS CODE WHEN THERE IS AN EXCEPTION

import sys

def platform_check():
    assert ('darwin' in sys.platform), "Function can only run on MacOS systems"
    print("Hi, Welcome to Python World")

try:
    platform_check()
except Exception as e:
    print("f{e}")

import sys

def platform_check():
    assert ('Linux' in sys.platform), "Function can only run on Linux systems"
    print("Hi, Welcome to Python World")

try:
    platform_check()
except AssertionError as error:
    print(error)
    print("f platform_check function was not executed")

try:
    # RUN THIS CODE
except:
    # EXECUTE THIS CODE WHEN THERE IS AN EXCEPTION
else:
    # NO EXCEPTIONS? RUN THIS CODE

try:
    # RUN THIS CODE
except:
    # EXECUTE THIS CODE WHEN THERE IS AN EXCEPTION
else:
    # NO EXCEPTIONS? RUN THIS CODE

    
import sys

def platform_check():
    assert ('darwin' in sys.platform), "Function can only run on Linux systems"
    print("Hi, Welcome to Python World")

try:
    platform_check()
except AssertionError as error:
    print(error)
    print("f platform_check function was not executed")
else:
    print("Executing the Code")

try:
    # RUN THIS CODE
except:
    # EXECUTE THIS CODE WHEN THERE IS AN EXCEPTION
else:
    # NO EXCEPTIONS? RUN THIS CODE
finally:
    # Always run this code
"""
import sys

def platform_check():
    assert ('linux' in sys.platform), "Function can only run on Linux systems"
    print("Hi, Welcome to Python World")

try:
    platform_check()
except AssertionError as error:
    print(error)
    print("f platform_check function was not executed")
else:
    print("Executing the Code")
finally:
    print("I am a Finally Block")

"""
raise allows you to throw an exception at any time.

assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

In the try clause, all statements are executed until an exception is encountered.

except is used to catch and handle the exception(s) that are encountered in the try clause.

else lets you code sections that should run only when no exceptions are encountered in the try clause.

finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.
"""