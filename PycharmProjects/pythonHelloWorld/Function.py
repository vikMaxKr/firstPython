import Numeric as nnn

nn=nnn.num
print(nn)

def hello_fun():
    print('inside function')

def hellow_fun1():
    return 'Inside function'

def hellow_argument(argument):
    return argument+' received'

print(hello_fun())
print(hello_fun)   #Memory address

for i in range(1,5):
    hello_fun()

print(len(hellow_fun1())) #Return length

print(hellow_argument('vikash'))

#*args allows a function to accept any number of positional arguments as a tuple.
#**kwargs allows a function to accept any number of keyword arguments as a dictionary.
def student_info(*args, **kwargs):    # *args and **kwargs are used to handle a variable number of arguments in a function.
    print(args)
    print(kwargs)




courses=['Maths', 'Art']
info={'name': 'vikash', 'age':25}


#print(student_info('vikas', 'kumar', name='Raj', age=26))
#print(student_info(courses, info))
print(student_info(*courses, **info))

