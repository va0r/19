# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao: MovieDAO = dao

    def get_one(self, mid: int):
        return self.dao.get_one(mid)

    def get_all(self, filters: dict):
        return self.dao.get_all(filters)

    def create(self, created_movie_data: dict):
        return self.dao.create(created_movie_data)

    def update(self, updated_movie_data: dict):
        self.dao.update(updated_movie_data)
        # return self.dao

    def delete(self, mid: int):
        self.dao.delete(mid)

# TODO проверить return-ы у CR-D
