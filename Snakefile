rule all:
    input:
        "results/netflix_genres.png",
        "results/imdb_genres.png",
        "results/original_vs_nonoriginal.png",
        "results/top1000_availability.txt"

rule run_all_analysis:
    input:
        netflix="data/netflix/netflix_titles.csv",
        basics="data/imdb/title.basics.tsv",
        ratings="data/imdb/title.ratings.tsv"
    output:
        "results/netflix_genres.png",
        "results/imdb_genres.png",
        "results/original_vs_nonoriginal.png",
        "results/top1000_availability.txt"
    shell:
        "python scripts/finalproject.py"
