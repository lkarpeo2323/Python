import pandas as pd
from collections import Counter

data = pd.read_excel('links.xlsx')

counts = Counter(data['link'])

print("Link counts:")
for link, count in counts.items():
    print(f"{link}: {count}")
