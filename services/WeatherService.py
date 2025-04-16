from infrastructure.postgres.repositories import WeatherRepository
from models.Weather import Weather

class WeatherService:
    def __init__(self, weatherRep: WeatherRepository):
        self.weatherRep = weatherRep
        
    def get_weather_by_location_and_date(self, location: str, date: str) -> Weather:
        return self.weatherRep.get_by_location_and_date(location, date)