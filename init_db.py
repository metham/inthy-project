from consumption_app.infrastructure.db import Base, engine
from consumption_app.infrastructure.models.energy import Energy

print("Creating the model")
Base.metadata.create_all(bind=engine)
print("Model created")