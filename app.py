import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
from fuzzywuzzy import process
from scipy.sparse import load_npz
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tmdbv3api import TMDb, Movie

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout='wide')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tfidf_matrix = load_npz('./tfidf_matrix_2.npz')
movies_df = pd.read_csv('./movies.csv')
tmdb = TMDb()
tmdb.api_key = '32d454b8da83a34184f709df16125749'

def get_movie_poster_url(movie_id):
    movie = Movie()
    try:
        details = movie.details(movie_id)
        poster_path = details.poster_path
        base_url = "https://image.tmdb.org/t/p/w300"
        poster_url = base_url + poster_path
    except Exception as e:
        poster_url = "https://res.cloudinary.com/dpuyeblqg/image/upload/v1711736581/movie_cover_jnsbcf.webp"
    return poster_url

def recommend_similar_movies(movie_title, top_n=12):
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    movie_vector = tfidf_matrix[idx]
    similarity_scores = cosine_similarity(movie_vector, tfidf_matrix)
    similar_movie_indices = np.argsort(similarity_scores[0])[::-1][1:top_n+1]
    movies_dict = {}
    for idx in similar_movie_indices:
        poster_url = get_movie_poster_url(movies_df.iloc[idx]['id'])
        movies_dict[movies_df.iloc[idx]['title']] = poster_url
    return  movies_dict

def load_lottie(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_file = load_lottie("https://lottie.host/378de3b3-9c52-4f44-ae7e-fc218966cfd8/XIk4mpKKLA.json")

# with st.container():
st.markdown("""
    <style>
        .stApp {
            padding: 0px;
        }
    </style>
""", unsafe_allow_html=True)

if lottie_file is not None:
    st_lottie(lottie_file, speed=1, key="animated_image", height=300)
else:
    st.write("Failed to load Lottie animation.")
st.markdown("""
    <div style='text-align: center;'>
        <h1>Welcome to CineMatch</h1>
        <p>Select a movie you like, and we will recommend you other movies you might like!</p>
    </div>
    """, unsafe_allow_html=True)

# movie_name = st.text_input(label='', placeholder="Enter a movie name")
all_titles = movies_df['title'].tolist()
all_titles_with_placeholder = [''] + all_titles
movie_name = st.selectbox(label="", options=all_titles_with_placeholder)
if movie_name != '':
    closest_match = process.extractOne(movie_name,all_titles)
    if closest_match[0]:
        recommended_movies = recommend_similar_movies(closest_match[0])
        st.write(f"Because you watched '{closest_match[0]}':")

        col1, col2, col3 = st.columns(3)

        for idx, (movie_name, poster_url) in enumerate(recommended_movies.items()):
            if idx % 3 == 0:
                container = col1
            elif idx % 3 == 1:
                container = col2
            else:
                container = col3

            container.image(poster_url, use_column_width=True)
            container.write(movie_name)