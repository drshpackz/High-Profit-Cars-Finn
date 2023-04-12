@echo off
echo Creating Project Folder...
mkdir Project_Folder

echo Creating data Folder...
mkdir Project_Folder\data

echo Creating notebooks Folder...
mkdir Project_Folder\notebooks

echo Creating models Folder...
mkdir Project_Folder\models

echo Creating utils Folder...
mkdir Project_Folder\utils

echo Creating Project Files...
cd Project_Folder
echo. > data\raw_data.csv
echo. > data\cleaned_data.csv
echo. > data\feature_engineered_data.csv
echo. > notebooks\data_preprocessing.ipynb
echo. > notebooks\feature_engineering.ipynb
echo. > notebooks\model_training.ipynb
echo. > notebooks\model_evaluation.ipynb
echo. > models\xgboost_model.pkl
echo. > utils\data_preprocessing.py
echo. > utils\feature_engineering.py
echo. > utils\model_evaluation.py
echo. > config.py
echo. > README.md
echo. > requirements.txt

echo Project Directory and Files Created Successfully!
