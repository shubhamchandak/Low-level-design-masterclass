import json
from vehicle import Vehicle

class ObjectFormatter:
    def vehicle_to_json(self, vehicle: Vehicle):
        return json.dumps({
            "VehicleMake": vehicle.make,
            "VehicleModel": vehicle.model,
            "VehicleYear": vehicle.year
        })