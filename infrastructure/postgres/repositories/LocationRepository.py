from sqlalchemy.orm import Session
from models.Location import Location

class LocationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, location: Location) -> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location

    def get_by_id(self, location_id: int) -> Location:
        return self.db.query(Location).filter(Location.id == location_id).first()
    
    def get_by_country(self, country: str) -> Location:
        return self.db.query(Location).filter(Location.country == country)
    
    def update(self, location: Location) -> Location:
        self.db.commit()
        self.db.refresh(location)
        return location

    def delete(self, location_id: int) -> None:
        location = self.db.query(Location).filter(Location.id == location_id).first()
        if location:
            self.db.delete(location)
            self.db.commit()