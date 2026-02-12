import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df.drop_duplicates(inplace=True)

text_columns = df.select_dtypes(include='object').columns
df[text_columns] = df[text_columns].fillna("Unknown")

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['type'] = df['type'].str.lower()
df['country'] = df['country'].str.lower()

df.columns = df.columns.str.lower().str.replace(" ", "_")

df.to_csv("cleaned_netflix.csv", index=False)

print("Cleaning complete.")
