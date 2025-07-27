from sqlalchemy import Column, Integer, DateTime
from consumption_app.infrastructure.db import Base

class Energy(Base):
    __tablename__ = "energy"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False, index=True)
    consumption = Column(Integer, nullable=False)
