from socket import send_fds
from typing import ClassVar


class Employee:
    raise_amount=1.04
    no_of_employees=0

    def __init__(self,first_name, last, email):
        self.first_name=first_name
        self.last=last
        self.email=email
        Employee.no_of_employees+=1

    def full_name(self):
        return self.first_name+self.last
    def increment(self):
        return self.raise_amount   #or Employee.raise_amount

    @classmethod                   #class method
    def cla_method(cls, amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,str):
        f_name, l_name, email=str.split('-')
        return cls(f_name,l_name,email)

    @staticmethod
    def is_birth_day():
        return True


class Developer(Employee):  #Inherit Employee
      raise_amount = 2.00

      def __init__(self,first_name, last, email, prog_lang):
          super().__init__(first_name,last,email)
          self.prog_lang=prog_lang




dev1=Developer.raise_amount
devlop1=Developer('vik','kr', 'aa@gmail.com', 'python')
print(dev1)
print(devlop1.prog_lang)

#print(help(Developer))           #shows inheritance tree

print(isinstance(devlop1, Employee))

print(issubclass(Developer, Employee))


e1=Employee('vik','kr','vik@gmail.com')
e2=Employee('Atul','kr','atul@gmail.com')

print(isinstance(e1, Developer))

print(Employee.full_name(e1))
print(e1.full_name())            #both same

print(e1.raise_amount)

e1.raise_amount=1.05

Employee.cla_method(1.233)

em1='vik-kr-9000'
em2='Atul-kr-90000'

ee1=Employee.from_string(em1)
ee2=Employee.from_string(em2)

print(ee1.email,ee1.first_name)
print(ee2)

print(e2.raise_amount)
print(e1.raise_amount)
print(Employee.raise_amount)
print(Employee.no_of_employees)



