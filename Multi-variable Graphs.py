import matplotlib.pyplot as plt
%matplotlib inline

values = [1,5,8,9,2,0,3,10,4,7]
values2 = [3,8,9,2,1,2,3,4,6,6]

plt.plot(range(1,11), values, 'o--')
plt.plot(range(1,11), values2, 'v:')

plt.show()
