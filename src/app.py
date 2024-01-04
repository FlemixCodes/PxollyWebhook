from flask import Flask, request, jsonify
from .events import Event
from .vk import Vk
from .database import Settings


app = Flask(__name__)
vk = Vk()


@app.route("/", methods=['POST'])
def callback_route():
    if request.is_json:
        data = request.json
        event = Event(data)
