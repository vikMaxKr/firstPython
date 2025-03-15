class Employee:

    def __init__(self,name,address,pay):
        self.name=name
        self.address=address
        self.pay=pay

    def __str__(self):
        return 'Employee( {},{}, {})'.format(self.name,self.address, self.pay)

    def __repr__(self):
        return [self.name,self.address]

    def __add__(self, other):
        return self.pay + other.pay


emp1=Employee('vikash', '123 Dawning Street',3000)
emp2=Employee('vik', '12344 Dawning Street',6000)

print(emp2+emp1)

print('test'.__len__())

print(emp1)