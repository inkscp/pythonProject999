import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase):   #все будем наследовать из этой биб-ки. поля:
    __tablename__ = 'users'  # служебный атрибут, указывает имя таблицы. которая будет создана в БД
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    create_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())

