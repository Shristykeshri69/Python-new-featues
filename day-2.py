# Keyword only Argument - After * , all parameters will become keyword only parameters.At the time of calling we should pass values by keyword only. 

# Positional only argument - we should pass values by positional only arguments.All parameter before / , will become positional only argument. 
# 

'''
def f1(*,a,b):             # example of Keyword only Argument
    print(a,b)
f1(a=10,b=20)    # 10 20
f1(10,20)        # TypeError: f1() takes 0 positional arguments but 2 were given
f1(10,b=20)     # TypeError: f1() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given
'''

'''
def f2(c,d,/):    # example of Positional only argument
    print(c,d)
f2(30,40)        # 30 40
'''


'''
Summary - 
1. Without effecting callers, we can change function parameter names.
2. we are not required to expose our internal parameter names to the outside world . Hence we will get security. 
3. while overriding parent class method in child class, we are not required to use same parameter names. 
4. Performance will be improved. 
5. more compatibilty between python function calls and internal C language calls. 
'''

'''Positional only  vs Keyword only :-
1. If the parameter names are not important & not having any meaning & there are only few arguments - Go with Positional only argument . 
2. If paramter names having meaning & function implementation is more understandable with these names. - Go with Keyword only argument. '''




 
