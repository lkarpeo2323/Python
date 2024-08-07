import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel('Word Counts.xlsx')

over = data['Over']
under = data['Under']


plt.plot(over, label='Pages with Over 1558 Word Count') 
plt.plot(under, label='Pages with Under 1558 Word Count')
plt.ylabel('Clicks') #label on the y-axis
plt.legend()
plt.show()
