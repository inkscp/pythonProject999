from mail_sender import send_mail  # импортируем ф-цию, чтобы потестить
# pip install python-dotenv
from dotenv import load_dotenv

send_mail('inna.pshenichnikova@gmail.com', 'Вам письмо', 'Текст письма')