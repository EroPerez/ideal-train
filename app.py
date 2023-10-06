from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Index</h2>'


@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"message": "Hello from flask 2.3.3"})


if __name__ == "__main__":
    app.run(debug=True)