# import_data.py
from datetime import datetime

import pandas as pd

from models.AirQuality import AirQuality
from models.CelestialEvents import CelestialEvents
from models.Location import Location
from models.Precipitation import Precipitation
from models.Temperature import Temperature
from models.Weather import Weather
from models.Wind import Wind


def parse_time(time_str):
    try:
        return datetime.strptime(time_str, "%I:%M %p").time()
    except:
        return None


def import_from_csv(csv_path, session):
    try:
        df = pd.read_csv(csv_path)
        session = session()
        
        for _, row in df.iterrows():
            try:
                # Location
                location = Location(
                    country=row["country"],
                    location_name=row["location_name"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                    timezone=row["timezone"],
                )
                session.add(location)

                # CelestialEvents
                celestial = CelestialEvents(
                    sunrise=parse_time(row["sunrise"]),
                    sunset=parse_time(row["sunset"]),
                    moonrise=parse_time(row["moonrise"]),
                    moonset=parse_time(row["moonset"]),
                    moon_phase=row["moon_phase"],
                    moon_illumination=row["moon_illumination"],
                )
                session.add(celestial)

                # Wind
                wind = Wind(
                    wind_kph=row["wind_kph"],
                    wind_degree=row["wind_degree"],
                    wind_direction=row["wind_direction"],
                )
                session.add(wind)

                # Temperature
                temperature = Temperature(
                    temperature_celsius=row["temperature_celsius"],
                    temperature_fahrenheit=row["temperature_fahrenheit"],
                )
                session.add(temperature)

                # Precipitation
                precipitation = Precipitation(
                    precip_mm=row["precip_mm"],
                    humidity=row["humidity"],
                    cloud=row["cloud"],
                )
                session.add(precipitation)

                # AirQuality
                air_quality = AirQuality(
                    pressure_mb=row["pressure_mb"],
                    visibility_km=row["visibility_km"],
                    uv_index=row["uv_index"],
                    air_quality_gb=row.get("air_quality_gb-defra-index", 0),
                )
                session.add(air_quality)

                session.flush()

                # Weather
                weather = Weather(
                    location_id=location.id,
                    celestial_id=celestial.id,
                    wind_id=wind.id,
                    temperature_id=temperature.id,
                    precipitation_id=precipitation.id,
                    air_quality_id=air_quality.id,
                    last_updated=datetime.strptime(
                        row["last_updated"], "%Y-%m-%d %H:%M"
                    ),
                    should_go_out=True if row["uv_index"] < 5 else False,
                )
                session.add(weather)

                
                if _ % 1000 == 0:
                    session.commit()
                    if _ != 0:
                        break

            except Exception as e:
                print(f"Error in row {_}: {e}")
                session.rollback()

        session.commit()
    finally:
        print("Ended....")
