

# Exception handling is always associated with runtime errors.
# The main purpose of assertions is for debugging purposes.
# Debugging - process of identifying & fixing the bug.

# Augmented version - we can augmented extra information with assertions error.
# syntax - assert conditional_expression , message 

# ex


def squareit(x):
    return x**x 

assert squareit(2)==4
assert squareit(3)==27
assert squareit(4)==16

print(squareit(2))
print(squareit(3))
print(squareit(4))

# RESULT :

'''Traceback (most recent call last):
  File "D:\python_features\day-7.py", line 17, in <module>
    assert squareit(4)==16
           ^^^^^^^^^^^^^^^
AssertionError'''


when to use assert ?

debugging and catching logical errors during development.
ensuring function inputs meet expected conditions.
validating intermediate states in complex calculations.
used in test cases for quick sanity checks.



NOTE :-
1. The most way of debugging is to use print statement.But the problem with print statement is after fixing the bug compulsory we have to delete extra added print statements which creates performance problem & logs will be distributed . 

2. Assert concept can be used to alert programmer to resolve development time errors.
3. Exception handling can be used to handle RuntimeErrors. 



  

