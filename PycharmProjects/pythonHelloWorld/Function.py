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

#
def student_Info(*args, **kwargs):
    print(args)
    print(kwargs)




courses=['Maths', 'Art']
info={'name': 'vikash', 'age':25}


#print(student_Info('vikas', 'kumar', name='Raj', age=26))
#print(student_Info(courses, info))
print(student_Info(*courses, **info))

