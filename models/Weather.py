from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Time,
)
from sqlalchemy.orm import relationship

from infrastructure.postgres.base.base import Base


class Weather(Base):
    __tablename__ = 'weather_data'
    
    id = Column(Integer, primary_key=True)
    
    location_id = Column(Integer, ForeignKey('locations_data.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    celestial_id = Column(Integer, ForeignKey('celestial_events_data.id', ondelete='CASCADE', onupdate='CASCADE'))
    air_quality_id = Column(Integer, ForeignKey('air_quality_data.id', ondelete='CASCADE', onupdate='CASCADE'))
    precipitation_id = Column(Integer, ForeignKey('precipitation_data.id', ondelete='CASCADE', onupdate='CASCADE'))
    wind_id = Column(Integer, ForeignKey('wind_data.id', ondelete='CASCADE', onupdate='CASCADE'))
    temperature_id = Column(Integer, ForeignKey('temperature_data.id', ondelete='CASCADE', onupdate='CASCADE'))

    last_updated = Column(DateTime, nullable=False, index=True)

    #Task
    should_go_out = Column(Boolean)
    
    # Relations
    location = relationship("Location", back_populates="weather")
    celestial = relationship("CelestialEvents", back_populates="weather")
    wind = relationship("Wind", back_populates="weather")
    precipitation = relationship("Precipitation", back_populates="weather")
    air_quality = relationship("AirQuality", back_populates="weather")
    temperature = relationship("Temperature", back_populates="weather")
