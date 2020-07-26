import setuptools

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": f"Hello, World!"})

@app.route('/<name>')
def hello_name(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
 app.run()