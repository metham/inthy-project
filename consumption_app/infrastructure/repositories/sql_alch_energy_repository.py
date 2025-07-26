from abc import ABC, abstractmethod
from datetime import datetime
from ..models.energy import Energy
from ..repositories.energy_repository import EnergyRepository
from ..db import SessionLocal

class SqlAlchemyEnergyRepository(EnergyRepository):
    def __init__(self):
        self.session = SessionLocal()

    def get_between(self, start: datetime, end: datetime):
        try: 
            return self.session.query(Energy).filter(
                Energy.date >= start,
                Energy.date <= end
            ).order_by(Energy.date).all()
        finally:
            self.session.close()
