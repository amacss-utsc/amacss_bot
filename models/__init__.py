from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .economy import EconomyPlayer, Inventory
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()