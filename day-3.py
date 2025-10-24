'''
String Formatting - means inserting values and expression in string literal. 
3 types of string formatting -
 |-> % - formatting 
 |-> str.format() method 
 |-> f-strings 


Nowadays f-string is  used more. b'z 
it is more concise 
more readable
Performance wise good/ upto the mark. '''


# ex- f-string formatting


import math
half_radius=10
print(f'The area of circle with radius {2 *half_radius} is {math.pi*2*half_radius * 2*half_radius} ')
print(f' The area of circle  with radius {(r:=2*half_radius)} is {math.pi*r*r}')
print(f'The area  of circle with radius {(r:=2*half_radius)} is {math.pi*r*r : .2f}')


# OUTPUT -

# The area of circle with radius 20 is 1256.6370614359173 
#  The area of circle  with radius 20 is 1256.6370614359173
# The area  of circle with radius 20 is  1256.64



# Here timeit is module in python which  is simply used to measure the execution time of small code block. 

import  timeit
t=timeit.timeit('''
name='Sunny'
salary='1000'
gf='Monika'
s=f"Hello {name} , your salary is {salary} ,your girlfriend {gf} is waiting" ''' ,number=10000)
print('the time taken :',t)

# OUTPUT -
# the time taken : 0.010792900000524241

