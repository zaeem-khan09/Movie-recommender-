import streamlit as st
import pandas as pd

# Load dataset
movies = pd.read_csv('movies.csv')

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    st.success("Recommendations generated successfully!")

    # Simple recommendation (random 5 movies)
    recommendations = movies.sample(5)

    for movie in recommendations['title']:
        st.write(movie)
