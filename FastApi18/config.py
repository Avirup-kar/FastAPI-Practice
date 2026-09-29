import os 
from dotenv import load_dotenv

class Settings:
    origin = os.getenv("ORIGIN")
    

settings = Settings()    