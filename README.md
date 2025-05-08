 # IS 477 Final Project Report

### Group Members: 
Anee Anisa, Anantya Kasturi

### Group Number: 
4
 
### Title:
Netflix and IMDb Ratings Analysis

### Link to archival record: 
https://sandbox.zenodo.org/records/215139

### Contributors: 
Anee Anisa and Anantya Kasturi


### Summary
For our project, we decided to look at two datasets: Netflix data from Kaggle and IMDb data from the platform itself. Our goal was to find how IMDb ratings influence the movies and TV shows Netflix uses for its platform. In order to do this, we centered our project around a complete analysis and comparison of data from the two platforms. Our main objective through analysis was to investigate prominent trends and insights. Specifically, we wanted to look at top ten genre distributions in both Netflix and Imdb content, the availability of top-rated content on Netflix, IMDb ratings compared between Netflix originals and non-originals, and IMDb ratings by genre. By conducting such an analysis, we were able to highlight how different kinds of content are promoted and curated, and what genres resonated most with audiences. We also were able to see how the availability of streaming aligns with user demand. This project is important because it studies media trends, data-driven decision making in the entertainment industry, and user behavior. This project could offer crucial insights for streaming platforms, content creation, and marketing purposes. We can understand and adapt to ever changing trends in viewer preferences and dynamics within the digital landscape.

The four core research questions we focused on were the following:

1. What are the most prominent genres on Netflix compared to the top-rated IMDb titles?
2. How do the Netflix Originals perform compared to non-original Netflix content on IMDb?
3. To what extent are the highly-rated IMDb movies and tv shows available on Netflix?
4. How do the IMDb ratings compare by genre?

Our approach to this study involved gathering metadata from both sources, conducting extensive cleaning and integration, using Python, Pandas, and Seaborn, and visualizing the trends. Through this process, we were able to discover that while Netflix mainly caters to a broader international audience while IMDb’s top rated content focuses more on traditional genres like Biography, History, and Drama. We also saw that Netflix Originals generally received a lower average rating on IMDb compared to non-original content. This was interesting because the originals often have extreme marketing on their side. Moreover, there was little overlap between top-rated IMDb content and the Netflix content. Only 1.1% of the top 1000 titles were currently available on Netflix. Lastly, our genre analysis showed that certain genres often received ratings (documentaries, classics), while others received lower average ratings (reality tv, stand-up comedy). We created genre-level boxplots of IMDb ratings, which gave us detailed insights into how specific genres performed on both platforms. Documentaries and classics had a higher median rating while reality tv shows and stand up comedy showed more variability and lower ratings. With the unexpected flops within each genre, there were outliers in both directions. Therefore, having a nuanced understanding and model for genre-level analysis over the aggregate scores was important. 

Overall, our project emphasizes how data from various platforms can be used to analyze user preferences, media trends, and strategic choices made by the streaming platforms. Through our process of cleaning, merging, and visualizing the data, we were able to draw crucial conclusions that could be useful in the future for content creators, marketing teams, and consumers. The insights we uncovered further reinforced the importance of having open source data in a transforming industry and showed how analytical tools can piece together even the most complex of datasets in the entertainment industry. 

### Data profile
We used two publicly available datasets to complete our analysis. The first was from Kaggle, which contains metadata for Netflix content, and the other from IMDb’s official data repository, datasets.imdbws.com, which contains multiple files with different information but only information about titles and their IMDb ratings were used for this report. 

The Netflix dataset was sourced from Kaggle at (https://www.kaggle.com/datasets/shivamb/netflix-shows). It includes metadata for thousands of movies and TV shows available on Netflix. Some of the key columns include title, genre (listed as "listed_in"), release year, type (TV Show or Movie), cast, director, date added, rating (TV-MA, PG, etc.), and duration. The dataset is licensed under a Creative Commons License (CC BY-NC-SA 4.0), meaning it can be freely used for educational or research purposes as long as it's not for commercial gain and proper credit is given. Before merging this data with the IMDb dataset, we performed several preprocessing steps. We removed rows that had missing or null values in critical columns like title and genre. Additionally, all titles were converted to lowercase to ensure consistency when matching with IMDb titles, since capitalization differences can interfere with data merges later on. 

The second dataset we used was obtained directly from IMDb’s official data dump site at datasets.imdbws.com. IMDb provides multiple .tsv.gz files representing different aspects of their catalog. For this project, we focused on two of the seven different files: title.basics.tsv.gz and title.ratings.tsv.gz. The title.basics.tsv.gz file contains metadata like title ID (tconst), primary title, title type (e.g., movie or TV series), and genres. The title.ratings.tsv.gz.file includes IMDb ratings for each title along with the number of votes. These files are provided by IMDb for personal and non-commercial use under their terms of service. Similar to the Netflix dataset, we cleaned the IMDb data by dropping rows with missing or invalid values in key fields like primayTitle, genres, and averageRating. We also converted all relevant text columns (e.g., primaryTitle) to lowercase to facilitate case-insensitive joins with the Netflix dataset.

A major part of our preprocessing focused on aligning the two datasets and making them compatible. Although both contain title names, the formatting often differs slightly. Netflix might list a title like "The Office (U.S.)" while IMDb has it as "The Office." To manage these inconsistencies, we standardized all titles to lowercase and relied on exact string matching. This resolved the majority of mismatches, although some differences remained due to punctuation, subtitles, or different naming conventions. Additionally, we limited our analysis to only movies and TV series from IMDb (excluding shorts, video games, etc.) to align with the types of content represented in the Netflix dataset.
Overall, by carefully cleaning, filtering, and standardizing both datasets, we created a reliable foundation for future comparisons between Netflix’s available content and IMDb’s highly rated titles. This sets up our analysis to be as accurate and informational as possible while retaining as much data.

### Findings 

After cleaning and merging the datasets, we conducted 4 primary analyses. 

The first question in our research was “How does the genre distribution on Netflix compare to top-rated IMDB movies?” For this genre comparison we found out that Netflix’s top genres included International movies, dramas, comedies, international TV shows, documentaries, action & adventure, TV dramas, independent movies, children & family movies, and romantic movies, whereas IMDb’s top-rated content skews toward genres like documentary, drama, comedy, thriller, music, romance, crime, history, action, and biography. 

![Top 10 Genres](https://github.com/illinois-data-curation/is477-sp25 group4/blob/ab40cd2a24bb1b6defcbb52cea0db67400714f4c/netflix_genres.png)







These differences reveal Netflix’s tendency to cater to international and diverse audiences, while IMDb’s top 1000 is more aligned with Hollywood blockbusters. There is though overlap between the genres as well such as dramas, comedies, and documentaries that show common interest and popularity among entertainment in general. Something to also note is that dramas and tv dramas are separated in the Netflix dataset so combined together it has an even higher overall rating similar to the IMDb ratings. 

The second question in our research was “Do Netflix Originals generally receive higher or lower IMDB ratings compared to non-netflix content?” For this original vs non-original comparison we created a bar chart comparing the average IMDb ratings of Netflix originals and non-originals. 

This bar chart shows how netflix originals tend to receive lower ratings on average with a rating of around 4.5 whereas other content on netflix has an average rating of around 6.5. This can be caused by a multiple of things such as the few number of Netflix originals out there leading to higher impact if one of them does bad. Overall though the difference suggests a critical gap despite the marketing prominence of Netflix originals. 

The third question we asked in our research was “Are highly-rated IMDB movies and TV shows available on Netflix?” For this comparison we simply executed some mathematical code to find quantitative answers for how much of IMDb rated movies are on Netflix. We took the top 1000 IMDb rated content and saw how much of that was available on Netflix. We came out with a result of 1.10% of IMDb’s top 500 rated titles are currently available on Netflix. This extremely low overlap emphasizes how limited Netflix’s catalog is when it comes to historically top-rated content. It points to potential gaps in licensing, competition from other streaming services, or Netflix’s strategic pivot toward prioritizing Originals over acquiring legacy content.

The last question we researched about and added at the end was “What are the IMDb ratings of each genre including factors like average rating and outlier productions.” For this comparison between rating by genre we created a genre-level box plot analysis. 

This revealed that genres like "Documentaries" and "Classic Movies" tend to receive higher IMDb ratings on average, while genres such as "Reality TV" and "Stand-Up Comedy" show more variability and generally lower ratings. This provides insight into which types of content are more likely to be critically well-received. It also shows outliers that can be useful in seeing if a genre is actually popular but skewed by a certain movie or series. On the same note but opposite view you can see movies that did exceptionally well in a certain genre through the outliers plotted on the right end of the graph. 

### Future Work

Although our analysis was able to offer a compelling view into how IMDb ratings are intertwined with Netflix content, this study only scratched the surface of what could be possible when working with rating and streaming data. There are several additional ways to explore and build on our findings which could uncover more nuanced results in the future.

One of the biggest future directions is expanding the scope of the streaming platforms we analyzed. Even though Netflix is one of the biggest streaming service providers, there are far more we could look into. For instance Hulu, Disney+, Amazon Prime Video, and HBO Max are all used frequently for streaming purposes and have equally unique content. Additionally, they target the same kinds of audiences and could shed light on differences in different content acquisition policies between each platform. Does one platform focus more on a specific genre? How about a specific region? One example of this would be how Disney+ ranks higher in family-oriented content, whereas HBO Max ranks higher in critically acclaimed dramas.

Another possible extension of our project could be a temporal analysis. By including a time series to analyze the time dimension, we could study how IMDb ratings and Netflix content evolve over a period of time, for example a year. This would give more insights into trends like how Netflix changes its high-rated content or shifts more towards original content during certains seasons or parts of the year. We would also be able to see how IMDb ratings may differ after a show or movie is added to Netflix - does it boost ratings? Or bring them down?

A deeper analysis could also be done using a machine learning model to predict how content performs based on its genre and other attributes. Using predictive modeling would be extremely useful in practically predicting how platforms could use such insights to make business decisions. Key features to be used would be genre, number of seasons, release year, country of origin, etc. Furthermore, natural language processing (NLP) could be used on user reviews and descriptions. Where IMDb ratings are numerical, user reviews on platforms which contain text contain powerful and unstructured data. This kind of analysis can reveal why content is rated in a certain way. By applying importance to analysis in reviews, we could spot recurring patterns in acting, pacing, plot, or more that may influence a show or movie’s rating. By adding this qualitative layer, we could complement the quantitative analysis already conducted.

We recognize that our current study has relied heavily on title matching across datasets, which gave us challenges. In future studies, adding matching algorithms would be useful to include titles of other languages or more localized versions of certain content. We recommend using a user personalization system to take into account user behavior. Future research with this could look into how rating data can be aligned with personal data (having taken precautions to protect user privacy) and show how biases or limited content diversity may exist on certain platforms. 

In conclusion, our project has opened up several additional ways to conduct further research and compare across various platforms. By applying machine learning, qualitative analysis, and other models, there are many options to continue building on this work. 

### Reproducing
In order to reproduce our work, we diligently prioritized documenting our methods, maintaining clean code and records, and using publicly available datasets. This section will outline the steps required to reproduce our results from accessing the data to evaluation. 

Our analysis used datasets which are available on Kaggle(Netflix) or the internet(IMDb). They were downloaded in CSV and tsv format respectively. We did the required processing using Python and the pandas library. We then used matplotlib and seaborn for visualizations, and scikit-learn for any modeling components. Below are the steps to replicate our results:

1. Clone the Repository:
   - git clone https://github.com/illinois-data-curation/is477-sp25-group4
   - cd finalproject 
2. Set up a virtual environment
   - python3 -m venv .venv
   - source .venv/bin/activate
3. Install required dependencies
   - pip install -r requirements.txt
   * This installs:
     + pandas for data manipulation
     + matplotlib and seaborn for plotting
     + snakemake for workflow automation
4. Download the datasets
   * Manually download the following datasets and place them in the data/ directory:
      + Netflix Dataset https://www.kaggle.com/datasets/shivamb/netflix-shows
         + Save as: data/netflix/netflix_titles.csv
      + IMDb Dataset datasets.imdbws.com only 2 files are necessary for download
      + Required files save as:
         + title.basics.tsv.gz → extract to → data/imdb/title.basics.tsv
         + title.ratings.tsv.gz → extract to → data/imdb/title.ratings.tsv
5. Run the snakemake workflow
   - Make sure you're in the finalproject/ directory
   - snakemake –cores 4
   * This will:
      + Run scripts/finalproject.py
      + Process and merge the datasets
      + Generate and save:
        + netflix_genres.png
        + imdb_genres.png
        + original_vs_nonoriginal.png
        + top1000_availability.txt
        + genre_rating_boxplot.png

Overall the structure of the folder should look this: 

We have additionally added comments in our code to explain the purpose and logic behind each step. This helps readers not only understand what we did, but why we did it. We made sure to use clear variable and function names to make the code more readable and easier to adapt for future studies. 

### References

"Netflix Shows Dataset." Kaggle, https://www.kaggle.com/datasets/shivamb/netflix-shows. Accessed 6 May 2025.

"IMDb Datasets." IMDb, https://datasets.imdbws.com/. Accessed 6 May 2025.

Seaborn: Statistical Data Visualization. https://seaborn.pydata.org/. Accessed 6 May 2025.

Köster, Johannes, et al. Snakemake Workflow Management System. https://snakemake.readthedocs.io/. Accessed 6 May 2025.

Matplotlib: Visualization with Python. https://matplotlib.org/. Accessed 6 May 2025.
