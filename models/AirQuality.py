from sqlalchemy import Column, Integer, Float, String, DateTime, Time, ForeignKey
from infrastructure.postgres.base.base import Base
from sqlalchemy.orm import relationship

class AirQuality(Base):
    __tablename__ = 'air_quality_data'
    
    id = Column(Integer, primary_key=True)
    
    pressure_mb = Column(Float)
    visibility_km = Column(Float)
    uv_index = Column(Float)
    # Great Britain measuring
    air_quality_gb = Column(Float)
    
    weather = relationship("Weather", back_populates="air_quality", cascade="all, delete-orphan")
