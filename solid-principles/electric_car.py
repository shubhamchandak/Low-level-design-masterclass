from vehicle import Vehicle
from rechargeable import Rechargeable

class ElectricCar(Vehicle, Rechargeable):

    def calculate_insurance_cost(self):
        age = 2024 - self.year
        return 2000 if age > 5 else 1000
    
    def recharge(self):
        print("Recharging electric car")