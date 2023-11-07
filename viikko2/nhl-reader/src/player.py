class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} team {self.team:5} {self.goals:2} + {self.assists:2} = {self.points:2}"
