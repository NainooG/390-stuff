class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Driving 30 mph")

    def what(self):
        print("brand: {}, model: {}", self.brand, self.model)
            
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sailing 30 knots")

    def what(self):
        print("brand: {}, model: {}", self.brand, self.model)

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flying 30 mph")

    def what(self):
        print("brand: {}, model: {}", self.brand, self.model)
    
car = Car("Ford", "Mustang")
car.move()

boat = Boat("Ibiza", "Touring 20")
boat.move()

plane = Plane("Boeing", "747")
plane.move()