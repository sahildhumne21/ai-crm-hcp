from database import SessionLocal
from models import Interaction

def log_interaction(data):
    db = SessionLocal()

    interaction = Interaction(
        hcp_name=data.get("hcp_name"),
        interaction_type=data.get("interaction_type"),
        topics=data.get("topics"),
        sentiment=data.get("sentiment"),
        outcome=data.get("outcome"),
        follow_up=data.get("follow_up")
    )

    db.add(interaction)
    db.commit()

    return {"message": "Interaction logged successfully"}