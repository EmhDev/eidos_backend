import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env si estás en local

class Settings:
    ENV: str = os.getenv("ENV", "local")
    FRONTEND_URL_LOCAL: str = os.getenv("FRONTEND_URL_LOCAL", "http://localhost:5173")
    FRONTEND_URL_PROD: str = os.getenv("FRONTEND_URL_PROD", "https://cleanmind-frontend.onrender.com")

    @property
    def allowed_origins(self):
        if self.ENV == "production":
            return [self.FRONTEND_URL_PROD]
        return [self.FRONTEND_URL_LOCAL]

settings = Settings()
