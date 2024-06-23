import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Survived': [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    'Age': [23, 43, 23, 23, 43, 52, 54, 24, 45, 53, 42]
})

# Calculate the count of passengers who died and survived by age
survived_by_age = data[data['Survived'] == 1]['Age']
died_by_age = data[data['Survived'] == 0]['Age']

# Plot the stacked bar chart
plt.hist([survived_by_age, died_by_age], bins=10, color=['blue', 'red'], stacked=True, label=['Survived', 'Died'])
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Survival Status by Age')
plt.legend()
plt.show()
