import pandas as pd
from scipy import stats

data = pd.read_excel('excel.xlsx')

describe = data.describe()

print(describe)



