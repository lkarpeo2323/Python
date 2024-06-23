import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

#Create a Historgram 
sns.histplot(data['Age'])

# Create a count plot of the 'BusinessTravel' column in the data
sns.countplot(x=data['BusinessTravel'])

plt.show()
