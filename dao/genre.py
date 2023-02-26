# ----------------------------------------------------------------
# ok ok
# ----------------------------------------------------------------
from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, gid: int) -> list:
        return self.session.query(Genre).get(gid)

    def get_all(self) -> list:
        return self.session.query(Genre).all()

    def create(self, created_genre_data: dict) -> Genre:
        created_genre: Genre = Genre(**created_genre_data)
        self.session.add(created_genre)
        self.session.commit()
        return created_genre

    def delete(self, gid) -> None:
        deleted_genre: list = self.get_one(gid)
        self.session.delete(deleted_genre)
        self.session.commit()

    def update(self, updated_genre_data) -> None:
        updated_genre: list = self.get_one(updated_genre_data.get("id"))
        updated_genre.name = updated_genre_data.get("name")
        self.session.add(updated_genre)
        self.session.commit()
