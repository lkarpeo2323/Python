import pandas as pd
from scipy import stats

# Create sample data and load it into a DataFrame
data = pd.DataFrame({
    'x': [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6],
    'y': [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6],
    'z': [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
})

# Get descriptive statistics for 'x'
leo = data.describe()

# Print the descriptive statistics
print(leo)
