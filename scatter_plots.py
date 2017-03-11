import matplotlib.pyplot as plt
import read_file	

#get dataframe from read_file.py
movie_reviews=read_file.movie_reviews

#create figure and ax
fig=plt.figure(figsize=(4,8))
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
# set characters for scatters.
#set x-range
ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)

ax1.tick_params(labelbottom='off')
ax2.tick_params(labelbottom='off')
#set title
ax1.text(0.9,4.5,"RT vs Fan")
ax2.text(0.9,4.5,"Mc vs Fan")
ax3.text(0.9,4.5,"ID vs Fan")


#drawing scatter
ax1.scatter(movie_reviews['RT_user_norm'],movie_reviews['Fandango_Ratingvalue'])
ax2.scatter(movie_reviews['Metacritic_user_nom'],movie_reviews['Fandango_Ratingvalue'])
ax3.scatter(movie_reviews['IMDB_norm'],movie_reviews['Fandango_Ratingvalue'])

plt.show()
