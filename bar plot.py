import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

sns.barplot(x='Department', y='MonthlyIncome', data=data)

# Set the label for the x-axis
plt.xlabel('Department')

# Set the label for the y-axis
plt.ylabel('Monthly Income')

# Set the title of the plot
plt.title('Bar Plot of Monthly Income by Department')

# Display the plot
plt.show()
