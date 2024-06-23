import pandas as pd
import numpy as np

x = pd.Series([2.2, 2.3, 4.5, 2.2, 2.5])

mean = np.mean(x)
median = np.median(x)
std = np.std(x)

outliers = []

for item in x:
    if (item < mean - std) or (item > mean + std):
        outliers.append(item)
print(outliers)

