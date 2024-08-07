import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('Word Counts.xlsx')

x = data['Word Count']
y = data['Clicks']


plt.scatter(x,y)
plt.show() 
