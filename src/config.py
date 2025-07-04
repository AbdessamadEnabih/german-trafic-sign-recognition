import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the data directory and Kaggle credentials
DATA_DIR = os.getenv("DATA_DIR", "data/gtsrb-german-traffic-sign")
DATASET_URL = os.getenv("DATASET_URL", "meowmeowmeowmeowmeow/gtsrb-german-traffic-sign")
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")



