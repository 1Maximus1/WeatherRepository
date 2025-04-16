from sqlalchemy import Column, Integer, Float, String, DateTime, Time, ForeignKey
from infrastructure.postgres.base.base import Base
from sqlalchemy.orm import relationship

class Location(Base):
    __tablename__ = 'locations_data'
    
    id = Column(Integer, primary_key=True)
    country = Column(String(100), nullable=False)
    location_name = Column(String(100), nullable=False)
    timezone = Column(String(100), nullable=False)
    latitude = Column(Float)   
    longitude = Column(Float)
    
    weather = relationship("Weather", back_populates="location", cascade="all, delete-orphan")
    
    