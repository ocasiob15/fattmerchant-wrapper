#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
from controllers.store import store

app = Flask(__name__)
app.register_blueprint(store)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

