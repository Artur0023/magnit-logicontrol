from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / 'data' / 'logistics.db'

engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()