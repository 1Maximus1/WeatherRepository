from sqlalchemy.orm import Session
from models.Weather import Weather

class WeatherRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, weather: Weather) -> Weather:
        self.db.add(weather)
        self.db.commit()
        self.db.refresh(weather)
        return weather

    def get_by_id(self, weather_id: int) -> Weather:
        return self.db.query(Weather).filter(Weather.id == weather_id).first()

    def get_by_location_and_date(self, location: str, date: str) -> Weather:
        return self.db.query(Weather).filter(
                Weather.location_id == location.id,
                Weather.last_updated >= date,
                Weather.last_updated < date.replace(day=date.day+1)
                )
    
    def update(self, weather: Weather) -> Weather:
        self.db.commit()
        self.db.refresh(weather)
        return weather

    def delete(self, weather_id: int) -> None:
        weather = self.db.query(Weather).filter(Weather.id == weather_id).first()
        if weather:
            self.db.delete(weather)
            self.db.commit()