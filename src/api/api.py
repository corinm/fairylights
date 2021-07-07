from time import sleep
from typing import Callable

from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from states.modes import modeStatesSerialised
from states.patterns import Pattern, statesSerialised

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class Modes(Resource):
    def get(self):
        return modeStatesSerialised, 200


class ModeCycle(Resource):
    def __init__(self, toCycle: Callable):
        self.toCycle = toCycle

    def get(self):
        self.toCycle()
        return None, 200


class ModeStaticPatterns(Resource):
    def get(self):
        return statesSerialised, 200


class ModeStatic(Resource):
    def __init__(self, toStatic: Callable[[Pattern], None]):
        self.toStatic: Callable[[Pattern], None] = toStatic

    def get(self, pattern: Pattern):
        self.toStatic(pattern)
        return None, 200


class ModeStop(Resource):
    def __init__(self, stop: Callable):
        self.stop = stop

    def get(self):
        self.stop()
        return None, 200


def runApiServer(toCycle: Callable, toStatic: Callable, stop: Callable):
    api.add_resource(Modes, "/modes")
    api.add_resource(ModeCycle, "/modes/cycle", resource_class_args=(toCycle,))
    api.add_resource(ModeStaticPatterns, "/modes/static")
    api.add_resource(ModeStatic, "/modes/static/<pattern>", resource_class_args=(toStatic,))
    api.add_resource(ModeStop, "/modes/stop", resource_class_args=(stop,))

    sleep(5)
    print(">>> s1")
    toStatic(Pattern.Twinkling_Complementary)
    sleep(5)
    print(">>> s2")
    toStatic(Pattern.Fireflies_StaticGlow)
    sleep(5)
    print(">>> c1")
    toCycle()
    sleep(5)
    print(">>> s3")
    toStatic(Pattern.Twinkling_Complementary)
    sleep(5)
    print(">>> s4")
    toStatic(Pattern.Fireflies_StaticGlow)
    sleep(5)
    print(">>> c2")
    toCycle()
    sleep(5)
    print(">>> stop")
    stop()
    print(">>> stopped")

    print("Starting api server")
    app.run(host="0.0.0.0", port=5001)
