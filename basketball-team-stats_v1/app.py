"""
Python Development Techdegree
Project 2 - Basketball Team Stats
-----------------------------------
"""

# NOTES ON STEP 0:
# Import copy to copy our data from file.
# Import time for use with time.sleep method to adjust app loading times.
# Import TEAMS and PLAYERS directly from constants.py to synch our list with the app.

import copy
import time
from constants import TEAMS, PLAYERS

# NOTES ON STEP 1:
# Clean players list: Iterates through player list
# Convert "height" properties to integers
# Change "experience" properties to boolean values
# Split guardians into a list of strings and remove whitespaces


def players_list(players):
    for player in players:
        player["height"] = int(player["height"][0:2])

        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False

        guardians_split = player["guardians"].split("and")
        player["guardians"] = [guardian.strip() for guardian in guardians_split]

    return players

# NOTES ON STEP 2:
# Create function for team equalizer
# Separate experienced and inexperienced players into separate lists
# Iterate over the two separate lists to divide players equally among teams


def balance_teams(players_team_list):
    panthers = []
    bandits = []
    warriors = []
    experienced = []
    inexperienced = []

    for player in players_team_list:
        if player["experience"]:
            experienced.append(player)
        else:
            inexperienced.append(player)

    for num, player in enumerate(experienced, start=1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    for num, player in enumerate(inexperienced, start=1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors

# NOTES ON STEP 3
# Create function for the team stats have it hold empty list to hold the player values.
# Used list comprehension for a "cleaner" display of different values within the list.
# Iterate over the players and append their names to the appropriate list based on their experience level.
# I print out both lists of players along with their counts.
# When function show_team_stats is called, it displays the names of both experienced-inexperienced players separately.


def show_team_stats(team, players):
    experienced_players = []
    inexperienced_players = []
    player_height = sum(player["height"] for player in players)
    guardian_names = [guardian for sublist in [player["guardians"] for player in players] for guardian in sublist]

    for player in players:
        if player["experience"]:
            experienced_players.append(player["name"])
        else:
            inexperienced_players.append(player["name"])

    print("<-<-PROFILE->->")
    print("......................")
    print("\n- Team Group: {}\n".format(team))
    print("- Number of Players: {}\n".format(len(players)))
    print("- Experienced:", ", ".join(experienced_players), "\n")
    print("- Inexperienced:", ", ".join(inexperienced_players), "\n")
    print("- Average Height: {} inches\n".format(player_height // len(players)))
    print("- Guardians:", ", ".join(guardian_names))
    print("\n.......................")

    if True:
        continue_app = input("Press 'Enter' to continue...")

# NOTES ON STEP 4
# For this step, I created a menu_selection function where the user can interact and choose accordingly.
# Added our copy.deepcopy of PLAYERS from our source.
# Made a "response" variable that can hold our user's response/input per menu_selection function.
# Created a time load using the time.sleep method to ensure smooth visual transition of data times within the app.


def menu_selection():
    players = players_list(copy.deepcopy(PLAYERS))
    panthers, bandits, warriors = balance_teams(players)

    print("\n--- BASKETBALL TEAM STATS TOOL ---\n")

    while True:
        user_input = input("Type 'S' to Start or 'Q' to Quit: ").strip().lower()
        print("\nLoading...\n\n")
        time.sleep(0.8)

        if user_input == 's':
            print("Welcome to the Basketball Stats Tool!")
            break
        elif user_input == 'q':
            print("You have exited. Thank you for using this application!\n")
            exit()
        else:
            print("\nInvalid input. Please try again.\n")

    while True:
        print("\nSelect a team to view its stats by entering the corresponding number.\n")
        print("1) Panthers\n2) Bandits\n3) Warriors")
        print("\nType 'Q' to Quit\n")
        response = input("Enter key: ").strip().lower()
        print("\nLoading...\n\n")
        time.sleep(1.5)

        if response == '1':
            show_team_stats(TEAMS[0], panthers)
        elif response == '2':
            show_team_stats(TEAMS[1], bandits)
        elif response == '3':
            show_team_stats(TEAMS[2], warriors)
        elif response == 'q':
            print("\nYou have exited. Thank you for using this application!\n")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    menu_selection()
