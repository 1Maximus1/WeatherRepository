from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship

from infrastructure.postgres.base.base import Base
from models.enums.WindDirection import WindDirection


class Wind(Base):
    __tablename__ = "wind_data"

    id = Column(Integer, primary_key=True)

    wind_kph = Column(Float)
    wind_degree = Column(Integer)
    wind_direction = Column(Enum(WindDirection))
    # wind_direction = Column(Enum(WindDirection, values_callable=lambda x: [e.value for e in x]))

    weather = relationship(
        "Weather", back_populates="wind", cascade="all, delete-orphan"
    )
