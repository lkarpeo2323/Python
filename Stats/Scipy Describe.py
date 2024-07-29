import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res=describe(v)
print(res)
