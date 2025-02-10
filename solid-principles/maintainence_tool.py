from abc import ABC, abstractmethod
from vehicle import Vehicle

class MaintainenceTool(ABC):

    @abstractmethod
    def perform_maintainence(self, vehicle: Vehicle):
        pass
