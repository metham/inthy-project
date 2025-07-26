from infrastructure.db import SessionLocal
from infrastructure.models.energy import EnergyORM

def get_consumption_between(start: str, end: str):
    """ Returns the consumption of energy in What between start and end 30 minutes by 30 minutes """
    session = SessionLocal()
    try: 
        rows = session.query(EnergyORM).filter(
            EnergyORM.date >= start,
            EnergyORM.date <= end
        ).order_by(EnergyORM.date).all()
        return [
            {
                "datetime": r.date.isoformat(),
                "consumption": r.consumption * 1000000
            } for r in rows
        ]
    finally:
        session.close()