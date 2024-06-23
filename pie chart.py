import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

department_counts = data['Department'].value_counts()

# Extract the department names as categories
categories = department_counts.index.tolist()

# Extract the count of employees as proportions
proportions = department_counts.values.tolist()

# Create a pie chart with the proportions and labels
plt.pie(proportions, labels=categories, autopct='%1.1f%%')

# Set the title of the chart
plt.title('Pie Chart of Departments')

# Display the chart
plt.show()
