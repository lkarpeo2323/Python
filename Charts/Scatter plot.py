import matplotlib.pyplot as plt

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [1,2,0,1,2,0,0,1,2,0] #Clases represent different colors

plt.scatter(x, y, c=classes)
plt.show()
