class Car:
    car_brand = "Ford"
    def __init__(self, color, year, hp = 150, miles = 0):
        self.color = color
        self.year = year
        self.hp = hp
        self.miles = miles
        
    
    def drive(self):
        print("DRIVING WEEEEEEEEEEEEEEEE")
        self.miles += 10
    
    def crash(self, other_car):
        print(f"Just crashed into a car with the color {other_car.color}")


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.car = Car("Pink", 2011)

guido = Owner("guido", 21)
guido.car.drive()








