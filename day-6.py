
# Aliasing - Process of creating duplicate refernce variable. 

# ex- 
l1=[10,20,30,40]
l2=l1
l2[3]=100
print(f'l1:{l1}')       # l1:[10, 20, 30, 100]
print(f'l2:{l2}')       # l2:[10, 20, 30, 100]

'''The problem with aliasing is by using one Reference if we perform any change,automatically those changes will be reflected for the remaining references also. 

If we want duplicate object instead of duplicate reference variable then we should go for cloning . '''


# cloning - process of creating duplicate object but with having different addresses.
#comment added
l1=[10,20,30,40]
l2=l1.copy()
print(id(l1))    #  3019624760512
print(id(l2))    #  3019624527424


# ex - shallow cloning

import copy 
l1=[10,20,[30,40],50]
l2=copy.copy(l1)
l1[2][0]=777
print(f'l1:{l1}')      #   l1:[10, 20, [777, 40], 50]
print(f'l2:{l2}')      #   l2:[10, 20, [777, 40], 50]



# ex - deeep cloning

import copy 
l1=[10,20,[30,40],50]
l2=copy.deepcopy(l1)
l1[2][0]=777
print(f'l1:{l1}')    # l1:[10, 20, [777, 40], 50]
print(f'l2:{l2}')    # l2:[10, 20, [30, 40], 50]


'''NOTE:-
If original object does not contain any nested object then it is highly recommended to go for - shallow cloning. 
If original object  contains any nested object then it is highly recommended to go for - deep cloning. '''





