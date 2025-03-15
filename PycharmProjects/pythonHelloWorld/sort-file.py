import os
import  csv
from opcode import opname

from OperatingSystem import new_path

os.chdir('/Users/vikashkumar/PycharmProjects/pythonHelloWorld/filesSort')

curr_dir=os.curdir

# for f in os.listdir():
#     print(f)

# for f in os.listdir():
#    file_name,file_ext=os.path.splitext(f)
#    course=file_name.split(' ')
#    f_num=course[2].strip()[1:].zfill(2)
#    f_owner=course[0].strip()
#    f_file=course[1].strip()
#    new_name='{}-{}{}{}'.format(f_num,f_owner,f_file,file_ext)
#    print(new_name)
#    #print({file_owner})
#    os.rename(f, new_name)

#print(curr_dir)

#reading from csv

# with open('first.csv','r') as csv_file:
#    csv_reader=csv.reader(csv_file)
#
#    next(csv_reader)       #skip first line in csv ie heading
#    for line in csv_reader:
#       print(line[2])

# with open('first.csv','r') as csv_file:
#    csv_reader=csv.reader(csv_file)
#
#    with open('writer.csv','w') as csv_writer:
#       new_file=csv.writer(csv_writer,delimiter='-')
#
#       for line in csv_reader:
#        new_file.writerow(line)

# with open('writer.csv','r') as csv_file:
#    csv_reader=csv.reader(csv_file,delimiter='-')
#    for line in csv_reader:
#     print(line)

#using dictionary reader/writer

# with open('first.csv','r') as dic_reader:
#     dic_read=csv.DictReader(dic_reader)
#     for line in dic_read:
#         print(line['email'])              #we can access by heading

with open('first.csv','r') as csv_file:
   csv_reader=csv.reader(csv_file)

   with open('writer.csv','w') as csv_writer:
       fields_name = ['first_name', 'last_name', 'email']
       new_file=csv.DictWriter(csv_writer,fieldnames=fields_name,delimiter=',')
       new_file.writeheader()
       for line in csv_reader:
         new_file.writerow(line)

