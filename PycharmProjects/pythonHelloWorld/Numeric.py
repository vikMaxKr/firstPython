from operator import indexOf
from xml.dom import NOT_FOUND_ERR

print(3/2)  #1.5
print(3//2)
print(round(2.345,2))

##########
#List
courses=['History','Physics','Maths']
courses_extra=['Quantum']
courses.insert(0,'Geography')
courses.append('Environmental')

str_joined='. '.join(courses)
print(str_joined)

#str_joined.split('')

print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:4])
print(courses[:3])

#Note extend vs append
courses.append(courses_extra)
print(courses)
courses.extend(courses_extra)
print(courses)

courses.remove('Quantum')
return_list=courses.pop()    #pop return poped data
courses.reverse()
courses.sort(reverse=True)

sorted_courses=sorted(courses)      #does not sort original list

print(courses)

num=[1,2,3,4,5]
print(max(num))
print(sum(num))

print(num.index(2))
print(3 in num)

for number in num:
    print(number)

for index, number in enumerate(num,start=1):
    print(index, number)



#Tuples
#Immutable

tuple1=('History','Physics','Maths')
tuple2=tuple1

print(tuple2)
print(tuple1)

#tuple1[0]='vik' #error

##Set
set_courses={'History','Physics','Maths','History','Physics','Maths'}  #does not maintain insertion order
print(set_courses)
set1_courses={'History','Physics','Maths','Geo'}

print(set1_courses.intersection(set_courses))
print(set1_courses.difference(set_courses))
print(set1_courses.union(set_courses))

#creating empty list, set, tuples
empty_list=[]
empty_list1=list()

empty_set=set()
empty_set1={}    # This is incorrect as it creates dict not set

empty_tuple=()
empty_tuple1=tuple()

###########################
#Dictionary
print()
print()
student={'name': 'vikash', 'roll': 123, 'age': 23, 'courses':['History', 'Geo']}
print(student['name'])
print(student.get('course'))  #if not present return none
print(student.get('course',NOT_FOUND_ERR))

#Adding new key-value
student['color']='White'
student['name']='Rinku' #update existing
student.update({'name': 'Tinku'})

#Delete
del student['name']
pop_age=student.pop('age')
print(pop_age)
print(student)
print(student.values())
print(student.keys())
print(student.items())

for key,value in student.items():
    print(key, value)
