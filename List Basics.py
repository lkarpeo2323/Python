# Append
names = ["Leo", "Abie", "Rebecca", "Cooper"]
names.append("Carl") #Adding an element
print(names)  # Output: ['Leo', 'Abie', 'Rebecca', 'Cooper', 'Carl']

# Insert
kids = ["Leo", "Abie", "Rebecca", "Cooper"]
kids.insert(1, "Carl") 
print(kids) #Output : ['Leo', 'Carl', 'Abie', 'Rebecca', 'Cooper']

# Extend
child = ["Leo", "Abie", "Rebecca", "Cooper"]
newchild = ["Carl", "Cooper"]
child.extend(newchild)
print(child) #Output: ['Leo', 'Abie', 'Rebecca', 'Cooper', 'Carl', 'Cooper']

# Pop (Remove Item)
teams = ["Mets","Yankees", "Orioles"]
teams.pop(1)
print(teams) #Output: ['Mets', 'Orioles']
