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

    @classmethod  # this will enable the method to receive cls as first agruement rather than self
    def display_all(cls):
        return cls.total_players

    @staticmethod  # static method does not take cls or self as first arguement
    # this is useful if class method or object method does not fit the match
    def display_points(*agrs):
        return f"Just Printing {agrs}"


# Player object
p1 = Player(20)
p2 = Player(10)

print('Class Method via Class: ', Player.display_all())
# One can also access class method via objects
print('Class Method via object: ', p1.display_all())
# Also objects can also access class variable
print('Accessed via Objects: ', p1.total_players)

# Also any additional attribute same name to class variable shall be created separetly
# Look attribute lookup:  -->class object-->class-->base class
p1.total_players = 10
print('Total Players via P1: ', p1.total_players)

print('Total Players via Class: ', Player.total_players)

# Example of just static method
print(p1.display_points(15))
