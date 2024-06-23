import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('employee.csv')


print(data)

sns.histplot(data['YearsSinceLastPromotion'])

plt.show()
