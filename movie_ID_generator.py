import requests
import json
import pandas as pd
key = '349cd6a'

website = 'https://www.omdbapi.com/?apikey=349cd6a'

df = pd.read_csv('movies.csv')
movie_list = []
for i in range(100):
    id = df["imdb_title_id"][i]
    print(website+f"&i={id}")
    req = requests.get(website+f"&i={id}")
    movie_list.append(req.json())
with open('movies.json','w') as cache:
    json.dump(movie_list,cache,indent=4)
cache.close()