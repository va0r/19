# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from helpers import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self) -> tuple[list, int]:
        director: str | None = request.args.get("director_id")
        genre: str | None = request.args.get("genre_id")
        year: str | None = request.args.get("year")
        filters: dict[str, str | None] = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        movies = movie_service.get_all(filters)
        result: list = MovieSchema(many=True).dump(movies)
        return result, 200

    @admin_required
    def post(self) -> tuple[str, int, dict]:
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):
    @auth_required
    def get(self, mid: int) -> tuple[dict, int]:
        movie = movie_service.get_one(mid)
        result = MovieSchema().dump(movie)
        return result, 200

    @admin_required
    def put(self, mid: int) -> tuple[str, int]:
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, mid: int) -> tuple[str, int]:
        movie_service.delete(mid)
        return "", 204
