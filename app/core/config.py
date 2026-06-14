from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int  

    class Config:
        env_file = ".env",
        extra = "ignore"
    
settings = Settings()