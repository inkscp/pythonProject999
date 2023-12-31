import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

class News(SqlAlchemyBase, UserMixin, SerializerMixin):  # наследование от 3 классов
    __tablename__ = 'news'  # название таблицы
    # текст новости, дата, приватность, идентификатор автора новости - создаем объекты:
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)  # по дефолту новость приватная
    is_published = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))  # забираем форенки из др табл
    user = orm.relationship('User')  # мы берем user из класса User.  пользователь - много новостей, связь идет по id


    def __repr__(self):  # спецметод represent, чтобы вывести все новости юзера
        return f'{self.content}'