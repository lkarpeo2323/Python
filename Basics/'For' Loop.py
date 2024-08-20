#Level 1

text = 'Hello World'
for i in text:
    print(i)




#Level 2

text = 'hello world'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in text:
    index = alphabet.find(i)
    print(i, 'is', index)


#Level 3

text = 'hello world'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
mom = ' '
for char in text:
    if char == ' ':
        mom += char
    else:
        index = alphabet.find(char)
        print(char, 'is', index) # There is no space included in the index





