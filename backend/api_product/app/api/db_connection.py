from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import  sessionmaker
import os

# DB_NAME =  os.environ['DB_NAME']
# DB_USER = os.environ['DB_USER']
# DB_PW = os.environ['DB_PASS']

#DATABASE_URL = 
#DATABASE_URL_LOCAL = "mysql+mysqlconnector://root:@localhost:3306/panda"
DB_URL = os.getenv("DB_URL")
Engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
    
Base = declarative_base()