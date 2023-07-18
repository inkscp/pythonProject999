# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
#
# каркасный вариант приложения
from flask import Flask, url_for, request, redirect, abort, jsonify  # подключаем конструктор и урл
from flask import render_template, json
import requests

from data.news_api import blueprint
from loginform import LoginForm
import sqlalchemy
from data import db_session, news_api
from mail_sender import send_mail
from data.users import User
from data.news import News
from forms.add_news import NewsForm
from forms.user import RegisterForm
from flask import make_response, session
from flask_login import LoginManager, login_user, login_required
from flask_login import logout_user, current_user
import datetime
from flask_restful import reqparse, abort, Api, Resource
import news_resources   # второй способ подключения приложения
# pip install sqlalchemy

app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()  # конструктор логин-менеджера, создали объект
login_manager.init_app(app)  # мы прописали его в нашем приложении

app.config[
    'SECRET_KEY'] = 'too short key'  # тут пишется вместо туу шорт ки длинный ключ с цифрами. буквами. спецсимволами
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/news.sqlite'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365)  # чтобы сессия действовала год. даже если закрыть браузер


#  прописываем функцию для получения пользователя, лучше писать функцию вверху, чтобы логин работал корректно:
@login_manager.user_loader  # рядом с декоратором не нужны скобки
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)  # вернет юзера, кот успешно авторизовался на нашем сайте


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')  # редирект юзера на страницы после авторизации и без нее


# ошибка 404
# @app.errorhandler(404)
# def http_404_error(error):
#     return redirect('/error404')


@app.errorhandler(400)
def http_400_handler(_):
    return make_response(jsonify({'error400': 'Некорректный запрос'}), 400)


@blueprint.errorhandler(404)
def http_404_error(error):
    return make_response(jsonify({'error': f'Новости не найдены'}), 404)

@app.route('/error404')
def well():  # колодец
    return render_template('well.html')  # прописать динозавтра


@app.errorhandler(401)
def def_http_401_handler(error):
    return redirect('/login')


@app.route('/')
@app.route('/index')
def index():
    # работу с БД начинаем с откр сессии
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    # db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    return render_template('index.html', title='Новости', news=news)
    # param = {}
    # param['username'] = "Слушатель"
    # param['title'] = "Расширяем шаблоны"
    return "hi"


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)


# @app.route('/news')
# def news():
#     lst = ['Ann', 'Tom', 'Bob']
#     return render_template('news.html', title="FOR", news=lst)

@app.route('/news', methods=['POST', 'GET'])
# добавлять новость может только тот. кто авторизован
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()  # создали сессию
        news = News()  # создаем объект, обращаемся к orm модели News
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)  # слияние сессии с залогиненным пользователем
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', form=form)
    # with open("news.json", "rt", encoding="utf-8") as f:
    #     news_list = json.loads(f.read())
    #     return render_template('news.html', title='Новости', news=news_list)


@app.route('/news/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_news(id):
    print(id)
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
        print(current_user, News.id, id, News.user)
        if news:
            form.title.data = news.title  # если новость была
            form.content.data = news.content
            form.is_private.data = news.is_private  # получаем из таблицы новостей
        # аварийный выход из ф-ции с передачей ошибки
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
        if news:
            news.title = form.title.data  # если новость была
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
            return render_template('news.html', title='Редактирование новости', form=form)


@app.route('/vartest')
def vartest():
    return render_template('var_test.html', title='Переменные в HTML')

    # return redirect('/Form')  # Безусловный редирект


#     return 'hello'
#
# @app.route('/countdown')
# def countdown():
#     lst = [str(x) for x in range(10, 0, -1)]
#     lst.append('Start')
#     return '<br>'.join(lst)  #br - перенос на новую строку
#
# @app.route('/slogan')
# def slogan():
#     return 'Адмирал<br><a href="/slogan">Слоган</a>'
#
# @app.route('/poster')
# def poster():
#     return f"""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Постер</title>
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
#     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
# </head>
# <body>
# <h1>Постер к фильму</h1>
# <img src="{url_for('static', filename='images/tigre.jpg')}"
# alt="Здесь должна была быть картинка, но не нашлась">
# <p class='red'>И крепка, как смерть, любовь</p>
# <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
# </body>
# </html>"""

# @app.route('/slogan')
# def slogan():
#     return 'Ибо крепка, как смерть, любовь<br><a href="/">Назад</a>'


@app.route('/greeting/<username>')  # строковый параметр
def greeting(username):
    return f"""<!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <title>{username}</title>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
 </head>
 <body>
 <h1>Привет, {username}</h1>
 <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
 </body>
 </html>"""


@app.route('/nekrasov')
def nekrasov():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Некрасов</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<h1>"Славная осень"</h1>
<img height="920" width="720" src="{url_for('static', filename='images/nekrasov.jpg')}"
alt="Здесь должна была быть картинка, но не нашлась">
<div class="p-3 mb-2 bg-secondary text-white">.Славная осень! Здоровый, ядрёный</div>
<div class="p-3 mb-2 bg-info text-white">.Воздух усталые силы бодрит</div>
<div class="p-3 mb-2 bg-dark text-white">.Лёд неокрепший на речке студёной</div>
<div class="p-3 mb-2 bg-transparent text-dark">.Словно как тающий сахар лежит</div>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>"""


@app.route('/variants/<int:var>')
def variants(var):
    if var == 1:
        return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Варианты выбора</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
            <h1>"Мюнхгаузен"</h1>
        <body>
        <dl>
        <dt>Пан или пропал</dt>
        <dd>А что, нельзя выжить, став паном?</dd>
        </dl>
        </body></html>"""
    elif var == 2:
        return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Варианты выбора</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
            <h1>"Мюнхгаузен"</h1>
        <body>
        <dl>
        <dt>Даже если Вас съели, у Вас есть два выхода</dt>
        <dd>А в рассказах Мюнхгаузена есть другой способ.</dd>
        </dl>
        </body></html>"""


#
# <p class='red'>И крепка, как смерть, любовь</p>
# <p><\p>


@app.route('/slideshow')  # Карусель
def slideshow():
    return f"""<!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <title>nyc</title>
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
         <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
     </head>
     <body>
     <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
       <div class="carousel-inner">
         <div class="carousel-item active">
           <img src="{url_for('static', filename='css/nyc1.jpg')}" class="d-block w-100">
         </div>
         <div class="carousel-item">
           <img src="{url_for('static', filename='css/nyc2.jpg')}" class="d-block w-100">
         </div>
         <div class="carousel-item">
           <img src="{url_for('static', filename='css/nyc3.jpg')}" class="d-block w-100">
         </div>
     </div>
     <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
     </body>
     </html>"""


@app.route('/form_sample', methods=['GET', 'POST'])  # Форма
def form_sample():
    if request.method == "GET":
        return render_template('user_form.html', title='Форма')
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file') - чтобы не выбросило искл-е. более мягкая форма
        f.save('./static/images/loaded.png')
        myform = request.form.to_dict()  # превратили в словарь
        return render_template('filled_form.html', title='Ваши данные', data=myform)
        # print(request.form['fname'])
        # print(request.form['sname'])


@app.route('/load_photo', methods=['GET', 'POST'])  # Загрузить фото
def load_photo():
    if request.method == 'GET':
        return f"""
        <form class="login_form" method="post" enctype="multipart/form-data">   <!--метод пост отправляет на сервер. гет - в браузер. Энктайп Мультипарт - чтобы форма перегоняла файлы-->
        <div class='form_group'>
        <label for="photo">Приложите фото</label>
        <input type="file" class="from-control-file" id="photo" name="file">
        </div><br>
        <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
        """
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file') - чтобы не выбросило искл-е. более мягкая форма
        f.save('./static/images/loaded.png')
        return '<h1>Файл у Вас на сервере</h1>'


@app.route('/weather_form', methods=['GET', 'POST'])  # методы задаем
def weather_form():
    if request.method == 'GET':
        return render_template('weather_form.html', title='Выбор города')
    elif request.method == 'POST':
        town = request.form.get('town')
        data = {}  # передать данные словаря, пустой
        key = 'f0c001f47039c4f29a033fbdd14851a6'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        code = weather['cod']
        # нужно еще прописать, что если код не 200, то информация не найдена
        icon = weather['weather'][0]['icon']
        temperature = weather['main']['temp']
        data["code"] = code
        data["icon"] = icon
        data['temp'] = temperature
        return render_template('weather.html', title=f'Погода в городе {town}', town=town, data=data, icon=icon)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # обращаюсь к объекту, вызываю метод
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()  # проверка есть ли юзер с каким имейлом
        if user and user.check_password(form.password.data):  # проверяем хэшированный пароль с хэшем в БД
            login_user(user, remember=form.remember_me.data)
            return redirect('/')  # если успешно залогинился юзер, то выбрасывает его на главную
        # return redirect('/success')  # если валидация прошла успешно
        return render_template('login.html', title='Повторная авторизация', message='Неверный логин или пароль',
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)  # если форму вызвали, то ее надо передать


@app.route('/success')
def success():
    return 'Success'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  # валидация формы
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title="Проблемы с регистрацией",
                                   message='Пароли не совпадают', form=form)  # нужно передать форму
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():  # проверяем нет ли такого имейла в базе
            return render_template('register.html', title="Проблемы с регистрацией",
                                   message='Пользователь с таким email уже существует', form=form)
        user = User(name=form.name.data, email=form.email.data, about=form.about.data)  # если все ок-создали юзера
        user.set_password(form.password.data)
        db_sess.add(user)  # добавляем юзера в БД
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count != 0 and visit_count <= 20:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1), max_age=60 * 60 * 24 * 365 * 2)
    elif visit_count > 20:
        res = make_response('Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', '1', max_age=0)
    else:
        res = make_response('Вы впервые здесь за 2 года')
        res.set_cookie('visit_count', '1', max_age=60 * 60 * 24 * 365 * 2)
        return res


@app.route('/session_test')  # то. что в декораторе, обязано что-то вернуть - return
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    if session['visit_count'] > 3:
        session.pop('visit_count', None)  # чтобы лимитировать сессии, после 4 начинается отсчет сначала
    session.permanent = True  # максимум 31 день
    return make_response(f'Мы тут были уже {visit_count + 1} раз.')


@app.route('/news_del/<int:id>', methods=['GET', 'POST'])  # то. что в декораторе, обязано что-то вернуть - return
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')  # подключились к сессии
    # подключаем АПИ с помощью blueprint
    # app.register_blueprint(news_api.blueprint)

    # подключаем АПИ с помощью flask-restful (второй способ подключения приложения, можно на лету добавлять, в отл от блюпринт.
    # миграция - похоже на систему контроля версий. но только для баз данных. фиксирует все изменения)
    # для чего регистрируем классы из news_resources
    # 1. для списка объектов
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    # 2. для одного объекта
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    app.run(host='127.0.0.1', port=5000, debug=True)
    # в сложных запросах:
    #  '|' - означает ИЛИ
    #  '&' означает И
    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 2).first()
    # print(user.news)
    # for news in user.news:  # для переменной news
    #     print(news)

    # чтобы пользователь добавил новость
    # news = News(title='Новости от Владимира', content='Опаздываю на работу', user_id=1, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()
    # id = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='Новость от Владимира №2', content='Больше не опаздываю на работу', user_id=id.id, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 1).first() # обращаемся напрямую через объект класс и метод append
    # news = News(title='Новость от Владимира №3', content='На месте', is_private=False)
    # user.news.append(news)  # новость добавить новости
    # db_sess.commit()
    # #
    # user = db_sess.query(User).filter(User.id == 1).first()
    # subj = News(title='Новость от Владимира №4', content='Пошел на обед', is_private=False)
    # user.news.append(subj)  # новость добавить новости
    # db_sess.commit()
    # users = db_sess.query(User).filter(User.email.notilike('%v%'))  # запрос к конкретному классу

    # user = db_sess.query(User).filter(User.id == 1).first()  # Вольдемара сделать Владимиром
    # user.name = 'Vladimir'
    # db_sess.commit()

    # user = db_sess.query(User).filter(User.name == 'Dmitry').first()  # удалить юзера
    # db_sess.delete(user)
    # db_sess.commit()
    # for user in users:
    #     print(user)
    # user = User()
    # user.name = 'Mark'
    # user.about = 'plumber'
    # user.mail = 'mark@mail.ru'
    # db_sess = db_session.create_session()  # создаем сессию
    # db_sess.add(user)  # добавить юзера
    # db_sess.commit()
