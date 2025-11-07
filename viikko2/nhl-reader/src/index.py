import requests
from player import Player

def main():


    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("Enter nationality")
    given_nationality = input()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == given_nationality:
           players.append(player)

    #Kysytty Currechatilta miten voidaan tulostaa sanakirjasta sisältö vain tietyn arvon perusteella, mutta ratkaisu ei hyvä.

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
