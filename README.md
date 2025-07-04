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
│   ├── prepare_data.py          # Dataset download and handling
│   ├── model.py                 # Model definition
│   └── train.py                 # Training script
├── main.py                      # Entry point for running the pipeline
├── Makefile                     # Project automation commands
├── .gitignore
└── README.md
```

## Setup

All setup and usage must be done via the provided Makefile.

1. **Install dependencies and download the dataset**

   ```sh
   make init
   ```

   This will install all dependencies and download/extract the German Traffic Sign dataset into `data/gtsrb-german-traffic-sign`.

2. **Kaggle API Key and Environment Variables**

   - Copy `.env.example` to `.env` and fill in your Kaggle credentials.

## Usage

Available Makefile commands:

| Command          | Description                                               |
| ---------------- | --------------------------------------------------------- |
| `make init`      | Install dependencies and download the dataset             |
| `make init-venv` | Initialize a virtual environment and install dependencies |

Example usage:

- To set up everything (dependencies and data) in one step:
  ```sh
  make init
  ```
- To initialize a virtual environment and install dependencies:

  ```sh
  make init-venv
  ```

- Training and model scripts are in `src/model.py` and `src/train.py`.

## File Descriptions

- `src/prepare_data.py`: Handles dataset download and extraction.
- `src/config.py`: Stores configuration variables like data paths and loads environment variables.
- `main.py`: Entry point for dataset download and (future) training.

## Notes

- The `data` directory is excluded from version control via `.gitignore`.
- You must have a valid Kaggle account and API key to download the dataset.
- Use the provided `.env.example` as a template for your `.env` file.
- The `data` directory is excluded from version control via `.gitignore`.
- You must have a valid Kaggle account and API key to download the dataset.
- Use the provided `.env.example` as a template for your `.env` file.

## Notes

- The `data` and `kaggle.json` files are excluded from version control via `.gitignore`.
- You must have a valid Kaggle account and API key to download the dataset.
- Use the provided `.env.example` as a template for your `.env` file.
