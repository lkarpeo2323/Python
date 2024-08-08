# Import the necessary modules from pydfs_lineup_optimizer
from pydfs_lineup_optimizer import Site, Sport, get_optimizer
import pandas as pd

# Initialize the optimizer for Yahoo DFS and baseball
optimizer = get_optimizer(Site.YAHOO, Sport.BASEBALL)

# Load player data from a CSV file
optimizer.load_players_from_csv("meta_data_results.csv")

# Access the player pool
pool = optimizer.player_pool

#EXclude a Player
optimizer.player_pool.remove_player('Bligh Madris')

#Exclude a Team
optimizer.player_pool.exclude_teams(['BAL'])

# Set max exposure for all players
for player in pool.all_players:
    player.max_exposure = 0.6

# Optimize lineups with the specified exposure limits
lineup_generator = optimizer.optimize(n=10)

# Print each optimized lineup
for lineup in lineup_generator:
    print(lineup)

# Print statistics related to the optimization process
optimizer.print_statistic()
