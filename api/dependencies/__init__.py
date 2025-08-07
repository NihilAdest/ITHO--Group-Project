from sqlalchemy.orm import Session
from api.dependencies.config import SessionLocal

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
