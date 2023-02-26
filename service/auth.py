# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
import calendar
import datetime

import jwt

from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        """
        Генерация токенов для пользователя

        @param username: логин
        @param password: пароль
        @param is_refresh: обновление пары токенов на основание токена обновления доступа
        @return: пара "токен доступа" и "токен обновления доступа"
        """

        user = self.user_service.get_by_username(username)  # получение пользователя из базы по логину

        if user is None:  # если пользователь не найден, вызываем ошибку
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

        data: dict = {
            "username": user.username,
            "role": user.role
        }

        # генерация токена доступа, срок жизни 60 минут
        min60 = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        data["exp"] = calendar.timegm(min60.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # генерация токена обновления доступа, срок жизни 360 дней
        days360 = datetime.datetime.utcnow() + datetime.timedelta(days=360)
        data["exp"] = calendar.timegm(days360.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {"access_token": access_token,
                "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get("username")

        user = self.user_service.get_by_username(username=username)

        if user is None:
            raise Exception()

        return self.generate_tokens(username, user.password, is_refresh=True)
