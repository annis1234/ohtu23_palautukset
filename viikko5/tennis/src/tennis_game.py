from player import Player
from score_service import ScoreService

class TennisGame:

    def __init__(self, player1_name, player2_name):

        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

        self.score_service = ScoreService(self.player1, self.player2)

    def won_point(self, player):
        if player == "player1":
            self.add_score(self.player1)
        else:
            self.add_score(self.player2)

    def add_score(self, player):
        return player.add()

    def get_score(self):
        if self.player1.score== self.player2.score:
            return self.score_service.equal_result(self.player1.score)
        
        elif self.player1.score>= 4 or self.player2.score >= 4:
            minus_result = self.player1.score- self.player2.score

            if minus_result == 1 or minus_result == -1 :
                return self.score_service.advantage_result(minus_result)
            else:
                return self.score_service.get_winner()
            
        else:
            return self.score_service.get_result()