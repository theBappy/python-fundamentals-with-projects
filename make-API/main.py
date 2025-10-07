from flask import Flask
from flask.json import jsonify
import random

app = Flask(__name__)

@app.route("/")
def life():
    fin = open("make-API\\quote.txt", "r")
    random_line = random.randint(0, 5)
    quote = fin.readlines()[random_line]
    return jsonify(quote[:-1])

if __name__ == "__main__":
    app.run(debug=True)