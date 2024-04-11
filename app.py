#importing constants because it is the data to be used
#and copy for deepcopy

import constants
from copy import deepcopy

#Convert heights to ints and experience to True or False

def clean_data():    

    for player in players:
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
        player["height"] = int(player["height"].split(" ")[0])
        player["guardians"] = player["guardians"].split(" and ")

def balance_teams():
    team_number = 1
    for player in players:
        player["team"] = team_number % 3 - 1
        if player["team"] == -1:
            player["team"] = 2
        team_number += 1

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
    team_choice -= 1    
    print(f"\nTeam: {teams[team_choice]} Stats")
    print("-" *len(f"Team: {teams[team_choice]} Stats"))
    print(f"Total players: {players_per_team}\n")
    print("Players on Team:")
    players_on_team = []
    for player in players:
        if player["team"] == team_choice:
            players_on_team.append(player["name"])    
    print(f"  {", ".join(players_on_team)}\n")
    input("Press ENTER to continue...")


if __name__ == "__main__":
    players = deepcopy(constants.PLAYERS)
    teams = deepcopy(constants.TEAMS)
    players_per_team = int(len(players)/len(teams))
    clean_data()
    balance_teams()
    print("BASKETBALL TEAM STATS TOOL")
    main_menu()
    print("Thank you for using the BASKETBALL TEAMS STATS TOOL app.  Have a nice day!")
        
