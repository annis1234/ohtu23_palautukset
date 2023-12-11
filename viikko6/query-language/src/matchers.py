class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:

    def test(self, player):
        return True
    
class Not:

    def __init__(self, condition):
        self._condition = condition
    
    def test (self, player):
        return self._condition.test(player) == False
    
class HasFewerThan:

    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value <= self._value
    
class Or:

    def __init__(self, *conditions):
        self._conditions = conditions

    def test(self, player):
        for condition in self._conditions:
            if condition.test(player) == True:
                return True
            
        return False