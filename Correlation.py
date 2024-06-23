import pandas as pd

# Data
data = {
    'Keywords': ['Carl', 'Cooper','Rebecca', 'Mom','Abie', 'Leo'],
    'Position': [22, 15, 5, 43, 3, 35],
    'Search Volume': [90, 10, 10, 20, 20, 260]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df['Position'].corr(df['Search Volume'])
correlation
