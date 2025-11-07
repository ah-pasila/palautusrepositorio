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
        self.points = dict['goals'] + dict['assists']
  
    # kysytty Currechatilta miten tulostuksen saa sarakkeistettua

    def __str__(self):
       return f"{self.name:<20} {self.team:<15} {self.assists:<2} + {self.goals:<2} = {self.points}"