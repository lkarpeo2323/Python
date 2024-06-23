import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')


# Calculate the count of employees in each department based on gender
department_gender_counts = data.groupby(['Department', 'Gender']).size().reset_index(name='Count')

# Create a line chart to visualize the count of employees by department and gender
sns.lineplot(x='Department', y='Count', hue='Gender', data=department_gender_counts)

# Set the labels for the x-axis and y-axis
plt.xlabel('Department')
plt.ylabel('Count')

# Set the title of the plot
plt.title('Line Chart of Employee Count by Department and Gender')

# Display the plot
plt.show()