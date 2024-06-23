import numpy
import matplotlib.pyplot as plt

#Generate random numbers
x = numpy.random.uniform(0.0, 5.0, 250)

#plot the historgam
plt.hist(x, 5)
plt.show()