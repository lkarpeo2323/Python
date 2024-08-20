#Level 1

text = 'Hello World'
for i in text:
    print(i)




#More advanced 

text = 'hello world'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in text:
    index = alphabet.find(i)
    print(i, 'is', index)
