# ----------------------------------------------------------------
# ok ok
# ----------------------------------------------------------------
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, mid) -> list:
        return self.session.query(Movie).get(mid)

    def get_all(self, filters: dict[str, str | None]) -> list:
        interim = self.session.query(Movie)
        if filters.get("director_id") is not None:
            interim = interim.filter(Movie.director_id == filters.get("director_id"))
        if filters.get("genre_id") is not None:
            interim = interim.filter(Movie.genre_id == filters.get("genre_id"))
        if filters.get("year") is not None:
            interim = interim.filter(Movie.year == filters.get("year"))
        return interim.all()

    def create(self, created_movie_data: dict) -> Movie:
        created_movie: Movie = Movie(**created_movie_data)
        self.session.add(created_movie)
        self.session.commit()
        return created_movie

    def delete(self, mid) -> None:
        deleted_movie: list = self.get_one(mid)
        self.session.delete(deleted_movie)
        self.session.commit()

    def update(self, updated_movie_data: dict) -> None:
        self.session.query(Movie).filter(Movie.id == updated_movie_data.get('id')).update(updated_movie_data)
        self.session.commit()
