class Player:

#Kysytty Currechatilta mitä ohjelma tekee ja miten __str___ kannattaa määritellä

    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals'] 
        self.team = dict['team'] 
        self.games = dict['games']
        self.id = dict['id']

    def __str__(self):
        return f"{self.name}, {self.nationality}, {self.assists}, {self.goals}, {self.team}, {self.games}, {self.id}"