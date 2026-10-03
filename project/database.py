from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Settings

DATABASE_URL = Settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()