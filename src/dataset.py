import kaggle
import os
from src.config import DATA_DIR


kaggle.api.authenticate()


def dataset_download():
    try:
        if os.path.exists(DATA_DIR) and os.listdir(DATA_DIR):
            print(f"Data already exists in {DATA_DIR} directory.")
            return
        else:
            print(f"Data does not exist in {DATA_DIR} directory. Downloading...")
            os.makedirs(DATA_DIR, exist_ok=True)

        kaggle.api.dataset_download_files(
            "meowmeowmeowmeowmeow/gtsrb-german-traffic-sign", path=DATA_DIR, unzip=True
        )

        print(f"Data is downloaded in {DATA_DIR}.")
    except Exception as e:
        print(f"An error occurred while downloading the dataset: {e}")
        raise
