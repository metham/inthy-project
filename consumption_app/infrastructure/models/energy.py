from sqlalchemy import Column, Integer, DateTime
from infrastructure.db import Base

class EnergyORM(Base):
    __tablename__ = "energy"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False, index=True)
    consumption = Column(Integer, nullable=False)
