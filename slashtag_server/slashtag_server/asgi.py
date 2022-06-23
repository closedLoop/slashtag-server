import logging

from .config import load_config
from .main import get_app

# Load Environental Variables
load_config()

# logging
logging.basicConfig(level=logging.DEBUG)

# Create the FastAPI application
app = get_app()
