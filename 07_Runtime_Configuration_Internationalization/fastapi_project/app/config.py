import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Application")
    APP_DEBUG: str = os.getenv("APP_DEBUG", "false").lower() == "true"
    
