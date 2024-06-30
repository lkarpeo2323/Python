import matplotlib.pyplot as plt
%matplotlib inline

values = [5,8,9,10,4,7]
colors = ['b','g','r','c','m','y']
labels = ['A','B','C','D','E','F']
explode = (0,0.2,0,0,0,0)

plt.pie(values, colors = colors, labels=labels, 
explode=explode, autopct= '%1.1f%%', counterclock=False, shadow=True)

plt.title('Values')

plt.show()