#
# Simple Flask app
#
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return subpath


@app.route('/data', methods=['GET'])
def get_query_string():
    return request.query_string


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
