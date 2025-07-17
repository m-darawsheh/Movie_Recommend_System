from flask import Flask , render_template
import pandas as pd
import ast  # This import is needed for ast.literal_eval
from flask import request  # This import is needed for request.form

app = Flask(__name__)

movies_df = pd.read_csv("tmdb_5000_movies.csv")
credits_df = pd.read_csv("tmdb_5000_credits.csv")

movies_df['id'] = pd.to_numeric(movies_df['id'], errors='coerce')
credits_df['movie_id'] = pd.to_numeric(credits_df['movie_id'], errors='coerce')

movies_df = movies_df.dropna(subset=['id'])
credits_df = credits_df.dropna(subset=['movie_id'])

df = pd.merge(movies_df, credits_df, left_on='id', right_on='movie_id')
df = df.rename(columns={"title_x": "title"}) 
df['cast'] = df['cast'].apply(ast.literal_eval)
df['crew'] = df['crew'].apply(ast.literal_eval)

@app.route('/')
def index():
    return render_template('index.html')

def get_movies_by_person(name):
    name = name.lower()
    result_movies = []

    for _, row in df.iterrows():
        for actor in row['cast']:
            if actor.get('name', '').lower() == name:
                result_movies.append(row['title'])
                break

        for crew_member in row['crew']:
            if crew_member.get('job') == 'Director' and crew_member.get('name', '').lower() == name:
                result_movies.append(row['title'])
                break

    return list(set(result_movies))

@app.route('/get_movie')
def get_movie():
    return render_template('input_page.html')

@app.route('/get_movie_by_cast_name_or_character',methods=['POST'])
def get_movie_by_cast_name_or_character():
    person_name = request.form['name']
    print("person_name------------",person_name)
    movies = get_movies_by_person(person_name)
    print("movies------------",movies)
    return render_template('results.html', name=person_name, movies=movies)

if __name__ == '__main__':
    app.run(debug=True, port=5001)