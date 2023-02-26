# ----------------------------------------------------------------
# ok ok
# ----------------------------------------------------------------
from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, did: int) -> list:
        return self.session.query(Director).get(did)

    def get_all(self) -> list:
        return self.session.query(Director).all()

    def create(self, created_director_data: dict) -> Director:
        created_director: Director = Director(**created_director_data)
        self.session.add(created_director)
        self.session.commit()
        return created_director

    def delete(self, did) -> None:
        deleted_director: list = self.get_one(did)
        self.session.delete(deleted_director)
        self.session.commit()

    def update(self, updated_director_data: dict) -> None:
        updated_director: list = self.get_one(updated_director_data.get("id"))
        updated_director.name = updated_director_data.get("name")
        self.session.add(updated_director)
        self.session.commit()
