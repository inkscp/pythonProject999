# http://127.0.0.1:5000/api/news
import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin  # чтобы юзеры успешно авторизовались

# роль пользователя/ ключи в словаре ACCESS. По дефолту каждый новый пользователь - user
ACCESS = {
    'user': 1,
    'admin': 2
}

class User(SqlAlchemyBase, UserMixin, SerializerMixin):  # чтобы методы вручную не прописывать. наш класс юзер теперь обладает всеми свойствами класса UserMixin. Множественное наследование
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True,
                              unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # как прописать админский доступ:
    level = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now())
    news = orm.relationship("News", back_populates='user')

    def __repr__(self):  # спецметод represent, чтобы вывести не объекты, а людей
        return f'{self.name} - {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)  #зашифрованный пароль запишется в таблицу

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    # проверяем, является ли пользователь админом
    def is_admin(self):
        return self.level == ACCESS['admin']  #буллево значение True/False

    # разрешение действий пользователя с текущим уровнем/ если нет, то можно написать, что ваш уровень не позволяет вам. можно задавать это с самого начала (пригодится. если уровней больше чем 2)
    def allowed(self, access_level):
        return self.level >= access_level


