# FinnParser

### Car Information Parser
This repository contains two Python scripts for parsing information about cars from a website and collecting car IDs as links from another website.




### LinkToCarsInfo.py
This script parses information about cars from a website, such as brand, model, year, engine type, and mileage. The script uses the BeautifulSoup library to scrape the website's HTML code and extract the relevant information.

To use this script, you need to provide the URL of the website that contains the car information. The script then goes through each page of the website and extracts the relevant information about each car. The output is saved as a CSV file.

### ParseIDLinks.py
This script collects car IDs as links from a website. The script uses the Requests library to send HTTP requests to the website and the BeautifulSoup library to parse the HTML code and extract the car IDs.

To use this script, you need to provide the URL of the website that contains the car links. The script then goes through each page of the website and extracts the car IDs as links. The output is saved as a text file.

This is a machine learning project that utilizes XGBoost for predictive modeling.

## Project Overview

This project aims to develop a machine learning model using XGBoost for a specific task (provide a brief description of the task, e.g., classification, regression, etc.). The project involves various steps, including data preprocessing, feature engineering, model training, and model evaluation.

## Repository Structure

The repository has the following structure:


```
Project Folder structure at the end of this project
├── data
│   ├── raw_data.csv        # Raw data file (e.g., CSV or Excel)
│   ├── cleaned_data.csv    # Cleaned data file after preprocessing
│   └── feature_engineered_data.csv    # Data file after feature engineering
├── notebooks
│   ├── data_preprocessing.ipynb    # Jupyter notebook for data preprocessing
│   ├── feature_engineering.ipynb    # Jupyter notebook for feature engineering
│   ├── model_training.ipynb         # Jupyter notebook for XGBoost model training
│   └── model_evaluation.ipynb       # Jupyter notebook for model evaluation
├── models
│   └── xgboost_model.pkl    # Serialized trained XGBoost model
├── utils
│   ├── data_preprocessing.py    # Python module for data preprocessing functions
│   ├── feature_engineering.py    # Python module for feature engineering functions
│   └── model_evaluation.py       # Python module for model evaluation functions
├── config.py        # Python module for storing hyperparameter values and other configurations
├── README.md        # Project documentation and instructions
└── requirements.txt # Text file containing the required packages and versions for the project

