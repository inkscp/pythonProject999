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
from flask import Flask, url_for  # подключаем конструктор и урл
#
app = Flask(__name__)
#
# @app.route('/')  #декораторы
# @app.route('/index')
# def index():
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



from flask import Flask, url_for, request

app = Flask(__name__)

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


@app.route('/slideshow')  #Карусель
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


@app.route('/form_sample', methods=['GET', 'POST'])  #Форма
def form_sample():
    if request.method == "GET":
        return f"""<!DOCTYPE html>
         <html lang="en">
         <head>
             <meta charset="UTF-8">
             <title>Пример формы</title>
             <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
             <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
         </head>
         <body>
         <h1>Форма для регистрации</h1>
         <div class="container">
         <form class="login_form" method="post">
         <input type="text" class="form-control" name="fname" placeholder="Фамилия"><br>  <!--нет закрывающего тэга у input-->
         <input type="text" class="form-control" name="sname" placeholder="Имя"><br>
         <input type="email" class="form-control" name="email" placeholder="email"><br>
         <input type="password" class="form-control" name="password" placeholder="password"><br>
         <div class="form-group">
         <label for="classSelect">Ваше образование</label>
         <select class="form-control" id="classSelect" name="profession">
         <option>Высшее</option>
         <option>Среднее</option>
         </select>
         </div>
         <button type="submit" class="btn btn-primary">Отправить</button>  <!--форма будет отправлять содержимое формы-->
         <!--Radio Button - Gender Selection-->
         <div class="form-group">
            <label for="form-check">Укажите пол</label>
            <div class="form-check">
            <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
            <label class="form-check-label" for="male">Мужской</label>
         </div>
         <div class="form-check">
            <input class="form-check-input" type="radio" name="sex" id="female" value="female">
            <label class="form-check-label" for="female">Женский</label>
            </div>
        </div>
        <!--End of gender selection-->
        <div>
        <label for="about">Немного о себе</label>
        <textarea class="form-control" id="about" name="about" rows="3"></textarea>
        </div><br>   <!--чтобы форма отлипла и не сливалась с полем-->
        <!--End of Text area-->
        <!--Check box-->
        <div>
        
        </div>
        <!--End of Check box-->
        </form>
         </body>
         </html>"""
    elif request.method == 'POST':
        print(request.method)
        print(request.form['fname'])
        print(request.form['sname'])
        return 'Форма отправлена'




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)