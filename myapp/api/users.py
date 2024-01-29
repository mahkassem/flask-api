from flask import Blueprint, request, jsonify
from ..models.users import User

# create the blueprint
bp = Blueprint("users", __name__, url_prefix="/users")


# define the routes
@bp.route("/hello")
def hello():
    return "Hello, World!"


@bp.route("")
def index():
    return User.all(), 200


@bp.route("/<int:id>")
def show(id):
    user = User.find(id)
    return jsonify(user), 200 if user else 404


@bp.route("", methods=["POST"])
def create():
    try:
        user = User(**request.json).save()
        return jsonify(user), 201
    except Exception as e:
        return {"error": str(e)}, 400


@bp.route("/<int:id>", methods=["PUT"])
def update(id):
    try:
        user = User.find(id, serialize=False)
        user = user.update(**request.json)
        return jsonify(user), 200
    except Exception as e:
        return {"error": str(e)}, 400


@bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        user = User.find(id)
        user.delete()
        return jsonify(user), 200
    except Exception as e:
        return {"error": str(e)}, 400
