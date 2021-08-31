# Python OOP 

## What is Object Oriented Programming?
> Object oriented programing is a paradigm (pattern) of programming design pattern. With object oriented programming, we take the concept of 'objects' and develop our code around accessing and manipulating our object to ultimately perform the output we want in our program.

## Creating a Class
```py
# Creating a class called 'Car'
class Car:
    # __init__ (also called dunder init) should always be the first function you create in a class as it is the function that will initialize our instances of objects with their own attributes
    # self is a keyword in python where you can think of it as if you're looking through the perspective of the instance of the object, you are referencing yourself. That is to say, self as in the english definition, myself.
    def __init__(self):
        self.color = "Blue"
        self.year = 1990
        self.hp = 250

# creating an instance of a Car object and storing it into our dojo_car variable
dojo_car = Car()
```

Now that we created a class, we want to access the information. The way we can access the attributes of a class is by using something we call `dot notation`. 
```py
print(dojo_car.color)
```

If we want to make our Car class more `dynamic`, that is to say, allow for a variance in attributes, we simply need to add parameters to our `__init__` function:
```py
class Car:
    def __init__(self, color, year, hp, miles):
        self.color = color
        self.year = year
        self.hp = hp
        self.miles = miles

dojo_car = Car("Grey", 2021, 300, 0)
```

With classes, we can also set default values to our cars. By setting default values, we can set up our `__init__` function to still run and instantiate an instance of a car without needed all of the arguments to match the parameters:
```py
class Car:
    # setting default values for hp and miles
    def __init__(self, color, year, hp = 150, miles = 0):
        self.color = color
        self.year = year
        self.hp = hp
        self.miles = miles

dojo_car = Car("Black", 2021)
```

## Methods

As I mentioned earlier with OOP, we should also be able to `maniuplate` our data or have our `object` do something. We achieve this feat using functions/methods.

```py
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

print(dojo_car.miles)
dojo_car.drive()
print(dojo_car.miles)
# OUTPUT:
# 0
# DRIVING WEEEEEEEEEEEEEEEE
# 10
```


