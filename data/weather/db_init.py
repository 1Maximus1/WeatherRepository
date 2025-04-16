from sqlalchemy import inspect
from models.Location import Location
from data.weather.GlobalWeatherInitial import import_from_csv 

# def is_database_empty():
#     inspector = inspect(engine)
#     tables = inspector.get_table_names()
    
#     if not tables:
#         return True
    
#     with SessionLocal() as session:
#         return session.query(Location).count() == 0

def is_database_empty(engine, SessionLocal):
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(tables)
    if not tables:
        return True
    
    with SessionLocal() as session:
        return session.query(Location).count() == 0

def initialize_data(SessionLocal, csv_path="data/weather/initial/GlobalWeatherRepository.csv"):
    engine = SessionLocal.kw["bind"]
    db_type = 'mysql' if 'mysql' in engine.url.drivername else 'postgres'
    
    print(f"Current connection: {engine.url}")
    print(f"Database type: {db_type}")
    
    if is_database_empty(engine, SessionLocal):
        print(f"Database ({db_type}) is empty. Let's start importing...")
        import_from_csv(csv_path, SessionLocal)
        print("Data import completed successfully!")
    else:
        print(f"Database ({db_type}) already contains data. No import required.")

