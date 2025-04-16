import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from services.WeatherService import WeatherService 
from services.LocationService import LocationService 

class WeatherCLI: 
    def __init__(self, WeatherService: WeatherService, LocationService: LocationService):
        self.weatherService = WeatherService
        self.locationService = LocationService

    def search_weather(self): 
        """Консольний пошук погоди за країною та датою"""
        print("\n=== Пошук погодних даних ===")
        
        # Введення параметрів
        country = input("Введіть країну: ").strip()
        date_str = input("Введіть дату (рррр-мм-дд): ").strip()
        
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Невірний формат дати. Використовуйте рррр-мм-дд")
            return
        
        locations = self.locationService.get_location_by_country(country)

        found_any = False

        for location in locations:
            weather = self.weatherService.get_weather_by_location_and_date(location, date).first()

            if weather:
                found_any = True
                print(f"\nЛокація: {location.location_name}, {location.country}")
                print(f"Дата: {weather.last_updated}")
                print(f"Температура: {weather.temperature.temperature_celsius}°C")
                print(f"Вологість: {weather.precipitation.humidity}%")
                print(f"Швидкість вітру: {weather.wind.wind_kph} км/год")
                print(f"Схід сонця: {weather.celestial.sunrise}")
                # Additional parameters ...

        if not found_any:
            print(f"\nДані за {date_str} відсутні")

if __name__ == "__main__":
    while True:
        from DependencyInjection import create_cli
        weatherCLI = create_cli()
        weatherCLI.search_weather()
        if input("\nПродовжити пошук? (так/ні): ").lower() != 'так':
            break