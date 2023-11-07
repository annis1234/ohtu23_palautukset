from player import Player

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def get_players(self):
        return self.reader.read_file()
    
    def get_points(self, player):
        return player.points
    
    def top_scorers_by_nationality(self, nationality):
        players = []

        for player_dict in self.get_players():
            if player_dict['nationality'] == nationality:
                player = Player(player_dict)
                players.append(player)

        sorted_players = sorted(players, reverse=True, key=self.get_points)

        return sorted_players