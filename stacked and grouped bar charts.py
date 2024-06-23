import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

# plotting a Grouped Bar Chart
pd.crosstab(data['Attrition'], data['Department']).plot(kind = 'bar', stacked = False)

# plotting a Stacked Bar Chart
pd.crosstab(data['Attrition'], data['Department']).plot(kind = 'bar', stacked = True)

plt.show()



