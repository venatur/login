from sqlalchemy import Column, DateTime, String, Boolean, Integer
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    time_created = Column(DateTime)
    time_updated = Column(DateTime)
    active = Column(Boolean)