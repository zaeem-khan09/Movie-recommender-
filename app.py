import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Default poster
default_poster = "https://via.placeholder.com/150x220.png?text=Movie"

# Recommend function
def recommend(movie, num):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:num+1]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# UI
st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite ones!")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

num = st.slider("Number of recommendations", 5, 10)

# Button
if st.button("Recommend"):
    with st.spinner("Finding best movies..."):
        names = recommend(selected_movie, num)

        st.success("Recommendations generated successfully!")  # ✅ added

        cols = st.columns(5)
        for i in range(len(names)):
            with cols[i % 5]:
                st.image(default_poster)
                st.caption(names[i])
