import smtplib
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "marcedl88@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "marcedl88@gmail.com"

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)

