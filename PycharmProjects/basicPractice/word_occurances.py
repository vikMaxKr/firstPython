s = "I work in bloomberg founded by bloomberg work work"

# Split the string into words
words=s.split(' ')
cache={}

for word in words:
    if word in cache:
        cache[word] +=1
    else:
        cache[word]=1

print(cache)

#####################

def sum(a,b):
    return a+b

n1=int(input('enter first number: '))
n2=int(input('enter first number: '))
print('sum is: ',sum(n1,n2))


