# IMDb Movie Recommendation System

This project scrapes 2024 movie storylines from IMDb, processes them using NLP techniques, and recommends similar movies using a Streamlit interface.

## Project Structure

- `scraper/scrape_imdb.py` - Scrapes IMDb movie names and storylines.
- `recommender/recommend.py` - TF-IDF + Cosine Similarity recommender logic.
- `app.py` - Streamlit app UI.
- `data/movies_2024.csv` - Output from scraper.

## Setup Instructions

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the scraper:
   ```
   python scraper/scrape_imdb.py
   ```

3. Launch the app:
   ```
   streamlit run app.py
   ```
