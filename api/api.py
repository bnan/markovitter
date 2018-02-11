from flask import Flask
from scrape import scrape
from markov import train, generate, generate_with
from flask_cors import CORS
import json
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongo', 27017)
db = client.test_database
tweets = db.tweets

@app.route('/new/<username>/', defaults={'include': None})
@app.route('/new/<username>/<include>', methods=['GET'])
def new(username, include):
    try:
        if not tweets.find_one({"username" : username }):
            tweets.insert_one({"username" : username, "tweets" : scrape(username)})
        obj = tweets.find_one({"username" : username })

        model, rmodel = train([e['full_text'] for e in obj["tweets"]])
        if include:
            text = generate_with(model, rmodel, include)
        else:
            text = generate(model)
        return json.dumps({
            'success': True,
            'message': ' '.join(text),
            'name': obj['tweets'][0]['user']['name'],
            'avatar': obj['tweets'][0]['user']['profile_image_url_https']
        })
    except:
        return json.dumps({
            'success': False,
            'message': 'Oops! An error occurred.',
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)

