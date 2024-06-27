import matplotlib.pyplot as plt
import numpy as np

y = [35, 25, 25, 15]
x = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = x)
plt.legend()
plt.show() 
