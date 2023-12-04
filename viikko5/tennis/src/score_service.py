class ScoreService:

    
    ADVANTAGE_SCORE = {1: "Advantage player1",
                       -1: "Advantage player2"}
    
    SCORE = {0: "Love",
             1: "Fifteen",
             2: "Thirty",
             3: "Forty"}

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def equal_result(self, score):
        if score <= 2:
            return f"{self.SCORE[score]}-All"
        else:
            return "Deuce"
        
    def advantage_result(self, minus_result):
        return self.ADVANTAGE_SCORE[minus_result]
        
    def get_winner(self):
        if self.player1.score > self.player2.score:
            return f"Win for {self.player1.name}"
        else:
            return f"Win for {self.player2.name}"
    
    def get_result(self):
        return f"{self.SCORE[self.player1.score]}-{self.SCORE[self.player2.score]}"
    