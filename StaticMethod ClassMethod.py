class Circle:
    no_of_circles=0
    
    def __init__(self, radius):
        self.radius=radius
        Circle.no_of_circles+=1
        
    @staticmethod
    def square(num):
        return num**2
    
    @classmethod
    def getCircleCount(cls):
        return cls.no_of_circles
    
    def area(self):
        return round(3.14*self.square(self.radius),2)