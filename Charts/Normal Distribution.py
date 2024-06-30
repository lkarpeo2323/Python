import numpy
import matplotlib.pyplot as plt

# normal distribution of 500 numbers 
# mean of 5 
# standard deviation of 1

x = numpy.random.normal(5.0, 1.0, 500)

print(x)


plt.hist(x, 100)
plt.show()

