from maintainence_tool import MaintainenceTool
from vehicle import Vehicle

class MaintenanceService:
    def __init__(self, tool: MaintainenceTool):
        self.tool = tool

    def service_vehicle(self, vehicle: Vehicle):
        self.tool.perform_maintainence(vehicle)