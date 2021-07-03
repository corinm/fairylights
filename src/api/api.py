from flask import Flask
from flask_restful import Api, Resource

from states.patterns import statesSerialised

app = Flask(__name__)
api = Api(app)


class CurrentState(Resource):
    def get(self):
        return [], 200


class States(Resource):
    def get(self):
        return statesSerialised, 200


api.add_resource(States, "/states")


def runApiServer():
    print("Starting api server")
    app.run(host="0.0.0.0")
