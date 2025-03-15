import os
from datetime import  datetime

print(dir(os))                                                      #show all attributes and methods os has to access

os.chdir('/Users/vikashkumar/PycharmProjects/')                     #change directory

print(os.getcwd())                                                  #return current working dir

#os.mkdir('vikash-python')                                          #create directory

#os.makedirs('vikash-python-deep/deep-dir')                          # create deep directory ie. dir inside dir.

#os.rmdir('vikash-python')

#os.removedirs('vikash-python-deep/deep-dir')

#os.rename('vikash-python', 'vikash-renamed-python')

print(os.stat('vikash-renamed-python'))

mod_time=os.stat('vikash-renamed-python').st_mtime

print(datetime.fromtimestamp(mod_time))

# for dirPath, dirNames, fileNames in os.walk('/Users/vikashkumar/PycharmProjects/'):          #print directories along with file contents inside it
#         print('directory path: ',dirPath)
#         print('directory name: ',dirNames)
#         print('File Names: ',fileNames)
#         print()


print()
print()
print(os.environ.get('HOME'))                                        #GET home dir from environment

#combine two paths

new_path=os.path.join(os.environ.get('HOME'),'vikash-python')        #join base path with new
print(new_path)

print(os.path.exists('vikas'))                                       #check if path exist

os.path.isdir('vfvfv')
os.path.isfile('vikas')

os.path.splitext('vikash/vik.txt')                                   #split extension



