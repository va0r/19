# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
# import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid: int):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, username: str):
        return self.dao.get_by_username(username)

    def create(self, created_user_data: dict):
        created_user_data["password"] = self.get_password_hash(created_user_data.get("password"))
        return self.dao.create(created_user_data)

    def update(self, updated_user_data: dict):
        updated_user_data["password"] = self.get_password_hash(updated_user_data.get("password"))
        self.dao.update(updated_user_data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_password_hash(self, password) -> hashlib:
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            password_hash,
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )

# TODO проверить return-ы у CR-D
