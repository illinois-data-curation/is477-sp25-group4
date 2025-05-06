import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# go to this website - https://datasets.imdbws.com/  - and download files title.basics.tsv.gz and title.ratings.tsv.gz 

# Ensure output folder exists
os.makedirs("results", exist_ok=True)

# Load Data 
netflix_file = "finalproject/data/netflix/netflix_titles.csv"
basics_file = "finalproject/data/imdb/title.basics.tsv"
ratings_file = "finalproject/data/imdb/title.ratings.tsv"

# assertion check
#assert os.path.exists(netflix_file), "Netflix file missing"
#assert os.path.exists(basics_file), "IMDb basics file missing"
#assert os.path.exists(ratings_file), "IMDb ratings file missing"

# Read Data
netflix_df = pd.read_csv(netflix_file)
netflix_df = netflix_df.dropna(subset=["title", "listed_in"])
netflix_df["title_lower"] = netflix_df["title"].str.lower()

basics_df = pd.read_csv(basics_file, sep="\t", na_values='\\N')
ratings_df = pd.read_csv(ratings_file, sep="\t", na_values='\\N')

imdb_df = basics_df.merge(ratings_df, on="tconst")
imdb_df = imdb_df[imdb_df["titleType"].isin(["movie", "tvSeries"])]
imdb_df["primaryTitle_lower"] = imdb_df["primaryTitle"].str.lower()

merged_df = netflix_df.merge(imdb_df, left_on="title_lower", right_on="primaryTitle_lower", how="inner")

# Genre Distribution Comparison question 1
netflix_genres = netflix_df["listed_in"].str.split(", ").explode()
netflix_genre_counts = netflix_genres.value_counts()

top_imdb = imdb_df.sort_values(by="averageRating", ascending=False).head(1000)
imdb_genres = top_imdb["genres"].dropna().str.split(",").explode()
imdb_genre_counts = imdb_genres.value_counts()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
netflix_genre_counts.head(10).plot(kind="bar", ax=axes[0], title="Top 10 Netflix Genres")
imdb_genre_counts.head(10).plot(kind="bar", ax=axes[1], title="Top 10 IMDB Genres")
plt.tight_layout()
plt.savefig("finalproject/results/netflix_genres.png")
plt.savefig("finalproject/results/imdb_genres.png")
plt.close()

# Originals vs Non-Originals Ratings question 2
merged_df["is_original"] = merged_df["title"].str.contains("netflix", case=False, na=False)
merged_df.groupby("is_original")["averageRating"].mean().plot(kind="bar", title="Avg IMDB Rating: Netflix Original vs Non-Original")
plt.tight_layout()
plt.savefig("finalproject/results/original_vs_nonoriginal.png")
plt.close()

# Availability of Top 1000 IMDB titles on Netflix question 3
top_rated = imdb_df.sort_values("averageRating", ascending=False).head(1000)
top_rated["on_netflix"] = top_rated["primaryTitle_lower"].isin(netflix_df["title_lower"])
percent_available = top_rated["on_netflix"].mean()
print(f"Percentage of Top 1000 IMDB titles available on Netflix: {percent_available:.4%}")

with open("results/top1000_availability.txt", "w") as f:
    f.write(f"Percentage of Top 1000 IMDB titles available on Netflix: {percent_available:.4%}\n")

# Ratings by Genre (Boxplot) question 4
merged_df["genre_list"] = merged_df["listed_in"].str.split(", ")
exploded = merged_df.explode("genre_list")
filtered = exploded[exploded["genre_list"].isin(
    exploded["genre_list"].value_counts()[exploded["genre_list"].value_counts() >= 30].index
)]

plt.figure(figsize=(12, 6))
sns.boxplot(data=filtered, x="averageRating", y="genre_list", orient="h")
plt.title("IMDb Ratings by Genre (Boxplot)")
plt.xlabel("IMDb Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("finalproject/results/genre_rating_boxplot.png")
plt.close()
