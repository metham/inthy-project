import pandas as pd
from datetime import datetime
from consumption_app.infrastructure.db import SessionLocal
from consumption_app.infrastructure.models.energy import EnergyORM

def parse_datetime(date: str, hour: str) -> str:
    """ Formating date and hour to insert in db """
    try:
        return datetime.strptime(f"{date} {hour}", "%Y-%m-%d %H:%M")
    except ValueError as e:
        return None

def is_on_the_half_hour(hour: str) -> bool:
    """ This function will serve as a filter to only import data every 30 minutes """
    return hour.endswith(":00") or hour.endswith(":30")


def import_csv(filepath: str):
    """ Import the given excel file inside the energy table """
    df = pd.read_csv(filepath)

    if not {"Date", "Heures", "Consommation"}.issubset(df.columns):
        raise ValueError("Le format du fichier n'est pas celui attendu")

    df = df[df["Heures"].apply(is_on_the_half_hour)]
    
    session = SessionLocal()
    inserted = 0
    now = datetime.now()
    for _, row in df.iterrows():
        dt = parse_datetime(row["Date"], row["Heures"])
        if dt is None or dt > now:
            continue
        try:
            consumption = float(row["Consommation"])
        except (ValueError, TypeError):
            continue
        ener = EnergyORM(date=dt, consumption= consumption)
        session.add(ener)
        inserted += 1
    try:
        session.commit()
    except Exception as err:
        db.session.rollback()
        print(f"{err}")
    finally:
        session.close()
    print(f"{inserted} lignes ajoutées en base.")

if __name__ == "__main__":
    import_csv("/app/data/data.csv")    