import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')
print(df.info())
print("Null values:\n")
print(df.isnull().sum())
print("Duplicated values:\n")
print(df.duplicated().sum())
df = df.dropna(subset=['title', 'type'])

cols_to_fill = ['director', 'cast', 'country', 'rating']
df[cols_to_fill] = df[cols_to_fill].fillna('Unknown')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].fillna('unknown')

dupes = df[df.duplicated(subset=['title', 'type', 'release_year','director','cast','country','date_added','release'], keep=False)]
print(dupes[['title', 'type', 'release_year']])

cols_to_check = [col for col in df.columns if col != 'show_id']
duplicates = df[df.duplicated(subset=cols_to_check, keep=False)]
num_duplicates = df.duplicated(subset=cols_to_check, keep='first').sum()
print("Number of duplicate rows (excluding show_id):", num_duplicates)

df = df.drop_duplicates(subset=cols_to_check, keep='first')
duplicates = df[df.duplicated(subset=cols_to_check, keep=False)]
num_duplicates = df.duplicated(subset=cols_to_check, keep='first').sum()

df[cols_to_check] = df[cols_to_check].apply(lambda x: x.str.strip().str.lower())

df.loc[:, 'country'] = df['country'].fillna('').astype(str).str.split(', ')
df.loc[:, 'listed_in'] = df['listed_in'].fillna('').astype(str).str.split(', ')



df.loc[:, ['duration_num', 'duration_unit']] = df['duration'].str.extract(r'(\d+)\s*(min|Season|Seasons)')
df.loc[:, 'duration_num'] = pd.to_numeric(df['duration_num'])

df = df.copy()
df[['duration_num', 'duration_unit']] = df['duration'].str.extract(r'(\d+)\s*(min|Season|Seasons)')
df['duration_num'] = pd.to_numeric(df['duration_num'])

valid_ratings = ['tv-ma', 'tv-14', 'tv-pg', 'r', 'pg-13', 'tv-y7', 'tv-y', 'pg', 'g', 'nc-17']
df['rating'] = df['rating'].where(df['rating'].isin(valid_ratings), 'Unknown')