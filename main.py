from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def main():
    with open('menu.json', 'r') as menu:
        return menu.read()

@app.route('/msx/<path:path>')
def start_msx(path):
    return send_from_directory('msx',path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)