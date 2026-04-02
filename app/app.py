# ==========================================
# 🎬 Movie Recommendation System (Final Clean)
# ==========================================

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib


# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True
)


# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    return pd.read_csv("data/movies.csv")


# ==============================
# PREPROCESS
# ==============================
def preprocess(df):
    features = ['genres','keywords','tagline','cast','director']
    
    for f in features:
        df[f] = df[f].fillna('')
    
    df['combined_features'] = (
        df['genres'] + ' ' +
        df['keywords'] + ' ' +
        df['tagline'] + ' ' +
        df['cast'] + ' ' +
        df['director']
    )
    
    return df


# ==============================
# SIMILARITY
# ==============================
@st.cache_resource
def compute_similarity(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(df['combined_features'])
    return cosine_similarity(vectors)


# ==============================
# RECOMMEND FUNCTION
# ==============================
def recommend(movie_name, df, similarity):
    titles = df['title'].tolist()
    
    matches = difflib.get_close_matches(movie_name, titles)
    
    if not matches:
        return None, None
    
    match = matches[0]
    index = df[df.title == match].index[0]
    
    scores = list(enumerate(similarity[index]))
    sorted_movies = sorted(scores, key=lambda x: x[1], reverse=True)
    
    rec_df = pd.DataFrame([df.iloc[i[0]] for i in sorted_movies[1:50]])
    
    return match, rec_df


# ==============================
# LOAD PIPELINE
# ==============================
df = preprocess(load_data())

# 🔥 CLEAN DATA (REMOVE BAD TITLES)
df = df[df['title'].str.match(r'^[A-Za-z0-9]')]
df = df.drop_duplicates(subset='title')
df = df.sort_values('title')

similarity = compute_similarity(df)


# ==============================
# SIDEBAR FILTERS
# ==============================
st.sidebar.header("🎛️ Filters")

top_n = st.sidebar.slider("🎯 Number of Recommendations", 5, 50, 15)

rating_range = st.sidebar.slider("⭐ Rating Range", 0.0, 10.0, (5.0, 10.0))

sort_option = st.sidebar.selectbox("📊 Sort By", ["Popularity", "Rating"])


# ==============================
# SEARCH SECTION
# ==============================
st.subheader("🔍 Search Movie")

col1, col2 = st.columns(2)

with col1:
    selected_movie = st.selectbox(
        "🎬 Choose Movie",
        options=["Select a movie..."] + df['title'].tolist()
    )

with col2:
    manual_input = st.text_input("✍️ Or type movie")

movie_name = manual_input if manual_input else selected_movie

# Handle empty selection
if movie_name == "Select a movie...":
    st.warning("⚠️ Please select or type a movie")
    st.stop()


# ==============================
# BUTTON ACTION
# ==============================
if st.button("🚀 Recommend Movies"):
    
    with st.spinner("Finding best recommendations..."):
        
        match, rec_df = recommend(movie_name, df, similarity)
        
        if match is None:
            st.error("❌ Movie not found")
        
        else:
            st.success(f"🎯 Showing results for: {match}")
            
            original_df = rec_df.copy()
            
            # ==============================
            # APPLY FILTERS
            # ==============================
            rec_df = rec_df[
                (rec_df['vote_average'] >= rating_range[0]) &
                (rec_df['vote_average'] <= rating_range[1])
            ]
            
            # ==============================
            # FALLBACK
            # ==============================
            if rec_df.empty:
                st.warning("⚠️ No movies match filters → showing default results")
                rec_df = original_df
            
            # ==============================
            # SORT
            # ==============================
            if sort_option == "Popularity":
                rec_df = rec_df.sort_values(by='popularity', ascending=False)
            else:
                rec_df = rec_df.sort_values(by='vote_average', ascending=False)
            
            rec_df = rec_df.head(top_n)
            
            # ==============================
            # SHOW COUNT
            # ==============================
            st.write(f"🎯 Showing {len(rec_df)} recommendations")
            
            # ==============================
            # TOP MOVIE
            # ==============================
            st.subheader("🔥 Top Recommendation")
            
            top_movie = rec_df.iloc[0]
            
            st.markdown(f"""
            <div style="
                background: linear-gradient(90deg,#1f4037,#99f2c8);
                padding:20px;
                border-radius:15px;
                margin-bottom:20px;
            ">
            <h2>🎬 {top_movie['title']}</h2>
            ⭐ Rating: {round(top_movie['vote_average'],1)} <br>
            📈 Popularity: {round(top_movie['popularity'],1)}
            </div>
            """, unsafe_allow_html=True)
            
            # ==============================
            # GRID DISPLAY
            # ==============================
            st.subheader("🍿 Recommended Movies")
            
            cols = st.columns(3)
            
            for i, (_, row) in enumerate(rec_df.iterrows()):
                
                with cols[i % 3]:
                    
                    popularity_percent = min(row['popularity'] / 10, 100)
                    
                    st.markdown(f"""
                    <div style="
                        background:#1e1e1e;
                        padding:15px;
                        border-radius:12px;
                        margin-bottom:15px;
                        box-shadow:0px 2px 10px rgba(0,0,0,0.3);
                    ">
                    
                    <h4>🎬 {row['title']}</h4>
                    
                    ⭐ {round(row['vote_average'],1)} <br>
                    
                    📈 Popularity
                    <div style="
                        background:#444;
                        border-radius:10px;
                        height:8px;
                        margin-top:5px;
                    ">
                        <div style="
                            width:{popularity_percent}%;
                            background:#00ffcc;
                            height:8px;
                            border-radius:10px;
                        "></div>
                    </div>
                    
                    </div>
                    """, unsafe_allow_html=True)


# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("<center>🚀 Built with Streamlit </center>", unsafe_allow_html=True)