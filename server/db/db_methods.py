from .db_model import Stats
from .db_connection import session

def insert_to_table(info:Stats):
    try:
        existing_user = (
            session.query(Stats).filter(Stats.ip == info.ip).first()
        )
        if existing_user is None:
            session.add(info)
            session.commit()
            print(f"Created new record for {info.ip}")
        else:
            print("Already inserted.")
    except Exception as e:
        print(e)