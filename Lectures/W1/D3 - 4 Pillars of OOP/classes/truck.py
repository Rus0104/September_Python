from classes.cars import Car

class Truck(Car):
    def __init__(self, color, year, can_tow, hp = 150, miles = 0):
        super().__init__(color, year, hp, miles)
        self.can_tow = can_tow
    
    def drive(self):
        self.miles += 20


