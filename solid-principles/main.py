from car import Car
from truck import Truck
from electric_car import ElectricCar
from insurance_calculator import InsuranceCalculator
from object_formatter import ObjectFormatter
from maintenance_service import MaintenanceService
from brake_inspection_tool import BrakeInspectionTool

def main():
    car = Car("Toyota", "Camry", 2018)
    truck = Truck("Ford", "F-150", 1980)
    electric_car = ElectricCar("Tesla", "Model 3", 2021)

    car.refuel()
    truck.refuel()
    electric_car.recharge()
    car.refuel()

    insurance_calculator = InsuranceCalculator()
    formatter = ObjectFormatter()

    print(f"Car Insurance Cost: ${insurance_calculator.calculate_vehicle_insurance(car) + 100}")
    print(f"Truck Insurance Cost: ${insurance_calculator.calculate_vehicle_insurance(truck) + 100}")
    print(f"Vehicle Details in JSON: {formatter.vehicle_to_json(car)}")
    print(f"Vehicle Details in JSON: {formatter.vehicle_to_json(truck)}")
    
    service = MaintenanceService(BrakeInspectionTool())
    service.service_vehicle(car)
    
if __name__ == "__main__":
    main()