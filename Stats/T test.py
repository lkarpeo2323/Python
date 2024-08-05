import numpy as np
from scipy import stats
import pandas as pd

data = pd.read_excel('excel.xlsx')

clicks = data['Clicks']
position = data['Position']

# Perform t-test
t_stat, p_value = stats.ttest_ind(clicks, position, equal_var=False)

# Print results
print(f"T-Statistic: {t_stat:.3f}")
print(f"P-Value: {p_value:.3f}")

# Interpret the results
if p_value < 0.05:
    print("There is a significant difference between the clicks and position.")
else:
    print("There is no significant difference between the clicks and position.")
