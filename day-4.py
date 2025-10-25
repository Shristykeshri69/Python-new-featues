
# Type Hints- 
# As Python is dynamically typed  programming language, where we are not allowed to define the type. 
 
# function related Type hints / Function Annotations :-

# Static type checking can be done by using 3rd party tools.
# mypy - It is a kind of  open source tool from dropbox. 

# ex- 

def add(x:int,y:int):
    print(x+y)

add(10,20)
add('durga','tech')
add([10,20],[30,40])


# '''PS D:\python_features> mypy day-4.py                                                                                  
# day-4.py:16: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
# day-4.py:16: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
# day-4.py:17: error: Argument 1 to "add" has incompatible type "list[int]"; expected "int"  [arg-type]
# day-4.py:17: error: Argument 2 to "add" has incompatible type "list[int]"; expected "int"  [arg-type]
# Found 4 errors in 1 file (checked 1 source file)
# '''



# Complex Type hnts from typing library
from typing import List
def getnames()->List[str]:
    names:List[str]=[]

    names.append('gauri')
    names.append('kali')
    names.append('shiva')
    names.append(10)
    return names 

names=getnames()
for name in names:
    print(f'{name} contains {len(name)} Characters')


# PS D:\python_features> mypy day-4.py
# day-4.py:38: error: Argument 1 to "append" of "list" has incompatible type "int"; expected "str"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)



# PS D:\python_features> py day-4.py
# gauri contains 5 Characters
# kali contains 4 Characters
# shiva contains 5 Characters
# Traceback (most recent call last):
#   File "D:\python_features\day-4.py", line 43, in <module>
#     print(f'{name} contains {len(name)} Characters')
#                              ~~~^^^^^^
# TypeError: object of type 'int' has no len()



'''Two uses cases:
For the easyness of the programmer.
for the detection of error/ debugging 
improve code readability . '''


Advantages:-
1. It helps to catch errors related to type.
2. It helps to document our code.
3. It improves IDE Fuctionality. 


Disadvantages:-
1. It takes more developers time as we have to add type hints explicitly.
2. Readability will be reduced as the length of the code increases.
3. It will work only in newer versions. 
4. The startup  time may increases if we use typing library. 





      