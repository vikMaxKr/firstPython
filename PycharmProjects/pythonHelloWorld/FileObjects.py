
file=open('file.txt', 'r')  #default file to read
print(file)
print(file.mode)            #return different mode file is in like r=read, w=write
file.close()                #close file after open always!

#using context manager

with open('file.txt','r') as f:   #It automatically closes file even in exception scenario
    #print(f)
    # for line in f:
    #     print(line)
    # read_contents=f.read(20)    #read only first 20 char
    # read_lines=f.readlines()
    # read_line=f.readline()
    # print(read_contents)

    # chunk_size=10
    # f_contents=f.read(chunk_size)
    # print(f.tell())                  #return current position in file
    # print(type(f_contents))
    #
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(chunk_size)

    chunk_size = 10
    f_contents = f.read(chunk_size)
    print(f_contents)

    f.seek(0)                        # It ensures next f_contents start from next line of file instead of next char

    f_contents = f.read(chunk_size)
    print(f_contents)


#write in file
# with open('file-write.txt', 'w') as f_write:    #create new file if isn't exist ; if file exist it overwrite it ; to append in existing file use 'a' instead of 'w'
#      f_write.write('Vikash written to file from Python')
#      f_write.seek(0)
#      f_write.write("Akash ")

with open('file.txt', 'r') as rf:
    with open('file-copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)




print(f.closed)
#print(f)