import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

columns_movies = ['ID', 'Title', 'Genres']
movies = pd.read_csv('movies.dat', sep='::', engine='python', header=None, names=columns_movies)
movies['Genres'] = movies['Genres'].str.replace('|', ', ')
movies['Info'] = movies['Title'] +" " + movies['Genres']

cv = CountVectorizer()
count_matrix = cv.fit_transform(movies['Info'])
similarity = cosine_similarity(count_matrix)

with open('similarity_matrix.pkl', 'wb') as file:
    pickle.dump(similarity, file)
    
# def get_movie_recommendations(movie_title):
#     movie_index = movies.index[movies['Title'] == movie_title].tolist()[0]
#     movie_similarity_scores = list(enumerate(similarity[movie_index]))
#     movie_similarity_scores = sorted(movie_similarity_scores, key=lambda x: x[1], reverse=True)
#     top_n = 5
#     similar_movies = [(movies['Title'][i], score) for i, score in movie_similarity_scores[1:top_n+1]]
#     return similar_movies

with open('similarity_matrix.pkl', 'rb') as file:
    similarity = pickle.load(file)
    
columns_movies = ['ID', 'Title', 'Genres']
movies = pd.read_csv('movies.dat', sep='::', engine='python', header=None, names=columns_movies)

def movies_recommendations(movie_title):
    movie_index = movies.index[movies['Title'] == movie_title].tolist()[0]
    movie_similarity_scores = list(enumerate(similarity[movie_index]))
    movie_similarity_scores = sorted(movie_similarity_scores, key=lambda x: x[1], reverse=True)
    top_n = 10
    similar_movies = [(movies['Title'][i], score) for i, score in movie_similarity_scores[1:top_n+1]]
    movies_list = [movie for movie, _ in similar_movies]
    return movies_list
    
    