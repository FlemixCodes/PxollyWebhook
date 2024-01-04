from flask import Flask, request, jsonify
from .events import Event, event_manager
from .vk import Vk
from .database import Settings


app = Flask(__name__)
vk = Vk()


@app.route("/", methods=['POST'])
def callback_route():
    if request.is_json:
        data = request.json
        event = Event(data)

        result_event = event_manager.use_event(event, vk)
        if result_event:
            return jsonify(result_event)
        else:
            ...