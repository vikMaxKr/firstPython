#IF

if 2==2:
    print('condition true')

if 2==3 and 2==2:
    print('not true')
elif 2==2:
    print('true')
else:
    print('false')

a=[1,2,3]
b=[1,2,3]

print(id(a))  #Memory address
print(id(b))

if a == b:
    print('a and b equal')
if id(a)==id(b):
    print('both memory equals')

#For
print()
print()
print()
num=[1,2,3,4,5]

for number in num:
    if number==3:
        print('three')
        break
    print('number',number)


for number in num:
    for letter in 'abc':
        print(number, letter)

for i in range(1, 5):
    print(i)

#while
x=10

while x<20:
    print(x)
    x+=1