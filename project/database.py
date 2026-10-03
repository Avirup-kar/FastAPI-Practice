from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://neondb_owner:npg_i6amOTbMWw3p@ep-super-leaf-azuu82sw-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()