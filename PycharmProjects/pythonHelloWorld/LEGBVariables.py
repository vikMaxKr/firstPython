import builtins
from tkinter.font import names


#LEGB
#L-Local
#E- enclosing
#G- global
#B- Built-in

#x='global x'

def fun(z):
    y='local y'
    global x
    x=y
    print(y)
    print(z)

fun('local z')
#print(x)

#####  Built-in

m=min([1,2,3,4])
print(m)

#print(dir(builtins))

#Note if any method defined here(global method) in class is similar to built-in methods python going to execute
#first global method then built-in

###     Enclosing scope for nested functions


def outer():
    x='outer x'
    print(x)
    def inner():
        x='inner x'
        print(x)
    inner()
    print(x)

outer()

class Employee():

    def __init__(self,name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return '{},{},${}'.format(self.name,self.age,self.salary)

e1=Employee('vikash', 28, 30000)
e2=Employee('Atul',23, 4000)
e3=Employee('Raj', 45, 344556)

employees=[e1,e2,e3]

def fun(emp):
    return emp.name

sortd_emp=sorted(employees,key=fun,reverse=True)
print(sortd_emp)

