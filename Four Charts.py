import matplotlib.pyplot as plt
import numpy as np

# Bar Chart
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

plt.subplot(1, 4, 1)
plt.bar(x1, y1)
plt.title('Bar Chart')

# Line Chart
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

plt.subplot(1, 4, 2)
plt.plot(x2, y2)
plt.title('Line Chart')

# Scatter Plot
x3 = np.array([0, 1, 2, 3])
y3 = np.array([5, 15, 25, 35])

plt.subplot(1, 4, 3)
plt.scatter(x3, y3)
plt.title('Scatter Plot')

# Pie Chart
x4 = np.array(["Apples", "Bananas", "Cherries", "Dates"])
y4 = np.array([35, 25, 25, 15])

plt.subplot(1, 4, 4)

x4 = ["Apples", "Bananas", "Cherries", "Dates"]
y4 = [35, 25, 25, 15]

plt.pie(y4, labels = x4)
plt.legend()
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show() 
