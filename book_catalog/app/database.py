from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://cj_sit722_cg57_user:bTMfuBFEGqO4noI36IaKxacXRa6J25lB@dpg-crrl9h56l47c73cktv3g-a.oregon-postgres.render.com/cj_sit722_cg57"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
