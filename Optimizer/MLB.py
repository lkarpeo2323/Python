# Import the necessary modules from pydfs_lineup_optimizer
from pydfs_lineup_optimizer import Site, Sport, get_optimizer

# Initialize the optimizer for Yahoo DFS and baseball
optimizer = get_optimizer(Site.YAHOO, Sport.BASEBALL)

# Load player data from a CSV file
optimizer.load_players_from_csv("newnewnew.csv")

# Optimize lineups, specifying the number of lineups to generate
lineup_generator = optimizer.optimize(10)

# Print each optimized lineup
for lineup in lineup_generator:
    print(lineup)

# Print statistics related to the optimization process
optimizer.print_statistic()
