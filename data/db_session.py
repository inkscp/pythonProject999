# создание базы данных и сессии по работе с ней
import sqlalchemy as sa
import sqlalchemy.orm as orm  # object relationship mapping
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()  # задаем переменную

created = None  # глобальн переменная создана ли сессия


def global_init(db_file):  # файл с таким именем будет созданю мы должны разрешить доступ внутри ф-ции:
    global created

    if created:
        return

    if not db_file or not db_file.strip():  # если мы на вход ф-ции ничего не подали или написали неск пробелов, то:
        raise Exception('Забыли подключить файл базы!')

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'  # строка для подключения базы данных. проверить тот же поток данных
    # для отладки. потом можно отключить
    print(f'Мы подключились к базе: {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)  # создаем движок
    created = orm.sessionmaker(bind=engine)  # связали с движком
    # для кого мы это все делали:
    from . import all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:  # эта функция будет возвращать сессию
    global created
    return created()
