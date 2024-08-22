import pandas as pd

# Load the CSV file
df = pd.read_csv('example_game_data.csv')


# Define the order of columns for optimized analysis
columns_to_keep = [
    # Pitch information
    'PitchNo',
    'PitchofPA',
    'PAofInning',
    'PitcherTeam',
    'Pitcher',
    'PitcherThrows',
    'BatterTeam',
    'Batter',
    'BatterSide',
    
    # Pitch characteristics
    'Pitch Velocity',
    'TaggedPitchType',
    'PitchCall',         
    'Hit Type',  # 'TaggedHitType' renamed to 'Hit Type'
    
    # Spin and angle data
    'VertRelAngle',
    'HorzRelAngle',
    'SpinRate',
    'SpinAxis',
    'Tilt',
    
    # Release and trajectory details
    'RelHeight',
    'RelSide',
    'Extension',
    'VertBreak',
    'HorzBreak',
    'PlateLocHeight',
    'PlateLocSide',
    
    # Flight and impact metrics
    'ZoneSpeed',
    'VertApprAngle',
    'HorzApprAngle',
    'ZoneTime',
    'Exit Velocity',  # 'ExitSpeed' was renamed to 'Exit Velocity'
    'Angle',
    'Direction',
    'Distance',
    
    # Results
    'PlayResult'
]

# Rename columns (check comments above)
df.rename(columns={'RelSpeed': 'Pitch Velocity', 'ExitSpeed': 'Exit Velocity', 'TaggedHitType': 'Hit Type'}, inplace=True)


# Select the relevant columns in the specified order
cleaned_df = df[columns_to_keep]

# Save the cleaned data to a new CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)

# Print a message indicating completion
print("Cleaned data has been saved to 'cleaned_data.csv'.")
