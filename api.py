from flask import Flask
from scrape import scrape
from markov import train, generate

app = Flask(__name__)
models = {}

@app.route('/new/<username>', methods=['GET'])
def new(username):
    if username not in models:
        models[username] = scrape(username)
    model = train([e['full_text'] for e in models[username]])
    text = generate(model)
    return ' '.join(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
