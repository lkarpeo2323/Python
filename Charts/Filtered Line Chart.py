import matplotlib.pyplot as plt
import pandas as pd

# Load data from Excel file
data = pd.read_excel('Most Important Words and URLs.xlsx')

# Filter the data where 'Clicks' is more than 50
filtered_data = data[data['Clicks'] > 50]

# Plot the filtered values
plt.plot(filtered_data['Keyword'], filtered_data['Clicks'])
plt.xlabel('Keyword')
plt.ylabel('Clicks')
plt.title('Clicks More Than 50')

# Rotate x-axis labels
plt.xticks(rotation=45)  # You can change 45 to any angle you prefer

plt.show()
