from infrastructure.db import SessionLocal
from infrastructure.models.energy import Energy
from datetime import datetime
from infrastructure.repositories.energy_repository import EnergyRepository

class GetConsumptionBetween:
    def __init__(self, repository: EnergyRepository):
        self.repository = repository

    def execute(self, start: datetime, end: datetime):
        if start >= end:
            raise ValueError("start needs to be a more recent date than end")
        
        results = self.repository.get_between(start, end)

        return [
            {
                "datetime": r.date.isoformat(),
                "consumption": r.consumption * 1000000
            } for r in results
        ]