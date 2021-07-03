from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    pass


api.add_resource(Users, "/users")
