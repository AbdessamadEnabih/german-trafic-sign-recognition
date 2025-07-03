# German Traffic Sign Recognition

This project implements a deep learning pipeline for recognizing German traffic signs using the GTSRB dataset.

## Project Structure

```
.
├── data/                        # Dataset directory
│   └── gtsrb-german-traffic-sign/
│       ├── Meta.csv
│       ├── Test.csv
│       ├── Train.csv
│       ├── Meta/
│       ├── Test/
│       └── Train/
├── outputs/                     # Output files (models, logs, etc.)
├── src/                         # Source code
│   ├── config.py                # Configuration (paths, constants)
│   ├── dataset.py               # Dataset download and handling
│   ├── model.py                 # Model definition
│   └── train.py                 # Training script
├── main.py                      # Entry point for running the pipeline
├── .gitignore
└── README.md
```

## Setup

1. **Install dependencies**

   ```sh
   pip install -r requirementsrequirements.txt
   ```

2. **Kaggle API Key**
   Place your `kaggle.json` file in the project root directory.

3. **Download the Dataset**
   Run:
   ```sh
   python main.py
   ```
   This will download and extract the German Traffic Sign dataset into `data/gtsrb-german-traffic-sign`.

## Usage

- To download the dataset, run:
  ```sh
  python main.py
  ```
- Training and model scripts are in `src/model.py` and `src/train.py`.

## File Descriptions

- `src/dataset.py`: Handles dataset download and loading.
- `src/config.py`: Stores configuration variables like data paths.
- `main.py`: Entry point for dataset download and (future) training.

## Notes

- The `data` and `kaggle.json` files are excluded from version control via `.gitignore`.
- You must have a valid Kaggle account and API key to download the dataset.
