from imdb import IMDb
import pandas as pd
import os

ia = IMDb()

results = ia.search_movie('2024')  # keyword search, results not guaranteed accurate by year

movies_2024 = []

for movie in results:
    ia.update(movie)
    if movie.get('year') == 2024:
        plot = movie.get('plot outline') or 'No plot available'
        movies_2024.append({
            'Movie Name': movie['title'],
            'Storyline': plot
        })
    if len(movies_2024) >= 100:
        break

os.makedirs("data", exist_ok=True)
df = pd.DataFrame(movies_2024)
df.to_csv("data/movies_2024.csv", index=False)
print("✅ Successfully saved movies_2024.csv")