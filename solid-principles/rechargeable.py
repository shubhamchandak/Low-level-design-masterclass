from abc import ABC, abstractmethod

class Rechargeable(ABC):
    @abstractmethod
    def recharge(self):
        pass