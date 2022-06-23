from pathlib import Path

from dotenv import load_dotenv


def load_config():
    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)
