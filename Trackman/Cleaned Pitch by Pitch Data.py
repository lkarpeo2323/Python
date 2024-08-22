import pandas as pd

# Load the Excel file
df = pd.read_excel('Clean.xlsx')


# Mapping the desired columns to their actual names in the Excel file
columns_to_keep = [
    'Pitcher',            
    'Velocity',           # 'Rel Speed' will be renamed to 'Velocity'
    'Pitch Type',       # 'Auto Pitch Type' will be renamed to 'Pitch Type'
    'Spin Rate',          
    'Rel Height',         
    'Rel Side',           
    'Extension',          
    'Induced Vert Break', 
    'Horz Break',          
    'Batter',
    'Balls',
    'Strikes',
    'Pitch Call',
    'Hit Type',    # 'Auto Hit Type' will be renamed to 'Hit Type'
    'Exit Velocity',    # 'Exit Speed' will be renamed to 'Exit Velocity'
    'Batter Side'
]

# Rename columns (check comments above)
df.rename(columns={'Rel Speed': 'Velocity', 'Auto Pitch Type': 'Pitch Type','Auto Hit Type': 'Hit Type', 'Exit Speed': 'Exit Velocity'}, inplace=True)

# Select the relevant columns
cleaned_df = df[columns_to_keep]

# Save the cleaned data to a new CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)

# Print a message indicating completion
print("Cleaned data has been saved to 'cleaned_data.csv'.")
