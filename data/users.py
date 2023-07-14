import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin  # чтобы юзеры успешно авторизовались

class User(SqlAlchemyBase, UserMixin):  # чтобы методы вручную не прописывать. наш класс юзер теперь обладает всеми свойствами класса UserMixin
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True,
                              unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now())
    news = orm.relationship("News", back_populates='user')

    def __repr__(self):  # спецметод represent, чтобы вывести не объекты, а людей
        return f'{self.name} - {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)  #зашифрованный пароль запишется в таблицу

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


