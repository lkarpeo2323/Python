import pandas as pd

# Download the stopwords list

# Read the Excel file
data = pd.read_excel('Issues.xlsx')

# Assuming the URLs are in a column named 'URL'
print(data['Page URL'].tolist())
