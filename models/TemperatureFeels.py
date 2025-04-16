from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from infrastructure.postgres.base.base import Base


class TemperatureFeels(Base):
    __tablename__ = "temperature_feels_data"

    id = Column(Integer, primary_key=True)

    temperature_celsius_feels = Column(Float)
    temperature_fahrenheit_feels = Column(Float)

    temperatures = relationship("Temperature", back_populates="temperature_feels",cascade="all, delete-orphan")

