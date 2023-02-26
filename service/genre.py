# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao: GenreDAO = dao

    def get_one(self, gid: int):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, created_genre_data: dict):
        return self.dao.create(created_genre_data)

    def update(self, updated_genre_data: dict):
        self.dao.update(updated_genre_data)
        return self.dao

    def delete(self, gid: int):
        self.dao.delete(gid)

# TODO проверить return-ы у CR-D
