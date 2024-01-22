# Movie Recommendation using ML
## Overview
This project implements a Movie Recommendation System using both **Content-Based Filtering** and **Collaborative-Based Filtering** techniques. The system extracts movie data from the TMDb website, performs data cleaning, and utilizes machine learning algorithms to provide personalized movie recommendations.
## Data Collection
- [TMDB dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata): The dataset comprises of 3 files:
  - tmdb_5000_credits.csv (contains information about the cast and crew of the movie)
  - tmdb_5000_movies.csv (contains information about the movie such as genres, overview etc.)
  - ratings.csv (contains user and movie ratings)

## Content Based Filtering
The "Based on what you like" section displays movie recommendations based on Content Filtering. Content Based Filtering recommends items based on the characteristics and features of the items themselves. It relies on the content or attributes of the items and the user's preferences.

![ContentBased](https://github.com/Isha-singh-01/MovieRecommendationProject/assets/59357002/2115a395-2dd1-4675-96b7-c47d45f1472b)
<br> The following approach was used - 
- Cleaning the data by retaining only relevant information.
- Creating tags for each movie based on genres, overview, keywords, top 3 cast, and director.
- Calculating the distance among vectors using cosine similarity.


## Colaborative Based Filtering
Collaborative Filtering recommends items based on user behavior and preferences. It considers the actions and preferences of other users who are similar to the target user. 
The "You may also like" section displays movie recommendations based on Collaborative Filtering.
![collaborative](https://github.com/Isha-singh-01/MovieRecommendationProject/assets/59357002/179aa13a-17d3-44bd-bcfb-807c68cc81e1)
<br> The following approach was used - 
- Filtering the dataset to remove noise:
  - Movie qualification: Minimum 10 votes.
  - User qualification: Minimum 50 movies voted by the user.
- Using csr_matrix function from the scipy library to reduce data sparsity.
- Employing the KNN algorithm with cosine similarity metric for fast computation.

## Popular Movies based on user voting
![popular](https://github.com/Isha-singh-01/MovieRecommendationProject/assets/59357002/92faa9ce-e26f-4126-b95b-d4a0d8c636f9)

## Tableau Dashboard to visualize trends and preferences
- [Tableau public link](https://public.tableau.com/views/TMDBDashboard_17048701588970/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)
-  ![Dashboard 1](https://github.com/Isha-singh-01/MovieRecommendationProject/assets/59357002/b6b474df-a2ae-4023-aee3-1021277b9a7d)




