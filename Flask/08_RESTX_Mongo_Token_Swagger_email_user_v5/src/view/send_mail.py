from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
import smtplib

from view import view

view_template = view()


def send_mail(login_user, name_user, email_to):
    body_template = view_template.welcome(login_user, name_user)
    print(body_template)
    message = MIMEMultipart()
    message['from'] = 'Admin Backend'
    message['to'] = email_to
    message['subject'] = 'Assunto Liga da Justiça'

    body = MIMEText(body_template, 'html')
    message.attach(body)
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('wag.backend@gmail.com', 'xxx')
            smtp.send_message(message)
            print('E-mail enviado com sucesso.')
        except Exception as e:
            print('E-mail não enviado...')
            print('Erro:', e)


send_mail('Superman', 'Clark', 'wag.backend@gmail.com')
