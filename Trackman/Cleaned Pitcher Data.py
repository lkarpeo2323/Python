import pandas as pd

# Load the Excel file
df = pd.read_excel('Clean.xlsx')

# Mapping the desired columns to their actual names in the Excel file
columns_to_keep = [
    'Pitcher',            # Already matches
    'Rel Speed',          # Mapped from 'RelSpeed'
    'Spin Rate',          # Mapped from 'SpinRate'
    'Rel Height',         # Mapped from 'RelHeight'
    'Rel Side',           # Mapped from 'RelSide'
    'Extension',          # Already matches
    'Induced Vert Break', # Mapped from 'InducedVertBreak'
    'Horz Break'          # Mapped from 'HorzBreak'
]

# Select the relevant columns
cleaned_df = df[columns_to_keep]

# Save the cleaned data to a new CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)

# Print a message indicating completion
print("Cleaned data has been saved to 'cleaned_data.csv'.")
