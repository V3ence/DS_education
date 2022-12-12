import pandas as pd

movies = pd.read_csv('C:\IDE\movies.csv')
ratings1 = pd.read_csv('C:/IDE/ratings1.csv')
ratings2 = pd.read_csv('ratings2.csv')
dates = pd.read_csv('C:\IDE\dates.csv')
dates['date'] = pd.to_datetime(dates['date'])
ratings = pd.concat([ratings1, ratings2], ignore_index=True)
ratings = ratings.drop_duplicates(ignore_index=True)
ratings_dates = pd.concat([ratings, dates], axis=1)
print(ratings_dates.tail(7))