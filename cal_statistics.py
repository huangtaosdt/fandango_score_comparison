import read_file



#calculate variance 
def calc_variance(series):
    return sum([(item-series.mean())**2 for item in series])/len(series)
#caculating covariance
def calc_covariance(x,y):
    x_mean=x.mean()
    y_mean=y.mean()
    return sum([(item1-x_mean)*(item2-y_mean) for item1,item2 in zip(x,y)])/len(x)
#caculating correlation values
def calc_correlation(x,y):
    covariance=calc_covariance(x,y)
    x_st_deviation=calc_variance(x)**(1/2)
    y_st_deviation=calc_variance(y)**(1/2)
    return covariance/(x_st_deviation*y_st_deviation)

#get dataframe from read.py
movie_reviews=read_file.movie_reviews

#--------------part one--------------

#Recall calc_variance,so we can get variance and standart deviation.
#variance reveals how data cluster or spread aroud mean value. 
rt_var=calc_variance(movie_reviews['RT_user_norm'])
rt_stdev=rt_var**(1/2)
mc_var=calc_variance(movie_reviews['Metacritic_user_nom'])
mc_stdev=mc_var**(1/2)
fg_var=calc_variance(movie_reviews['Fandango_Ratingvalue'])
fg_stdev=fg_var**(1/2)
id_var=calc_variance(movie_reviews['IMDB_norm'])
id_stdev=id_var**(1/2)

print("Rotten Tomatoes (variance):", rt_var)
print("Metacritic (variance):", mc_var)
print("Fandango (variance):", fg_var)
print("IMDB (variance):", id_var)
print("\n")
print("Rotten Tomatoes (standard deviation):", rt_stdev)
print("Metacritic (standard deviation):", mc_stdev)
print("Fandango (standard deviation):", fg_stdev)
print("IMDB (standard deviation):", id_stdev)

print("\n")
#----------------part two---------------

#Call the calc_variance method to get the covariance.
rt_fg_covar=calc_covariance(movie_reviews['RT_user_norm'],movie_reviews['Fandango_Ratingvalue'])
mc_fg_covar=calc_covariance(movie_reviews['Metacritic_user_nom'],movie_reviews['Fandango_Ratingvalue'])
id_fg_covar=calc_covariance(movie_reviews['IMDB_norm'],movie_reviews['Fandango_Ratingvalue'])

#Call the calc_correlation method to get the correlation values.
rt_fg_corr=calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr=calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr=calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango", rt_fg_corr)
print("Correlation between Metacritic and Fandango", mc_fg_corr)
print("Correlation between IMDB and Fandango", id_fg_corr)


