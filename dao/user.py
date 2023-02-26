# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from dao.model.user import User


class UserDAO:
    def __init__(self, session) -> None:
        self.session = session

    def get_one(self, uid) -> list:
        return self.session.query(User).get(uid)

    def get_by_username(self, username: str) -> list:
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self) -> list:
        return self.session.query(User).all()

    def create(self, created_user_data) -> User:
        created_user = User(**created_user_data)
        self.session.add(created_user)
        self.session.commit()
        return created_user

    def delete(self, uid) -> None:
        deleted_user = self.get_one(uid)
        self.session.delete(deleted_user)
        self.session.commit()

    def update(self, updated_user_data):
        user = self.get_one(updated_user_data.get("id"))
        user.name = updated_user_data.get("name")
        user.password = updated_user_data.get("password")
        self.session.add(user)
        self.session.commit()
