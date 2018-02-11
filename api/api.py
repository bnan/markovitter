from flask import Flask
from scrape import scrape
from markov import train, generate
from flask_cors import CORS
import json
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongo', 27017)
db = client.test_database
tweets = db.tweets

@app.route('/new/<username>', methods=['GET'])
def new(username):
    try:
        if not tweets.find_one({"username" : username }):
            tweets.insert_one({"username" : username, "tweets" : scrape(username)})
        obj = tweets.find_one({"username" : username })
        model = train([e['full_text'] for e in obj["tweets"]])
        text = generate(model)
        return json.dumps({ 'message': ' '.join(text) })
    except:
        return json.dumps({ 'message': 'Oops! An error occurred.' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)

