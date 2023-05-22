from flask import Flask, send_from_directory, request
from pathlib import Path
import json
import os


app = Flask(__name__)

@app.route('/')
def main():
    with open('menu.json', 'r', encoding='utf8') as menu:
        menu_dict = json.loads(menu.read())

    movie_path = 'media/movies'
    movies = []
    for movie in os.listdir(movie_path):
        movies.append({
            'title': movie,
            'action': f'video:http://{{SERVER}}/{movie_path}/{movie}/vid.mp4',
            'image': f'http://{{SERVER}}/{movie_path}/{movie}/img.jpg'
        })
    menu_dict['menu'][0]['data']['items'] = movies
    return json.dumps(menu_dict)
    
@app.route('/media/<path:path>')
def media(path):
    return send_from_directory(Path('media'), path)

@app.route('/msx/<path:path>')
def start_msx(path):
    return send_from_directory('msx', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)