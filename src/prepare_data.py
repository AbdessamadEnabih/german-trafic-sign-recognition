import os
from config import DATA_DIR
from kaggle import api

if not os.environ["KAGGLE_USERNAME"] or not os.environ["KAGGLE_KEY"]:
    raise EnvironmentError(
        "KAGGLE_USERNAME and KAGGLE_KEY must be set in the environment variables."
    )

os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

print("Authenticating with Kaggle...")

api.authenticate()

def dataset_download():
    try:
        if os.path.exists(DATA_DIR) and os.listdir(DATA_DIR):
            print(f"Data already exists in {DATA_DIR} directory.")
            return
        else:
            print(f"Data does not exist in {DATA_DIR} directory. Downloading...")
            os.makedirs(DATA_DIR, exist_ok=True)

        api.dataset_download_files(
            "meowmeowmeowmeowmeow/gtsrb-german-traffic-sign", path=DATA_DIR, unzip=True
        )

        print(f"Data is downloaded in {DATA_DIR}.")
    except Exception as e:
        print(f"An error occurred while downloading the dataset: {e}")
        raise


if __name__ == "__main__":
    print("Starting dataset download script...")
    dataset_download()
    print("Dataset download script executed successfully.")
