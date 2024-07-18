import pandas as pd

data = pd.read_excel('Issues.xlsx')

print(data['Page URL'].tolist())
