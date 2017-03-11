import matplotlib.pyplot as plt
import read_file



#caculate mean value 
def calc_mean(col):
    return col.mean()

#get dataframe from read.py
movie_reviews=read_file.movie_reviews
user_reviews=read_file.user_reviews

#calculating means value
means=user_reviews.apply(calc_mean)
rt_mean=means.iloc[0]
mc_mean=means.iloc[1]
fg_mean=means.iloc[2]
id_mean=means.iloc[3]

# add subplot
fig=plt.figure(figsize=(5,15))
ax1=fig.add_subplot(4,1,1)
ax2=fig.add_subplot(4,1,2)
ax3=fig.add_subplot(4,1,3)
ax4=fig.add_subplot(4,1,4)

# set characters for plots.
# set x range from 0.0 to 5.0
ax1.set_xlim(0.0,5.0)
ax2.set_xlim(0.0,5.0)
ax3.set_xlim(0.0,5.0)
ax4.set_xlim(0.0,5.0) 

# add mean-line to every plot
ax1.axvline(rt_mean,color='r')
ax2.axvline(mc_mean,color='r')
ax3.axvline(fg_mean,color='r')
ax4.axvline(id_mean,color='r')

# set caption text for every histplot.
ax1.text(1,25,"RT_user_norm")
ax2.text(1,30,"RT_user_norm")
ax3.text(1,20,"RT_user_norm")
ax4.text(1,25,"RT_user_norm")

# drawing plots
movie_reviews['RT_user_norm'].hist(ax=ax1)
movie_reviews['Metacritic_user_nom'].hist(ax=ax2)
movie_reviews['Fandango_Ratingvalue'].hist(ax=ax3)
movie_reviews['IMDB_norm'].hist(ax=ax4)


plt.show()
