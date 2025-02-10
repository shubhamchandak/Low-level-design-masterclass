from maintainence_tool import MaintainenceTool
from vehicle import Vehicle

class BrakeInspectionTool(MaintainenceTool):
    def perform_maintainence(self, vehicle: Vehicle):
        print("Performing brake inspection on {vehicle.make} {vehicle.model}".format(vehicle=vehicle))