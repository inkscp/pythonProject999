# pip install flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms import EmailField
from wtforms.validators import DataRequired

# Если из формы добавлен файл, то обращаться к нему при обработке формы
# следует так: f.form.<название поля с файлом>.data


class LoginForm(FlaskForm):  # наш личный класс будет наследован из фласк форм
    email = EmailField('Ваша почта', validators=[DataRequired()])  # из обертки wtforms импортируем нужные поля
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')  # из него получается чек бокс запоминать меня или нет
    # file = FileField('Файл')
    submit = SubmitField('Войти')
