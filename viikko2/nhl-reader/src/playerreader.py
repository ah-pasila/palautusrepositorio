import requests
from player import Player

class PlayerReader:
    
    #Kysytty CurreChatilta kertaukseksi, miten tietotyyppi lisätään parametreille
    
    def __init__(self, url: str):
        self.url = url
        self.response = ""


  #Kysytty CurreChatilta apua response-muuttujan saamiseen määritellyksi.

    def fetch_data(self):
        self.response = requests.get(self.url).json()
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players