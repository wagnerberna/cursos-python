import smtplib
import email.message

# import os
# from pathlib import Path
# from dotenv import dotenv_values

# Get the base directory
# basepath = Path()
# basedir = str(basepath.cwd())
# # Load the environment variables
# envars = basepath.cwd() / 'mail.env'
# dotenv_values(envars)
# # Read an environment variable.
# SECRET_KEY = os.getenv('EMAIL')
# print(SECRET_KEY)


# dotenv = load_dotenv()

# EMAIL = os.getenv('EMAIL')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


def enviar_email():
    corpo_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'xxx@gmail.com'
    msg['To'] = 'xxx@gmail.com'
    password = 'xxxx'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login('cabelo29007', password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email()
