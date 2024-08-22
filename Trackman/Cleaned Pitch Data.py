import pandas as pd

# Load the Excel file
df = pd.read_excel('Clean.xlsx')

# Mapping the desired columns to their actual names in the Excel file
columns_to_keep = [
    'Pitcher',            
    'Rel Speed',          
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
    'Auto Hit Type',
    'Batter Side'
    
]

# Select the relevant columns
cleaned_df = df[columns_to_keep]

# Save the cleaned data to a new CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)

# Print a message indicating completion
print("Cleaned data has been saved to 'cleaned_data.csv'.")
