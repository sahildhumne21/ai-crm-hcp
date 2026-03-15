from database import SessionLocal
from models import Interaction

def get_history(hcp_name):
    db = SessionLocal()

    interactions = db.query(Interaction).filter(
        Interaction.hcp_name == hcp_name
    ).all()

    return interactions