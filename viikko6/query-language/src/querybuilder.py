from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:

    def __init__(self, matcher = All()):
        self.matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(And(self.matcher, Or(m1, m2)))

    def build(self):
        return self.matcher