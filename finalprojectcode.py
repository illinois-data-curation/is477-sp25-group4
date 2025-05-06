# all imports necessary
import os
import pandas as pd
import kagglehub
import zipfile
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns 

# Download Netflix dataset
netflix_path = kagglehub.dataset_download("shivamb/netflix-shows")
netflix_file = os.path.join(netflix_path, "netflix_titles.csv")

# Download IMDB datasets
# after looking at all the files we found these 2 to be the most prevalent
imdb_urls = {
    "basics": "https://datasets.imdbws.com/title.basics.tsv.gz",
    "ratings": "https://datasets.imdbws.com/title.ratings.tsv.gz"
}

os.makedirs("data/imdb", exist_ok=True)
for name, url in imdb_urls.items():
    response = requests.get(url)
    with open(f"data/imdb/{name}.tsv.gz", "wb") as f:
        f.write(response.content)

# Data Cleaning

# Load Netflix
netflix_df = pd.read_csv(netflix_file)

# Load IMDb
basics_df = pd.read_csv("data/imdb/basics.tsv.gz", sep="\t", na_values='\\N')
ratings_df = pd.read_csv("data/imdb/ratings.tsv.gz", sep="\t", na_values='\\N')

# Clean Netflix
# keep only rows with valid title and genre
netflix_df = netflix_df.dropna(subset=["title", "listed_in"])
netflix_df["title_lower"] = netflix_df["title"].str.lower()

# Clean IMDb
# filter to movies and TV shows with ratings
imdb_df = basics_df.merge(ratings_df, on="tconst")
imdb_df = imdb_df[imdb_df["titleType"].isin(["movie", "tvSeries"])]
imdb_df["primaryTitle_lower"] = imdb_df["primaryTitle"].str.lower()

# Merge based on lowercased titles
merged_df = netflix_df.merge(imdb_df, left_on="title_lower", right_on="primaryTitle_lower", how="inner")

#How does the genre distribution on Netflix compare to top-rated IMDB movies?

# Netflix genres
from collections import Counter
netflix_genres = netflix_df["listed_in"].str.split(", ").explode()
netflix_genre_counts = netflix_genres.value_counts()

# IMDb top-rated genre
top_imdb = imdb_df.sort_values(by="averageRating", ascending=False).head(1000)
# (you might need genre column: available in 'genres' column in basics)
imdb_genres = top_imdb["genres"].dropna().str.split(",").explode()
imdb_genre_counts = imdb_genres.value_counts()

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
netflix_genre_counts.head(10).plot(kind="bar", ax=axes[0], title="Top 10 Netflix Genres")
imdb_genre_counts.head(10).plot(kind="bar", ax=axes[1], title="Top 10 IMDB Genres")
plt.tight_layout()
plt.show()

# Do Netflix Originals generally receive higher or lower IMDB ratings compared to non-Netflix content?

# had to do some manual checks to see what would be the best differentiate between a netflix original or not
# Define a 'Netflix Original' as having 'Netflix' in the description
netflix_df["is_original"] = netflix_df["title"].str.contains("netflix", case=False, na=False)
merged_df["is_original"] = merged_df["title"].str.contains("netflix", case=False, na=False)

# Compare ratings
merged_df.groupby("is_original")["averageRating"].mean().plot(kind="bar", title="Avg IMDB Rating: Netflix Original vs Non-Original")
plt.show()

# Are highly-rated IMDB movies and TV shows available on Netflix?
top_rated = imdb_df.sort_values("averageRating", ascending=False).head(500)
top_rated["on_netflix"] = top_rated["primaryTitle_lower"].isin(netflix_df["title_lower"])
percent_available = top_rated["on_netflix"].mean()
print(f"Percentage of Top 500 IMDB titles available on Netflix: {percent_available:.2%}")

# What is the spread of rating based on genre? (including average and any outliers)

# explode genres 
merged_df["genre_list"] = merged_df["listed_in"].str.split(", ")
exploded = merged_df.explode("genre_list")

filtered = exploded[exploded["genre_list"].isin(
    exploded["genre_list"].value_counts()[exploded["genre_list"].value_counts() >= 30].index
)]

# plot 
plt.figure(figsize=(12, 6))
sns.boxplot(data=filtered, x="averageRating", y="genre_list", orient="h")
plt.title("IMDb Ratings by Genre (Boxplot)")
plt.xlabel("IMDb Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
