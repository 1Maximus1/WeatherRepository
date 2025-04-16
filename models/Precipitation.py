from sqlalchemy import Column, Integer, Float, String, DateTime, Time, ForeignKey
from infrastructure.postgres.base.base import Base
from sqlalchemy.orm import relationship

class Precipitation(Base):
    __tablename__ = 'precipitation_data'
    
    id = Column(Integer, primary_key=True)
    
    precip_mm = Column(Float)
    humidity = Column(Integer)
    cloud = Column(Integer)
    
    weather = relationship("Weather", back_populates="precipitation", cascade="all, delete-orphan")