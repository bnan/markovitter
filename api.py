from flask import Flask
from scrape import scrape
from markov import train, generate

app = Flask(__name__)

@app.route('/new', methods=['GET'])
def new():
    trump = scrape('realDonaldTrump')
    model = train([x['full_text'] for x in trump])
    text = generate(model)
    return ' '.join(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
