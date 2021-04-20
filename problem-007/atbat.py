import sys
import math
import string

# Dictionary for storing the at bat values
at_bats = {"K":0,"1B":1,"2B":2,"3B":3,"HR":4}

# Get the number of batters (cases)
cases = int(sys.stdin.readline().rstrip())

# Iterate for each batter
for caseNum in range(cases):

    # Set a count for the current batters and their bases
    player_sum = 0
    # Set a count for the current batters number of at bats
    bat_sum = 0
    # Get player data from file and split into the player name and their at bats at the colon
    player_data = sys.stdin.readline().rstrip().split(":")
    # Split up the at bats for the player into its own list inside the player_data list
    player_data[1] = player_data[1].split(',')

    # Iterate for each at bat the current player hit
    for at_bat in player_data[1]:

        # Edge case for BB which is a void at bat
        if at_bat != "BB":
            # Find the current at bat in the at bat dictionary and pull the value and add it to player_sum
            player_sum += at_bats[at_bat]
            # Increment the at bat count
            bat_sum += 1
        # In case of BB
        else:
            pass

    # Print the player name followed by an = and the player sum divided by the bat count to 3 decimal places
    print(player_data[0] + "=" + "%.3f" % round(player_sum/bat_sum,3))
