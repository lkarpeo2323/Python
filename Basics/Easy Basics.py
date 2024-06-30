import pandas as pd
import numpy as np



text = "Schnitzel"
print(text[4]) #Output is 'i'
print(text[-3]) #Output is 'z'
print(text[0:4]) #Output is 'Schn'
print(text[2:6]) #Output is 'hnit'
print(text[:3]) #Output is 'Sch'
print(text[2:]) #Output is 'hnitzel'
print(text.upper())  # Output: 'SCHNITZEL'
print(text.lower())  # Output: 'schnitzel'
print(text.capitalize())  # Output: 'Schnitzel'
print(len(text)) #Output is 9 (Length of text)
print(text.find('t')) #Output is 5 (Find location of 't')
print(text[1::2]) #Output is 'cnte'


# For Loop
for i in range (0, 10):
    print(i)

#While Loop
j = int(input("input a number below 15: "))

while (j<15):
    print(j)
    j = j+1


#Easy Math

a = int(input("input a number for A: "))
b = int(input("input a number for B: "))

sum = a + b
diff = a - b
mult = a * b
div = a / b


print(f"a is equal to {a}")
print(f"b is equal to {b}")
print(f"The sum of the numbers is {sum}")
print(f"The difference of the numbers is {diff}")
print(f"The product of the numbers is {mult}")
print(f"The quotient of the numbers is {div}")

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# Mean and median

x = pd.Series([2.2,2.3,4.5,2.2,2.5])

mean = np.mean(x)
median = np.median(x)
print(f"The mean is {mean}")
print(f"The median is {median}")


#return

def mom(x):
    return x + 2

leo = mom(3)

print(leo) #Output is 5
