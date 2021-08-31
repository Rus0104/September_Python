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

dojo_car = Car("Grey", 2021, 300)
ninja_car = Car("Black", 2009, 700)
student_car = Car("White", 2020)

print("DOJOCAR:")
print(dojo_car.color)
print(dojo_car.hp)
print(dojo_car.miles)
dojo_car.drive()
print(dojo_car.miles)

# if we want to access all of our attributes and see it in dictionary form:
print(dojo_car.__dict__)
# now that it is in dictionary form, we can use a for-loop to loop through all the key-value pairs in our object
for key, val in dojo_car.__dict__.items():
    print(f'{key} : {val}')

print("NINJACAR:")
print(ninja_car.color)

print("STUDENTCAR:")
print(student_car.hp)