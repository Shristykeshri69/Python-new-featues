# walrus operator (:=) - This operator released as a part of PEP 572. To assign values to the variable as a part of expression itself. 

# Problem Statement - without use of this opertor length of code more .

# Solution - this allows us to manage  both assign and evaluate a variable in the same expression. and  simplicify complex expression as well as avoid repeated computations. 

 
#  The main advantage :- 
#  Actually It won't do any new thing. It just reduces length of code and readability will be improved. and it would have allowed a modest but clear improvement in quite a few bits of code. 




'''l=[10,20,30,40,50]             # without using walrus 
n=len(l)
if n>3:
    print('List contains more  than 3 element')
    print('The length of the list is ',n)
print(n)'''


'''l=[10,20,30,40,50]             #  using wlarus 
if (n:=len(l)) >3 :
    print('List contains more  than 3 element')
    print('The length of the list is ',n)
print(n)'''






