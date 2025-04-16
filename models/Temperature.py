from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from infrastructure.postgres.base.base import Base


class Temperature(Base):
    __tablename__ = "temperature_data"

    id = Column(Integer, primary_key=True)

    temperature_celsius = Column(Float)
    temperature_fahrenheit = Column(Float)

    id_temperature_feels = Column(
        "temperature_feels",
        Integer,
        ForeignKey("temperature_feels_data.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    weather = relationship(
        "Weather", back_populates="temperature", cascade="all, delete-orphan"
    )
    temperature_feels = relationship("TemperatureFeels", back_populates="temperatures")
