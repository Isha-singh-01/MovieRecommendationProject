import streamlit as st
import pickle
import pandas as pd
import requests

movies = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_df = pd.DataFrame(movies)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=39f8d008289c5e0cd7e33730a220eef6&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

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

st.title('Movie Recommender System')
selected_movie = st.selectbox(
    'Which movie did you watch today?',movies_df['original_title'].values)

if st.button('Recommend'):
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

