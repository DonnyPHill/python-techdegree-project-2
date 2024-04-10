#importing constants because it is the data to be used
#and copy for deepcopy

import constants
from copy import deepcopy

#Convert heights to ints and experience to True or False

def clean_data():    
    players = deepcopy(constants.PLAYERS)
    for player in players:
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
        player["height"] = int(player["height"].split(" ")[0])
        player["guardians"] = player["guardians"].split(" and ")








if __name__ == "__main__":
    clean_data()
    
    
    
    
