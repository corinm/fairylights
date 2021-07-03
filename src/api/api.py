from typing import Callable

from flask import Flask
from flask_restful import Api, Resource

from states.modes import modeStatesSerialised
from states.patterns import statesSerialised

app = Flask(__name__)
api = Api(app)


class ModeCycle(Resource):
    def __init__(self, toCycle: Callable):
        self.toCycle = toCycle

    def get(self):
        self.toStatic("Flickering")
        return None, 200


class ModeStatic(Resource):
    def __init__(self, toStatic: Callable):
        self.toStatic = toStatic

    def get(self, pattern):
        self.toStatic(pattern)
        return None, 200


class Modes(Resource):
    def get(self):
        return modeStatesSerialised, 200


class States(Resource):
    def get(self):
        return statesSerialised, 200


api.add_resource(Modes, "/modes")
api.add_resource(States, "/states")


def runApiServer(toCycle: Callable, toStatic: Callable):
    api.add_resource(ModeCycle, "/modes/cycle", resource_class_args=(toCycle,))
    api.add_resource(ModeStatic, "/modes/static/<pattern>", resource_class_args=(toStatic,))

    print("Starting api server")
    app.run(host="0.0.0.0")
