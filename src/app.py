from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['POST'])
def callback_route():
    if request.is_json:
        data = request.json
