from .config import load_config
from .main import get_app

# Load Environental Variables
load_config()

# Create the FastAPI application
app = get_app()
