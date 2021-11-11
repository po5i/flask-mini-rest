from http import HTTPStatus
from typing import TypedDict

from flask import Blueprint
from flask_restx import Resource, Api, fields


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    version="1.0",
    title="Mini REST API",
    description="A mini REST API",
)
ns = api.namespace("items", description="Item operations")
api.add_namespace(ns)


# API Models
detail_model = api.model("Detail", {"id": fields.Integer, "name": fields.String})
item_model = api.model(
    "Item",
    {
        "id": fields.Integer,
        "name": fields.String,
        "details": fields.List(fields.Nested(detail_model)),
    },
)

# Request parsers
item_parser = api.parser()
item_parser.add_argument("id", type=int, location="form")
item_parser.add_argument("name", type=str, location="form")

detail_parser = api.parser()
detail_parser.add_argument("id", type=int, location="form")
detail_parser.add_argument("name", type=str, location="form")


# Types
class ItemDetails(TypedDict):
    """
    TypedDict for item details
    """

    id: int
    name: str


class Item(TypedDict):
    """
    TypedDict for item
    """

    id: int
    name: str
    details: list[ItemDetails]


# Memory "Database"
memory_object: list[Item] = [
    {
        "id": 1,
        "name": "Item 1",
        "details": [
            {"id": 1, "name": "Detail 1"},
            {"id": 2, "name": "Detail 2"},
        ],
    }
]


@ns.route("/")
class ItemsApi(Resource):
    """
    API for handling the Item list resource
    """

    @api.response(HTTPStatus.OK.value, "Get the item list", [item_model])
    @api.marshal_list_with(item_model)
    def get(self) -> list[Item]:
        """
        Returns the memory object
        """
        return memory_object

    @api.response(HTTPStatus.OK.value, "Object added")
    @api.expect(item_parser)
    def post(self) -> None:
        """
        Simple append something to the memory object
        """
        args = item_parser.parse_args()
        memory_object.append(args)


@ns.route("/<int:item_id>")
class ItemApi(Resource):
    """
    API for handling the single Item resource
    """

    @api.response(HTTPStatus.OK.value, "Get the item list", item_model)
    @api.response(HTTPStatus.BAD_REQUEST.value, "Item not found")
    @api.marshal_with(item_model)
    def get(self, item_id: int) -> Item:
        """
        Returns the memory object
        """
        try:
            return self._lookup(item_id)
        except StopIteration:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Item not found")

    def _lookup(self, item_id):
        return next(
            (item for item in memory_object if item["id"] == item_id),
        )

    @api.response(HTTPStatus.NO_CONTENT.value, "Object added")
    @api.response(HTTPStatus.BAD_REQUEST.value, "Item not found")
    @api.expect(detail_parser)
    def post(self, item_id: int) -> None:
        """
        Simple append details to the memory object
        """
        args = item_parser.parse_args()
        try:
            if item := self._lookup(item_id):
                item["details"].append(args)
            return None
        except StopIteration:
            return api.abort(HTTPStatus.BAD_REQUEST.value, "Item not found")
