# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# каркасный вариант приложения
from flask import Flask, url_for  # подключаем конструктор и урл

app = Flask(__name__)

@app.route('/')  #декораторы
@app.route('/index')
def index():
    return 'hello'

@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Start')
    return '<br>'.join(lst)  #br - перенос на новую строку

@app.route('/slogan')
def slogan():
    return 'Адмирал<br><a href="/slogan">Слоган</a>'

@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/tigre.jpg')}"
alt="Здесь должна была быть картинка, но не нашлась">
<p class='red'>И крепка, как смерть, любовь</p>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>"""

# @app.route('/slogan')
# def slogan():
#     return 'Ибо крепка, как смерть, любовь<br><a href="/">Назад</a>'

@app.route('/nekrasov')
def nekrasov():
    return
<img src="{url_for('static', filename='images/nekrasov.jpg')}"
alt="Здесь должна была быть картинка, но не нашлась">



<p class='red'>И крепка, как смерть, любовь</p>
<p><\p>

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)