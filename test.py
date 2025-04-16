import pandas as pd

df = pd.read_csv("data/weather/initial/GlobalWeatherRepository.csv")

print(df.columns)

print(df.groupby("wind_direction")["wind_direction"].count())
print(df.groupby("wind_direction")["wind_direction"].unique().count())
print(df.groupby("air_quality_us-epa-index")["air_quality_us-epa-index"].count().sum())
print(df.groupby("air_quality_gb-defra-index")["air_quality_gb-defra-index"].count().sum())


from config.config import Config
