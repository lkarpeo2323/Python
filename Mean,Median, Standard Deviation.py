import pandas as pd
import numpy as np

x = pd.Series([2.2,2.3,4.5,2.2,2.5])

mean = np.mean(x)
median = np.median(x)
std = np.std(x)

print(f"The mean is {mean}")
print(f"The median is {median}")
print(f"The standard deviation is {std}")