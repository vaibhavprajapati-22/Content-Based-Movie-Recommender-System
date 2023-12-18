from flask import Flask, render_template, request, jsonify
from recommend import movies_recommendations

app = Flask(__name__)

all_movie_names = open('movies.txt','r', encoding='utf-8').readlines()
all_movie_names = [movie.strip() for movie in all_movie_names]

def is_subsequence(subsequence, sequence):
    sub_len, seq_len = len(subsequence), len(sequence)
    i = j = 0
    while i < sub_len and j < seq_len:
        if subsequence[i].lower() == sequence[j].lower():
            i += 1
        else :
            i = 0
        j += 1
    return i == sub_len

@app.route('/', methods=['GET'])
def index():
    page_size = 25
    current_page = int(request.args.get('page', 1))
    start_index = (current_page - 1) * page_size
    end_index = current_page * page_size
    movie_names = all_movie_names[start_index:end_index]
    return render_template('index.html', movie_names=movie_names, current_page=current_page)

@app.route('/search.html', methods=['GET'])
def search():
    search_query = request.args.get('query', '')
    matching_movies = [movie for movie in all_movie_names if is_subsequence(search_query.lower(), movie.lower())]
    return render_template('search.html', title=search_query, matching_movies=matching_movies)

@app.route('/play_movie.html', methods=['GET'])
def play_movie():
    movie_name = request.args.get('movie', '')
    print(movie_name)
    movie_name = movie_name.strip()
    recommendations = movies_recommendations(movie_name)
    print(recommendations)
    return render_template('play_movie.html', movie_name=movie_name, recommendations=recommendations)

@app.route('/api/movies', methods=['GET'])
def get_movies():
    all_movie_names = open('movies.txt', 'r', encoding='utf-8').readlines()
    return jsonify(all_movie_names)

if __name__ == '__main__':
    app.run(debug=True)
