message="Hello world"
print(message[0])
print(message[0:4])  #4 not included
print(message[:5])
print(message[6:])
print(message.upper())
print(message.count('l'))
print(message.find('world'))

message1=message.replace('l','b')
print(message1)
print(message)                                     #not change
print(message+' '+message1)                        #concatenate

#Note concat with + is costly operation

msg='{},{}'.format(message,message1)
print('message '+msg)

print(dir(msg))   #gives all attributes, methods available on this msg
print(help(str.lower))