import streamlit as st
from recommender.recommend import load_data, recommend_movies

st.title("🎬 IMDb Movie Recommender")
st.write("Enter a storyline and get movie recommendations!")

storyline = st.text_area("Enter movie storyline")

if st.button("Recommend"):
    if not storyline.strip():
        st.warning("Please enter a storyline.")
    else:
        df = load_data()
        results = recommend_movies(storyline, df)
        st.success("Top 5 Recommendations:")
        for _, row in results.iterrows():
            st.markdown(f"**{row['Movie Name']}**")
            st.markdown(f"_{row['Storyline']}_\n")
