from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:123localhost:5432/mydatabase"
engine=create_engine()
SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)