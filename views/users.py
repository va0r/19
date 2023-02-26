# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self) -> tuple[list, int]:
        users: list = user_service.get_all()
        result: list = UserSchema(many=True).dump(users)
        return result, 200

    def post(self) -> tuple[str, int, dict]:
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>/')
class UserView(Resource):
    def get(self, uid: int) -> tuple[dict, int]:
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    def put(self, uid: int) -> tuple[str, int]:
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid: int) -> tuple[str, int]:
        user_service.delete(uid)
        return "", 204
