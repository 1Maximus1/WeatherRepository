import yaml

class Config:
    
    def get_config_postgres() -> str:
        CONFIG = Config.__load_config()
        DB_CONFIG = CONFIG["postgres"]
        
        return f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
        
    def get_config_mysql() -> str:
        CONFIG = Config.__load_config()
        DB_CONFIG = CONFIG["mysql"]
        
        return f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
            
    def __load_config():
        with open("application.yml", "r") as file:
            return yaml.safe_load(file)

    def get_kagle_repo() -> str:
        return "nelgiriyewithana/global-weather-repository"