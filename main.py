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
def index():
    return 'Адмирал<br><a href="/slogan">Слоган</a>'

@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
</head>
<body>
<h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/tigre.jpg')}"  # 
alt="Здесь должна была быть картинка, но не нашлась">
<p>И крепка, как смерть, любовь</p>
</body>
</html>"""

@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь<br><a href="/">Назад</a>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)