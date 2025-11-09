from playerreader import PlayerReader

class PlayerStats:
    
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.fetch_data()

    def top_scorers_by_nationality(self, nationality):
        players_nationality = [player for player in self.players if player.nationality == nationality]
        players_nationality.sort(key=lambda a: a.points, reverse=True)
        return players_nationality