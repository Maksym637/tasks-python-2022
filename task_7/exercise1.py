class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return "The car brand is {} and it moves at a speed {} kph | mph.".format(self.brand, self.speed)

    @classmethod
    def mph(cls, brand, kph):
        mph = round(kph * 0.621)
        return cls(brand, mph)
    
    @staticmethod
    def isFast(speed):
        if speed > 80:
            return True
        else:
            return False


car1 = Car("Toyota", 30)
print(car1)

print(Car.mph("Renault", 51))

print(Car.isFast(70))