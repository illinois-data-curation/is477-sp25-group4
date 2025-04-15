# Status Interim Report

### Members: Anantya Kasturi, Anee Anisa


### Group: 4


### Datasets:


- https://datasets.imdbws.com/


- https://www.kaggle.com/datasets/shivamb/netflix-shows

### Project Overview

Our project aims to analyze and compare data from two major entertainment platforms, Netflix and IMDb, to answer key research questions about genre distributions, content ratings, and content availability. Specifically, we want to explore trends in top-rated genres, evaluate how Netflix Originals perform compared to non-original content, and assess how much of IMDb’s highest-rated content is accessible on Netflix. This analysis has both academic and practical uses for understanding content curation, viewer preferences, and platform strategies.

### Project Updates

We began writing our Python script for analysis in a Google Colab notebook. We chose to use Google Colab because of its collaborative capabilities, ease of sharing, and built-in support for Jupyter-style code execution. Originally, our plan was to use OpenRefine for cleaning and transforming the data, but we quickly discovered that for our specific use case such as dropping irrelevant columns, standardizing text values, and filtering rows using Pandas in Python provided more flexibility and efficiency. OpenRefine, while strong for clustering and reconciling data inconsistencies through visual tools, didn’t align well with our need for a programmatic, reproducible workflow.

During data cleaning, we focused on several key preprocessing tasks. First, we ensured that all missing or null values were removed to prevent inaccurate analyses later on. We also filtered the datasets to retain only entries with valid titles, genres, and ratings. Because we were working with two different datasets (one from Netflix and another from IMDb), we paid special attention to standardizing titles to lowercase before merging to ensure accurate matches.

Here are the key Python libraries we used in our code:
Import os
Import pandas as pd
Import kagglehub
Import zipfile
Import requests
From io import BytesIO
Import matplotlib.pyplot as plt

We then downloaded both datasets and began cleaning. We only kept rows with valid titles and genres. We also filtered to only include movies and TV shows that have ratings. Then we merged the data based on lowercase titles. We wanted to see how the genre distribution compared to top rated IMDb movies. So, we imported Counter from collections and sorted by IMDb top-rated genres. We plotted the Top 10 Netflix Genres and IMDB Genres. Then, we wanted to see if Netflix Originals generally received higher or lower IMDb ratings compared to non-Netflix content. So we performed some manual checks to see what would be the best way to differentiate between a Netflix Original or a non original. Then we compared ratings using groupby and created a visualization to compare. Lastly, we wanted to see whether or not highly-rated IMDb movies and TV shows are available on Netflix. To calculate this, we sorted the top rated values across both and calculated the percentage of the top 500 IMDb titles available on Netflix which was 0.60%. 

### Updated Timeline

#### Completed Plan: 
Initial Project Plan (Due April 2nd)
- [March 31 - April 2]  
- Finalize research questions  (Anee)
- Identify and document dataset sources (Anantya)
- Plan dataset retrieval strategy (programmatic acquisition or documented steps)  (Anantya)
- Outline data integration and analysis approach (Both)
- Write and submit project plan (Both)

Status Report (Due April 15th)
- [April 3 - April 10]
- Write Python scripts for dataset acquisition  (Both)
- Implement integrity checks (checksums, missing values) (Anee)
- Perform initial data profiling and cleaning  (Anee)
- Conduct exploratory data analysis (EDA)  (Both)
- [April 11 - April 15]
- Merge datasets programmatically (Pandas/SQL) (Both)
- Begin generating basic visualizations  (Both)
- Document progress and methodology (Anantya)
- Submit status report  (Anantya)

#### Pending Tasks:
Final Project Submission (Due May 1st)
- [April 16 - April 22]
- Build on current code for more in-depth analysis (Both)
- Find better visualizations and explore how to showcase findings 
- Finalize data integration and ensure dataset compatibility  (Anantya)
Already figured out 
- Expand on analysis with additional insights  (Anee)
- Implement workflow automation (script execution from start to finish) (Both)
- We are currently thinking about how best to incorporate Snakemake into our workflow, especially since we are working in a Google Colab environment. Because Snakemake is typically more compatible with local or Linux-based environments, we plan to spend more time exploring workarounds or consider packaging our Colab steps into a bash script or Python function that mimics Snakemake-like automation.
- [April 23 - April 30]
- Create metadata for reproducibility  (Anantya)
- Complete Markdown documentation  (Both)
- Finalize citations for datasets and software used  (Anee)
- Archive project and obtain a persistent identifier (Both)
- Submit final project release on GitHub  (Anantya)

### Changes to Project Plan
Overall, we have stayed aligned with our initial project plan. The main deviation was our switch from OpenRefine to Pandas for data cleaning, which ultimately proved more suitable for our goals. Additionally, we’ve already begun gaining insights earlier than expected, allowing us more time in the coming weeks to refine our analyses and visuals.
Moving forward, we plan to dig deeper into our datasets. This includes analyzing metadata such as release year, director, cast, and content type. We also aim to explore ratings trends across time and whether genre popularity varies by year if there’s time. These insights could enrich our understanding of content strategies on each platform.
Another area for improvement is data visualization. While our current plots are functional, we believe that using libraries like Seaborn or Plotly may help us create more detailed and interactive graphs, particularly for the final presentation.
Lastly, we’ll be working on making our workflow reproducible from start to finish. Whether this means incorporating Snakemake, or modular Python functions, we plan on spending time to learn how to ensure that others can run our analysis with minimal setup. We are foreseeing that we don't need to change our timeline any further because everything has been going according to plan.

