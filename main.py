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
from flask import Flask

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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)