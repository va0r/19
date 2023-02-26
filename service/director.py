# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------

from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao: DirectorDAO = dao

    def get_one(self, did: int):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, created_director_data: dict):
        return self.dao.create(created_director_data)

    def update(self, updated_director_data: dict):
        self.dao.update(updated_director_data)
        return self.dao

    def delete(self, did: int):
        self.dao.delete(did)

# TODO проверить return-ы у C-UD
