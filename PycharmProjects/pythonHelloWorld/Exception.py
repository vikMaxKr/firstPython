from linecache import cache

try:
    f=open('file22.txt')
    if 'file22.txt'==f.name:
        raise Exception                  #  Raising exception manually
except FileNotFoundError as e:
    print("sorry this file does'nt exist",e)
except Exception as e:
    print("something went wrong!",e)
else:                                   # this executes when no exception in try
    print("no exception thrown !")
finally:
    print("finally always runs")
