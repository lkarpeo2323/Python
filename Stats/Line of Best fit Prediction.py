import numpy

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
y = [12.4, 15.0, 10.5, 18.3, 20.0, 14.2, 25.5, 18.9, 22.1, 30.2, 18.7, 16.5, 21.3, 24.0, 19.8, 23.4, 27.5]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

score = mymodel(18)
print(score)


