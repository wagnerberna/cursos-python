from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# import os
# from dotenv import load_dotenv

from string import Template
from datetime import datetime

# dotenv = load_dotenv()


# EMAIL = os.getenv('EMAIL')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


def welcome(login_user, name_user):
    with open('src/template/template_welcome.html', 'r') as file:
        template = Template(file.read())
        date_now = datetime.now().strftime('%d/%m/%y')
        body_message = template.substitute(login=login_user, name=name_user, date=date_now)
        print(body_message)
        # return body_message

    message = MIMEMultipart()
    message['from'] = 'Admin Backend'
    message['to'] = 'xxx@gmail.com'
    message['subject'] = 'Assunto Liga da Justiça'

    body = MIMEText(body_message, 'html')
    message.attach(body)

    # ENVIO DE IMAGEM EM ANEXO
    # with open('ljs2.jpg', 'rb') as img:
    #   image = MIMEImage(img.read())
    #   message.attach(img)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('xxx@gmail.com', 'xxx')
            smtp.send_message(message)
            print('E-mail enviado com sucesso.')
        except Exception as e:
            print('E-mail não enviado...')
            print('Erro:', e)


welcome('Superman', 'Clark')
