# Data_Cleaning

## Task
This project demonstrates data cleaning and preprocessing on the [Netflix Movies and TV Shows dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) from Kaggle. The goal was to prepare the raw data for analysis by handling missing values, duplicates, inconsistent formats, and standardizing columns.

Dataset Source: [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

## Tools Used
- Python
- Pandas

## Files
- `netflix_titles.csv`: Original dataset from Kaggle.
- `cleaned_netflix_data.csv`: Cleaned dataset after preprocessing.
- `data_cleaning.py`: Python script used for all cleaning steps.
- `cleaned_data.csv`: to show difference of saving with encoding on python script

## Screenshots
Original data:

![image](https://github.com/user-attachments/assets/77c6a660-d132-49e8-8425-a15b8bf084e9)

Extracting info of the file -

![image](https://github.com/user-attachments/assets/744766a6-1a1f-4b44-a71b-bfa3ea3ec969)

Evaluating null values in the dataset-

![image](https://github.com/user-attachments/assets/1206e87a-d09a-45ed-a1f0-9a04aa56b60d)

Overall duplicate values-

![image](https://github.com/user-attachments/assets/233ac79c-df3b-4e5a-9763-2d7ff4292f98)

But since show_id is unique for all, checking for all other columns-

![image](https://github.com/user-attachments/assets/37d4ddab-b400-4893-9515-dbb83667b9fe)
![Screenshot 2025-04-22 102150](https://github.com/user-attachments/assets/f9c6b400-7b66-4dba-92e4-5250c148dadd)

Output to cleaned data still had garbage encoded characters as seen below:
![image](https://github.com/user-attachments/assets/84e3edb0-07a7-4ddf-a8e7-8a2efa0db746)

Thus using: encoding='utf-8-sig' and saving it to cleaned_netflix_data.csv
![image](https://github.com/user-attachments/assets/2075efaa-6c1e-4d64-af4a-1846c1363f2c)

## Credits

- [Netflix Movies and TV Shows Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Data cleaning performed by Tanisha Pahwa









