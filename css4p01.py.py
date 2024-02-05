
#Open Pandas library
import pandas as pd
#Read the CSV file into a Pandas DataFrame
file = pd.read_csv("movie_dataset.csv")
print(file)

#Dataframe details
print(file.info())
print(file.describe())

""" Question 1 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Identify and locate max value
highest_rated_movie = df.loc[df['Rating'].idxmax()]

print('The highest-rated movie in the IMDb dataset is:')
print(highest_rated_movie)


""" Question 2 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Calculate the average revenue, ignoring missing values
average_revenue = df['Revenue (Millions)'].mean()

print(f'The average revenue of all movies is: ${average_revenue:.2f}')


""" Question 3 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

start_year = 2015
end_year = 2017

#Filter rows within the specified year range
filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

#Calculate the average revenue for the filtered data
average_revenue = filtered_df['Revenue (Millions)'].mean()

print(f'The average revenue of movies from {start_year} to {end_year} is: ${average_revenue:.2f}')


""" Question 4 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

release_year = 2016

#Filter rows for the specified release year
movies_2016 = df[df['Year'] == release_year]

#Count the number of movies released in 2016
num_movies_2016 = len(movies_2016)

print(f'The number of movies released in the year {release_year} is: {num_movies_2016}')


""" Question 5 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

director_name = 'Christopher Nolan'

#Filter rows for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == director_name]

#Count the number of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

print(f'The number of movies directed by {director_name} is: {num_nolan_movies}')


""" Question 6 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

min_rating_threshold = 8.0

#Filter rows for movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= min_rating_threshold]

#Count the number of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)

print(f'The number of movies with a rating of at least {min_rating_threshold} is: {num_high_rated_movies}')


""" Question 7 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Assuming 'Director' is a column containing the director's name and 'Rating' is a column containing movie ratings
director_name = 'Christopher Nolan'

#Filter rows for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == director_name]

#Calculate the median rating for movies directed by Christopher Nolan
median_rating_nolan = nolan_movies['Rating'].median()

print(f'The median rating of movies directed by {director_name} is: {median_rating_nolan:.2f}')


""" Question 8 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Group by 'Release_Year' and calculate the mean rating for each year
average_ratings_by_year = df.groupby('Year')['Rating'].mean()

#Find the year with the highest average rating
year_highest_average_rating = average_ratings_by_year.idxmax()
highest_average_rating = average_ratings_by_year.max()

print(f'The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}')


""" Question 9 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Count the number of movies made in 2006 and 2016
num_movies_2006 = len(df[df['Year'] == 2006])
num_movies_2016 = len(df[df['Year'] == 2016])

#Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print(f'The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%')


""" Question 10 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Split the 'Actors' column into a list of actors for each movie
all_actors = df['Actors'].str.split(', ')

#Flatten the list of lists into a single list of all actors in all movies
all_actors_flat = [actor for sublist in all_actors.dropna() for actor in sublist]

#Count the occurrences of each actor
actor_counts = pd.Series(all_actors_flat).value_counts()

#Find the most common actor
most_common_actor = actor_counts.idxmax()
num_movies_with_most_common_actor = actor_counts.max()

print(f'The most common actor in all the movies is {most_common_actor} appearing in {num_movies_with_most_common_actor} movies.')


""" Question 11 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Split the 'Genre' column into a list of genres for each movie
all_genres = df['Genre'].str.split(', ')

#Flatten the list of lists into a single list of all genres in all movies
all_genres_flat = [genre for sublist in all_genres.dropna() for genre in sublist]

#Get unique genres
unique_genres = set(all_genres_flat)

#Count the number of unique genres
num_unique_genres = len(unique_genres)

print(f'The number of unique genres in the dataset is: {num_unique_genres}')


""" Question 12 """

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

#Select only numerical columns for correlation analysis
numerical_features = df.select_dtypes(include=['float64', 'int64'])

#Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

#Display the correlation matrix
print(correlation_matrix)









