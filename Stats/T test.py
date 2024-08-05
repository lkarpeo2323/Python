
import numpy as np
from scipy import stats
import pandas as pd



data = pd.read_excel('t test.xlsx')


under = data['Clicks']
over = data['Clicks over']

# Example data


# Perform t-test
t_stat, p_value = stats.ttest_ind(under, over, equal_var=False)

# Print results
print(f"T-Statistic: {t_stat:.3f}")
print(f"P-Value: {p_value:.3f}")

# Interpret the results
if p_value < 0.05:
    print("There is a significant difference between the over and under.")
else:
    print("There is no significant difference between the clicks for Position 1 and other positions.")
