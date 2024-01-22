#importing the required libraries
import streamlit as st
import pickle
import pandas as pd
import requests

#loading the movies,similarity matrix, and csr_matrix
movies = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
popular = pickle.load(open('popular.pkl','rb'))
popular_movies_df = pd.DataFrame(popular)
movies_df = pd.DataFrame(movies)
csr_data = pickle.load(open('csr_data','rb'))

#Fetching the movie posters using TMDB API
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=39f8d008289c5e0cd7e33730a220eef6&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

#Recommendation Function based on Content based filtering
def recommend(movie):
    movie_index = movies_df[movies_df['original_title']==movie].index[0]
    distances = similarity[movie_index]
    recommend_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommendations = []
    posters = []
    for i in recommend_list:
        movie_id = movies_df.iloc[i[0]]['id']
        recommendations.append(movies_df.iloc[i[0]]['original_title'])
        posters.append(fetch_poster(movie_id))
    return recommendations,posters

#Recommendation Function based on Collaborative based filtering
from sklearn.neighbors import NearestNeighbors
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)
def collaborative_recommendation(movie):
    movie_index = movies_df[movies_df['original_title']==movie].index[0]
    distances, indices = knn.kneighbors(csr_data[movie_index],n_neighbors=6)
    recommended_list = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x:x[1])[:0:-1]
    recommendations = []
    posters = []
    for items in recommended_list:
        movie_id = movies_df.iloc[items[0]]['id']
        recommendations.append(movies_df.iloc[items[0]]['original_title'])
        posters.append(fetch_poster(movie_id))
    return recommendations, posters

#Function to fetch the Top 5 Trending Movies based on rating
def popular_movies():
    titles = popular_movies_df['original_title'].values
    ids = popular_movies_df['id'].values
    genres = popular_movies_df['genres'].values
    vote_count = popular_movies_df['vote_count'].values
    vote_average = popular_movies_df['vote_average'].values
    movieIDs = []
    list_of_titles = []
    genreslist = []
    count = []
    rating = []
    for i in titles:
        list_of_titles.append(i)
    for i in ids:
        movieIDs.append(i)
    for i in genres:
        genreslist.append(i)
    for i in vote_count:
        count.append(i)
    for i in vote_average:
        rating.append(i)
    return list_of_titles, movieIDs, genreslist, count, rating

#Title of our website
st.title('Movie Recommender System')

#Input box to fetch a movie from user
selected_movie = st.selectbox(
        'Please select a movie',movies_df['original_title'].values)

#Button for recommendation
if st.button('Recommend Movie'):
    st.subheader('Based on what you liked', divider='rainbow') #shows content based filtering recommendations
    movies, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movies[0])
        st.image(posters[0])
    with col2:
        st.text(movies[1])
        st.image(posters[1])
    with col3:
        st.text(movies[2])
        st.image(posters[2])
    with col4:
        st.text(movies[3])
        st.image(posters[3])
    with col5:
        st.text(movies[4])
        st.image(posters[4])

    st.subheader('You may also like', divider='rainbow') #shows collaborative based filtering recommendations
    user_movies, poster = collaborative_recommendation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(user_movies[0])
        st.image(poster[0])
    with col2:
        st.text(user_movies[1])
        st.image(poster[1])
    with col3:
        st.text(user_movies[2])
        st.image(poster[2])
    with col4:
        st.text(user_movies[3])
        st.image(poster[3])
    with col5:
        st.text(user_movies[4])
        st.image(poster[4])

st.subheader('Top 5 Trending Movies', divider='rainbow')
titles,movie_id, genres, counts, ratings = popular_movies()
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.text(titles[0])
    st.image(fetch_poster(movie_id[0]))
    #st.text(f"Genres: {genres[0]}")
    st.text(f"Votes: {counts[0]}")
    st.text(f"Rating: {ratings[0]}/10")
with col2:
    st.text(titles[1])
    st.image(fetch_poster(movie_id[1]))
    #st.text(f"Genres: {genres[1]}")
    st.text(f"Votes: {counts[1]}")
    st.text(f"Rating: {ratings[1]}/10")
with col3:
    st.text(titles[2])
    st.image(fetch_poster(movie_id[2]))
    #st.text(f"Genres: {genres[2]}")
    st.text(f"Votes: {counts[2]}")
    st.text(f"Rating: {ratings[2]}/10")
with col4:
    st.text(titles[3])
    st.image(fetch_poster(movie_id[3]))
    #st.text(f"Genres: {genres[3]}")
    st.text(f"Votes: {counts[3]}")
    st.text(f"Rating: {ratings[3]}/10")
with col5:
    st.text(titles[4])
    st.image(fetch_poster(movie_id[4]))
    #st.text(f"Genres: {genres[4]}")
    st.text(f"Votes: {counts[4]}")
    st.text(f"Rating: {ratings[4]}/10")
