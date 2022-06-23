import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create new engine instance
engine = create_engine(os.environ["SQLALCHEMY_DATABASE_URL"])

# create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
