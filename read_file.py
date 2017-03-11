import pandas as pd

movie_reviews = pd.read_csv("fandango_score_comparison.csv")

# extract the following columns and return a new dataframe. 
user_reviews=movie_reviews[['RT_user_norm','Metacritic_user_nom','Fandango_Ratingvalue','IMDB_norm']]
