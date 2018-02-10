from flask import Flask
app = Flask(__name__)

@app.route('/new', methods=['GET'])
def new():
    return "I like turtles"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
