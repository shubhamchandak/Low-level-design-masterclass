from vehicle import Vehicle
from fuelable import Fuelable

class Car(Vehicle, Fuelable):
    def calculate_insurance_cost(self):
        age = 2024 - self.year
        return 1000 if age > 5 else 500
    
    def refuel(self):
        print("Refueling car with petrol")
