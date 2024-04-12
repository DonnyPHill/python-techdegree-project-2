# import constants and deepcopy

import constants
from copy import deepcopy

# deepcopy data, convert heights to int, experience to True or False
# and seperate guardians into list


def clean_data(teams_unclean, players_unclean):
    teams_clean = deepcopy(teams_unclean)
    players_clean = deepcopy(players_unclean)
    for player in players_clean:
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
        player["height"] = int(player["height"].split(" ")[0])
        player["guardians"] = player["guardians"].split(" and ")
    return teams_clean, players_clean

# iterate through list of players and add experienced players to team
# and then iterate again to add inexperienced


def balance_teams():
    team_number = 1
    for player in players:
        if player["experience"] is True:
            player["team"] = team_number % 3 - 1
            if player["team"] == -1:
                player["team"] = 2
            team_number += 1
    team_number = 1
    for player in players:
        if player["experience"] is False:
            player["team"] = team_number % 3 - 1
            if player["team"] == -1:
                player["team"] = 2
            team_number += 1

# display main menu and ask for choice between team menu and quitting app


def main_menu():
    quit_app = 0
    while True:
        print("\n---- MENU ----\n")
        print("Here are your choices:")
        print(" 1)  Display Team Stats")
        print(" 2)  Quit\n")
        while True:
            menu_choice = input("Enter an Option:  ")
            if menu_choice == "1":
                team_menu()
                break
            elif menu_choice == "2":
                quit_app = 1
                break
            else:
                print("\nPlease press 1 to display team stats or 2 to quit\n")
        if quit_app == 1:
            break

# display team menu and ask for choice of team then display that teams stats


def team_menu():
    print(f"\n1) {teams[0]}")
    print(f"2) {teams[1]}")
    print(f"3) {teams[2]}\n")
    while True:
        try:
            team_choice = int(input("Enter an option: "))
            if team_choice < 1 or team_choice > 3:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nPlease press 1, 2 or 3 for team stats\n")
    players_per_team = 0
    players_on_team = []
    guardians_on_team = []
    number_of_experienced = 0
    number_of_inexperienced = 0
    average_height = 0
    for player in players:
        if player["team"] == team_choice - 1:
            players_on_team.append(player["name"])
            guardians_on_team.append(player["guardians"])
            if player["experience"] is True:
                number_of_experienced += 1
            else:
                number_of_inexperienced += 1
            average_height += player["height"]
            players_per_team += 1
    print(f"\nTeam: {teams[team_choice - 1]} Stats")
    print("-" * len(f"Team: {teams[team_choice - 1]} Stats"))
    print(f"Total players: {players_per_team}")
    print(f"Total experienced: {number_of_experienced}")
    print(f"Total inexperienced: {number_of_inexperienced}")
    print(f"Average height: {round((average_height / players_per_team), 1)}",
          " in.\n")
    print("Players on Team:")
    print(f"  {", ".join(players_on_team)}\n")
    print("Guardians:")
    print(f"  {", ".join(guardian for guardians in guardians_on_team for guardian in guardians)}\n")
    input("Press ENTER to continue...")

# make sure nothing can be run by importing this app into another


if __name__ == "__main__":
    print("BASKETBALL TEAM STATS TOOL")
    teams, players = clean_data(constants.TEAMS, constants.PLAYERS)
    balance_teams()
    main_menu()
    print("\nThank you for using the BASKETBALL TEAMS STATS TOOL app.",
          "Have a nice day!")
