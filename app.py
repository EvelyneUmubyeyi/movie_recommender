import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
from fuzzywuzzy import process
from scipy.sparse import load_npz
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout='wide')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tfidf_matrix = load_npz('./tfidf_matrix.npz')
movies_df = pd.read_csv('./movies.csv')

def recommend_similar_movies(movie_title, top_n=10):
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    movie_vector = tfidf_matrix[idx]
    similarity_scores = cosine_similarity(movie_vector, tfidf_matrix)
    similar_movie_indices = np.argsort(similarity_scores[0])[::-1][1:top_n+1]
    print(f"Because you watched '{movie_title}':")
    for idx in similar_movie_indices:
        print(f"  {movies_df.iloc[idx]['title']}")


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
        <p>Type a movie you like, and we will recommend you other movies you might like!</p>
    </div>
    """, unsafe_allow_html=True)

movie_name = st.text_input(label='', placeholder="Enter a movie name")

all_titles = movies_df['title'].tolist()
closest_match = process.extractOne(movie_name,all_titles)
recommend_similar_movies(closest_match[0])
