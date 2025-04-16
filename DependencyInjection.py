from sqlalchemy.orm import Session
from infrastructure.postgres.base.base import engine
from infrastructure.postgres.repositories.WeatherRepository import WeatherRepository
from infrastructure.postgres.repositories.LocationRepository import LocationRepository
from services.WeatherService import WeatherService
from services.LocationService import LocationService
from scripts.WeatherCLI import WeatherCLI

def create_cli():
    with Session(engine) as session:
        weather_repository = WeatherRepository(session)
        location_repository = LocationRepository(session)

        weather_service = WeatherService(weather_repository)
        location_service = LocationService(location_repository)

        return WeatherCLI(weather_service, location_service)