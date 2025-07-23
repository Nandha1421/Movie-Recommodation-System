import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(path='data/movies_2024.csv'):
    return pd.read_csv(path)

def recommend_movies(input_storyline, df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Storyline'].fillna(""))
    input_vec = tfidf.transform([input_storyline])
    scores = cosine_similarity(input_vec, tfidf_matrix).flatten()
    top_indices = scores.argsort()[-5:][::-1]
    return df.iloc[top_indices][['Movie Name', 'Storyline']]
