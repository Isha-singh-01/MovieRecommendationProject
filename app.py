import streamlit as st
import pickle
import pandas as pd
import requests

movies = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
popular = pickle.load(open('popular.pkl','rb'))
popular_movies_df = pd.DataFrame(popular)
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


st.title('Movie Recommender System')

st.subheader('Recommendations', divider='rainbow')
selected_movie = st.selectbox(
    'Please select a movie',movies_df['original_title'].values)

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

st.subheader('Top 5 Trending Movies', divider='rainbow')
titles,movie_id, genres, counts, ratings = popular_movies()
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.text(titles[0])
    st.image(fetch_poster(movie_id[0]))
    with st.expander("See more"):
        st.text(f"Genres: {genres[0]}")
        st.text(f"Vote Counts: {counts[0]}")
        st.text(f"Rating: {ratings[0]}")
with col2:
    st.text(titles[1])
    st.image(fetch_poster(movie_id[1]))
    with st.expander("See more"):
        st.text(f"Genres: {genres[1]}")
        st.text(f"Vote Counts: {counts[1]}")
        st.text(f"Rating: {ratings[1]}")
with col3:
    st.text(titles[2])
    st.image(fetch_poster(movie_id[2]))
    with st.expander("See more"):
        st.text(f"Genres: {genres[2]}")
        st.text(f"Vote Counts: {counts[2]}")
        st.text(f"Rating: {ratings[2]}")
with col4:
    st.text(titles[3])
    st.image(fetch_poster(movie_id[3]))
    with st.expander("See more"):
        st.text(f"Genres: {genres[3]}")
        st.text(f"Vote Counts: {counts[3]}")
        st.text(f"Rating: {ratings[3]}")
with col5:
    st.text(titles[4])
    st.image(fetch_poster(movie_id[4]))
    with st.expander("See more"):
        st.text(f"Genres: {genres[4]}")
        st.text(f"Vote Counts: {counts[4]}")
        st.text(f"Rating: {ratings[4]}")
