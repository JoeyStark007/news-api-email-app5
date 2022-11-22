import smtplib
import ssl


def send_email_m(message):
    host = "smtp.gmail.com"
    port = 465
    password = 'vzxjowkaejyafiac'
    username = 'jgtefera@gmail.com'
    receiver = "jgtefera@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

