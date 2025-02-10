from abc import ABC, abstractmethod

class Fuelable(ABC):
    @abstractmethod
    def refuel(self):
        pass