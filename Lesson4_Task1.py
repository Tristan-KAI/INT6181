class Car:
    def __init__(self, license, speed):
        self.license = license
        self.speed = speed

    def accelerate(self, spd):
        self.speed += spd

    def brake(self):
        self.speed -= 10


class Tesla(Car):
    def accelerate(self, spd):
        if spd == 0:
            self.brake()
        else:
            super().accelerate(spd)

    def brake(self):
        super().brake()


car = Car("AB1234", 30)
car.accelerate(5)
car.brake()
print(f"Car speed: {car.speed} km/h")


tesla = Tesla("TESLA01", 30)
tesla.accelerate(5)
tesla.brake()
print(f"Tesla speed: {tesla.speed} km/h")