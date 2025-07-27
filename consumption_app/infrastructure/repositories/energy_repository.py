from abc import ABC, abstractmethod
from datetime import datetime
from consumption_app.infrastructure.models.energy import Energy

class EnergyRepository(ABC):
    @abstractmethod
    def get_between(self, start: datetime, end: datetime):
        pass
