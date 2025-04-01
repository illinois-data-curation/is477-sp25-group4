# Project Plan

### Members: Anantya Kasturi, Anee Anisa


### Group: 4


### Datasets:


- https://datasets.imdbws.com/


- https://www.kaggle.com/datasets/shivamb/netflix-shows



The first dataset we chose is from IMDb, and it shows not only basic information about movies (such as title, language, etc.), but also attributes between different parts of the data. The second dataset is from Kaggle, which shows an updated list of Netflix movies and TV shows. By using both of these datasets, we can analyze how Netflix suggests certain films and how that leads those films to become popularized. Upon a preliminary analysis on the datasets, we found that both contain information that will allow us to perform an in-depth analysis on film rankings and their distribution. 


### Overall Goal: 

This study attempts to find differences in genre trends, content accessibility, and quality perception by analyzing the relationship between Netflix's content library and the broader film industry. This study will investigate whether Netflix favors particular genres over highly regarded films, how well Netflix Originals perform in comparison to industry norms, and whether Netflix offers access to highly rated movies and TV shows by utilizing data from IMDB (TSV format) and Netflix (CSV format). 

Although streaming services like Netflix have a big influence on how people watch, their methods for selecting material are still mostly hidden. This research will offer data-driven insights into Netflix's decision-making process, specifically with regard to genre representation, the trade-off between quality and accessibility, and the comparison of Netflix-produced content with ratings and reviews from the industry as a whole. Customers, scholars, and media professionals will have a better understanding of how Netflix's collection fits into larger trends in television and movies by examining these factors. 

The data will be imported respectively and merged together. We plan on using all the files in the IMDB website and merging them to compare it with the netflix dataset afterwards. While the IMDB dataset offers title ratings, votes, and metadata for a huge collection of films and TV series, the Netflix dataset includes details about the titles that are available on the site, such as title, release year, genre, director, cast, and type (movie/TV show). By changing column formats, managing missing or duplicate items, standardizing genre classifications, and mapping Netflix titles to their IMDB counterparts using distinct identifiers such as title names and release years, the datasets will be cleaned and preprocessed. 

We plan on using OpenRefine learned in lab7 for our data cleaning as well. Python, notably Pandas, Matplotlib, and Seaborn, will be used for data analysis. By comparing Netflix's genre distribution to that of the larger IMDB database, the study will determine which genres are overrepresented and underrepresented and determine whether Netflix's content library leans toward any particular demographic. It will also look into whether Netflix favors mass-market or highly-rated films, compare the IMDB ratings of Netflix Originals to those of other movies, and find out which TV series and movies have the highest IMDB ratings available on Netflix. By comparing the average ratings of Netflix films to those of non-Netflix films and analyzing the performance of Netflix Originals in comparison to regular studio productions, the research will also determine whether Netflix prioritizes quantity over quality. 

We anticipate that this study will reveal trends in Netflix's genre preferences in comparison to the industry as a whole, provide insights into Netflix's emphasis on critical acclaim rather than audience popularity, provide a more comprehensive understanding of Netflix's strategy for Original content as opposed to acquired content, and demonstrate how Netflix's content strategy satisfies viewer expectations. In order to help consumers and media professionals comprehend the broader impacts of content curation, availability, and quality standards in the streaming era, this study will offer data-backed insights about Netflix's changing role in the film business.


### Research Questions:


- How does the genre distribution on Netflix compare to top-rated IMDB movies?


- Do Netflix Originals generally receive higher or lower IMDB ratings compared to non-Netflix content?


- Are highly-rated IMDB movies and TV shows available on Netflix?


### Team Responsibilities:


Anantya: 

- Create the Repository 

- Research and document the original sources of the datasets

- Ensure everything is complete, well-documented, and ready for submission


Anee:

- Develop research questions based on the datasets
  
- Perform initial data cleaning (handling missing values, formatting issues)
  
- Implement integrity checks (e.g., checksums, duplicates, consistency)
  

Shared Responsibilities: 

- Conduct exploratory data analysis (EDA)

- Perform statistical comparisons (e.g., rating distributions, genre trends)

- Create visualizations (graphs, charts) to support findings

- Collaborate to merge IMDB & Netflix data using Python/Pandas or SQL

- Both will commit changes, review code, and ensure version control
  
- Both will contribute to Markdown reports, ensuring clear explanations of methodology, findings, and conclusions


### Timeline:

#### Initial Project Plan (Due April 2nd)

[March 31 - April 2]  

- Finalize research questions  (Anee)

- Identify and document dataset sources (Anantya)

- Plan dataset retrieval strategy (programmatic acquisition or documented steps)  (Anantya)

- Outline data integration and analysis approach (Both)

- Write and submit project plan (Both)



#### Status Report (Due April 15th)

[April 3 - April 10]

- Write Python scripts for dataset acquisition  (Both)

- Implement integrity checks (checksums, missing values) (Anee)

- Perform initial data profiling and cleaning  (Anee)

- Conduct exploratory data analysis (EDA)  (Both)

[April 11 - April 15]

- Merge datasets programmatically (Pandas/SQL) (Both)

- Begin generating basic visualizations  (Both)

- Document progress and methodology (Anantya)

- Submit status report  (Anantya)




#### Final Project Submission (Due May 1st)

[April 16 - April 22]

- Finalize data integration and ensure dataset compatibility  (Anantya)

- Expand on analysis with additional insights  (Anee)

- Implement workflow automation (script execution from start to finish) (Both)

[April 23 - April 30]

- Create metadata for reproducibility  (Anantya)

- Complete Markdown documentation  (Both)

- Finalize citations for datasets and software used  (Anee)

- Archive project and obtain a persistent identifier (Both)

- Submit final project release on GitHub  (Anantya)


### Workflow & Tools

We will be using GitHub for collaboration and version control

For data cleaning, we plan on using Open Refine 

Since Python (Pandas, Matplotlib/Seaborn) can be used for data analysis, we will be able to generate more accurate visualizations

Our submission will make use of Markdown for documentation and reporting

Finally, we will utilize Checksums & Data Validation for integrity checks
