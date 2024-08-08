# Import the necessary modules from pydfs_lineup_optimizer
from pydfs_lineup_optimizer import Site, Sport, get_optimizer
import pandas as pd

# Initialize the optimizer for Yahoo DFS and baseball
optimizer = get_optimizer(Site.YAHOO, Sport.BASEBALL)

# Load player data from a CSV file
optimizer.load_players_from_csv("fantasy.csv")

# Access the player pool
pool = optimizer.player_pool

#Exclude a Player
optimizer.player_pool.remove_player('Adrian Del Castillo')
optimizer.player_pool.remove_player('Jordan Montgomery')
optimizer.player_pool.remove_player('Brandon Marsh')

#Lock a Player
optimizer.player_pool.lock_player('Randal Grichuk')
optimizer.player_pool.lock_player('Josh Lowe')
optimizer.player_pool.lock_player('Brandon Lowe')
optimizer.player_pool.lock_player('Bryan Woo')
optimizer.player_pool.lock_player('Trea Turner')


#Exclude Teams
optimizer.player_pool.exclude_teams(['NYY', 'LAA'])


# Set max exposure for all players
for player in pool.all_players:
    player.max_exposure = .6

# Optimize lineups with the specified exposure limits
lineup_generator = optimizer.optimize(n=20)

# Print each optimized lineup
for lineup in lineup_generator:
    print(lineup)

# Print statistics related to the optimization process
optimizer.print_statistic()
