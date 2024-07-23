import pandas as pd
import random

# Load player data from CSV file
player_data = pd.read_csv('csv-baseball.csv')

# Parse player data into a list of dictionaries
players = []
for index, row in player_data.iterrows():
    player = {
        'ID': row['ID'],
        'First Name': row['First Name'],
        'Last Name': row['Last Name'],
        'ID + Name': row['ID + Name'],
        'Position': row['Position'],
        'Team': row['Team'],
        'Opponent': row['Opponent'],
        'Game': row['Game'],
        'Time': row['Time'],
        'Salary': int(row['Salary']),
        'FPPG': float(row['FPPG']),
        'Probable Pitcher': row['Probable Pitcher'],
        'Injury Status': row['Injury Status'],
        'Starting': row['Starting']
    }
    players.append(player)

# Function to generate a lineup
def generate_lineup(players, budget=200):
    positions = ['P', 'P', 'C', '1B', '2B', '3B', 'SS', 'OF', 'OF', 'OF']
    lineup = []
    total_salary = 0
    random.shuffle(players)

    for position in positions:
        for player in players:
            if player['Position'] == position and player['Salary'] + total_salary <= budget:
                lineup.append(player)
                total_salary += player['Salary']
                break

    return lineup

# Generate 10 lineups
lineups = [generate_lineup(players) for _ in range(10)]

# Display the lineups
for i, lineup in enumerate(lineups):
    print(f"Lineup {i+1}:")
    for player in lineup:
        print(f"{player['ID + Name']} - {player['Position']} - ${player['Salary']} - {player['FPPG']} FPPG")
    print(f"Total Salary: {sum(player['Salary'] for player in lineup)}\n")
