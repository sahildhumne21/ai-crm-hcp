from database import SessionLocal
from models import Interaction

def edit_interaction(interaction_id, new_data):
    db = SessionLocal()

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return {"error": "Interaction not found"}

    for key, value in new_data.items():
        setattr(interaction, key, value)

    db.commit()

    return {"message": "Interaction updated"}