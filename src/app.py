from flask import Flask, request, jsonify
from events import Event


app = Flask(__name__)


@app.route("/", methods=['POST'])
def callback_route():
    if request.is_json:
        data = request.json
        event = Event(data)
