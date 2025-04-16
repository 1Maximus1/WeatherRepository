from infrastructure.postgres.repositories import LocationRepository
from models.Location import Location

class LocationService:
    def __init__(self, locationRep: LocationRepository):
        self.locationRep = locationRep
        
    def get_location_by_country(self, country: str) -> Location:
        return self.locationRep.get_by_country(country)