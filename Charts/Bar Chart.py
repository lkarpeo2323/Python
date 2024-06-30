import matplotlib.pyplot as plt
%matplotlib inline

values = [5,8,9,10,4,7]
widths = [0.7, 0.8, 0.7 , 0.7, 0.7 , 0.7]
colors = ['b','r','b','b','b','b']

plt.bar(range(0,6), values, width=widths, 
color=colors, align='center')


plt.show()