#чтобы пользователю отправлять автоматическое сообщение

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_mail(email, subject, text):  # параметры ф-ции текст
    addr_from = os.getenv('FROM')
    password = os.getenv('PASSWORD')

    msg = MIMEMultipart()  # объект,конструктор, который будет управлять нашими сообщениями
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))

    # прикрепить к серверу:
    server = smtplib.SMTP_SSL(os.getenv('HOST'), os.getenv('PORT'))
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
    return True
