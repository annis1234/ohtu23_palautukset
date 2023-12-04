class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_name(self):
        return self.name
    
    def score(self):
        return self.score
    
    def add(self):
        self.score +=1
        return self.score
