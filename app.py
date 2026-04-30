import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

st.title("Movie Recommendation System 🎬")

data = {
    'movie': ['Avengers', 'Iron Man', 'Thor', 'Titanic', 'Notebook', 'Inception'],
    'genre': ['action hero', 'action tech', 'action god', 'romance drama', 'romance love', 'sci-fi thriller']
}

df = pd.DataFrame(data)

cv = CountVectorizer()
matrix = cv.fit_transform(df['genre'])

similarity = cosine_similarity(matrix)

movie_name = st.text_input("Enter movie name:")

if movie_name:
    if movie_name in df['movie'].values:
        index = df[df['movie'] == movie_name].index[0]
        scores = list(enumerate(similarity[index]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

        st.write("Recommended movies:")
        for i in sorted_scores[1:4]:
            st.write(df.iloc[i[0]].movie)
    else:
        st.write("Movie not found")