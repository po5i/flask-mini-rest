from flask import Blueprint
from flask_restx import Resource, Api


blueprint = Blueprint('api', __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version="1.0",
    title="Mini REST API",
    description="A mini REST API",
)
ns = api.namespace('items', description='Item operations')
api.add_namespace(ns)


@ns.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
