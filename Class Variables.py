# Class Self and class variable

class Player:  # considering this a Player model
    total_players = 0  # this is a class variable | will increament on each object creation

    def __init__(self, points):
        '''
        Self here represents the class object instance
        '''
        self.points = points
        Player.total_players += 1

    def display(self):
        return self.points

    @classmethod
    def display_all(cls):
        return cls.total_players


# Player object
p1 = Player(20)
p2 = Player(10)

print(p1.display())
print(Player.display_all())
