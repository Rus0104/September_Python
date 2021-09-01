from classes.cars import Car

class Sedan(Car):
    def __init__(self, color, year, hp = 150, miles = 0):
        super().__init__(color, year, hp = 150, miles = 0)