import numpy as np
from scipy import stats
import pandas as pd



data = pd.read_excel('Issues.xlsx')



other_position_clicks = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 5, 5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1, 9, 8, 8, 8, 5, 3, 2, 2, 1, 1, 14, 8, 8, 3, 3, 2, 1, 1, 1, 1, 6, 3, 2, 1, 20, 2, 1, 1, 4, 1, 2, 1, 1, 1, 1, 1, 13, 1, 1, 1, 2, 2, 10, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

position_1_clicks = [35.0, 27.0, 21.0, 19.0, 14.0, 13.0, 11.0, 10.0, 9.0, 9.0, 8.0, 7.0, 7.0, 6.0, 6.0, 6.0, 5.0, 5.0, 5.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 5.0, 3.0, 2.0, 2.0, 1.0, 1.0]

# Example data


# Perform t-test
t_stat, p_value = stats.ttest_ind(position_1_clicks, other_position_clicks, equal_var=False)

# Print results
print(f"T-Statistic: {t_stat:.3f}")
print(f"P-Value: {p_value:.3f}")

# Interpret the results
if p_value < 0.05:
    print("There is a significant difference between the clicks for Position 1 and other positions.")
else:
    print("There is no significant difference between the clicks for Position 1 and other positions.")
