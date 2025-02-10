from vehicle import Vehicle
from fuelable import Fuelable

class Truck(Vehicle, Fuelable):
    def calculate_insurance_cost(self):
        age = 2024 - self.year
        return 1500 if age > 8 else 700
    
    def refuel(self):
        print("Refueling truck with diesel")