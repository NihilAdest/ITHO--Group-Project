from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class conf:
    db_host = "localhost"
    db_name = "sandwich_maker_api"
    db_port = 3306
    db_user = "root"
    db_password = "Breego9419088!"
    app_host = "localhost"
    app_port = 8000

# MySQL database URL format:
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{conf.db_user}:{conf.db_password}"
    f"@{conf.db_host}:{conf.db_port}/{conf.db_name}"
)

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base
Base = declarative_base()
