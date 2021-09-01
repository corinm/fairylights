from typing import Callable

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource

from modes import states as modes
from patterns import Pattern
from patterns import states as patterns

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


@app.route("/")
def index():
    return "index"


class Modes(Resource):
    def __init__(self):
        self.modes = [(i, modes[i].name) for i in range(len(modes))]

    def get(self):
        return self.modes, 200


class Patterns(Resource):
    def __init__(self):
        self.patterns = [(i, patterns[i].serialise()) for i in range(len(patterns))]

    def get(self):
        return self.patterns, 200


class Lights(Resource):
    def __init__(self, toCycle: Callable, toStatic: Callable, stop: Callable, getCurrentLights: Callable):
        self.toCycle: Callable = toCycle
        self.toStatic: Callable[[Pattern], None] = toStatic
        self.stop: Callable = stop
        self.getCurrentLights: Callable = getCurrentLights

    def get(self):
        # TODO: Get values from state machines
        (mode, pattern) = self.getCurrentLights()
        return dict(mode=mode, pattern=pattern)

    def put(self):
        mode = request.args.get('mode')
        patternName = request.args.get('pattern')

        if mode == "cycle":
            self.toCycle()
            return None, 200
        elif mode == "stop":
            self.stop()
            return None, 200
        elif mode == "static":
            pattern = Pattern[patternName]
            self.toStatic(pattern)
            return None, 200
        else:
            return None, 400


def runApiServer(toCycle: Callable, toStatic: Callable, stop: Callable, getCurrentLights: Callable):
    """
    GET /modes
    GET /patterns
    PUT /lights?mode=X&pattern=Y
    """
    api.add_resource(Modes, "/modes")
    api.add_resource(Patterns, "/patterns")
    api.add_resource(
        Lights,
        "/lights",
        resource_class_args=(
            toCycle,
            toStatic,
            stop,
            getCurrentLights,
        ),
    )

    print("Starting api server")
    app.run(host="0.0.0.0", port=5001)
