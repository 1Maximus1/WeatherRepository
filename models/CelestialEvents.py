from sqlalchemy import Column, Integer, Float, String, DateTime, Time, ForeignKey,Boolean
from infrastructure.postgres.base.base import Base
from sqlalchemy.orm import relationship

class CelestialEvents(Base):
    __tablename__ = 'celestial_events_data'
    
    id = Column(Integer, primary_key=True)
    
    sunrise = Column(Time)
    sunset = Column(Time)
    moonrise = Column(Time)
    moonset = Column(Time)
    moon_phase = Column(String(50))
    moon_illumination = Column(Float)
    
    weather = relationship("Weather", back_populates="celestial", cascade="all, delete-orphan")
