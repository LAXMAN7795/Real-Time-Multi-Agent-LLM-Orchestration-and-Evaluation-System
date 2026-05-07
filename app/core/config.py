from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    GROQ_API_KEY: str
    TAVILY_API_KEY: str

    ENVIRONMENT: str

    class Config:
        env_file = ".env"


settings = Settings()