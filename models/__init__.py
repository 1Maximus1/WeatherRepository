# models/__init__.py
from .AirQuality import AirQuality
from .CelestialEvents import CelestialEvents
from .Location import Location
from .Precipitation import Precipitation
from .Temperature import Temperature
from .TemperatureFeels import TemperatureFeels
from .Weather import Weather
from .Wind import Wind

__all__ = [
    "Location",
    "CelestialEvents",
    "Weather",
    "Temperature",
    "Precipitation",
    "Wind",
    "AirQuality",
    "TemperatureFeels"
]
