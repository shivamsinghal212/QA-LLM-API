from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "LLM-API"
    PROJECT_DESCRIPTION: str = "APIs for LLM QA"
    PROJECT_VERSION: str = "0.0.1"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
