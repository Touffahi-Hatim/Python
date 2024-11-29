class Car:
    def __init__(self, make, model, year, max_vitesse):
        self.make = make
        self.model = model
        self.year = year
        self.max_vitesse = max_vitesse
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def get_vitesse(self):
        max_vitesse=f"{self.max_vitesse}"
        return max_vitesse
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Create a Car object
my_car = Car('audi', 'a4', 2022, 290)

# Access attributes and call methods
print(my_car.get_descriptive_name())
print(f"max vitesse is {my_car.get_vitesse()} km/h")
my_car.read_odometer()


# Update odometer reading
my_car.update_odometer(int(input("enter your odometer value now :")))
my_car.read_odometer()

# Increment odometer reading
my_car.increment_odometer(100)
my_car.read_odometer()

#niiiice