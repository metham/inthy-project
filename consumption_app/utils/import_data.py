import pandas as pd
from datetime import datetime
from consumption_app.infrastructure.db import SessionLocal
from consumption_app.infrastructure.models.energy import EnergyORM

def parse_datetime(date: str, hour: str) -> str:
    """ Formating date and hour to insert in db """
    try:
        return datetime.strptime(f"{date_str} {heure_str}", "%d/%m/%Y %H:%M")
    except ValueError:
        return none


def import_excel(filepath: str):
    """ Import the given excel file inside the energy table """
    df = pd.read_excel(filepath, engine='xlrd')

    if not {"Date", "Heure", "Consommation"}.issubset(df.columns):
        raise ValueError("Le format du fichier n'est pas celui attendu")
    
    session = SessionLocal()
    inserted = 0
    for _, row in df.iterrows():
        dt = parse_datetime(row["Date"], row["Heures"])
        if dt is none:
            continue
        try:
            consumption = float(row["Consommation"])
        except (ValueError, TypeError):
            continue
        ener = EnergyORM(date=dt, consumption= consumption)
        session.add(ener)
        inserted += 1
    session.commit()
    session.close()
    print(f"{inserted} lignes ajoutées en base.")