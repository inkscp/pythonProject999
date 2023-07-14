from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField
from wtforms import SubmitField, EmailField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):   # класс унаследован от фласк форм
    email = EmailField('*Email', validators=[DataRequired()])
    password = PasswordField('*Пароль', validators=[DataRequired()])
    password_again = PasswordField('*Повторите Пароль', validators=[DataRequired()])
    name = StringField('*Ваше имя', validators=[DataRequired()])
    about = TextAreaField('Немного о себе')
    submit = SubmitField('Регистрация')

