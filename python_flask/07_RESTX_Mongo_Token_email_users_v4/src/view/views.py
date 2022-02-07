from string import Template
from datetime import datetime

def welcome(login_user, name_user):
    with open ('src/template/template_welcome.html', 'r') as file:
        template = Template(file.read())
        date_now = datetime.now().strftime('%d/%m/%y')
        body_message = template.substitute(login=login_user , name=name_user, date=date_now)
        print(body_message)
        return body_message


# print(welcome('Superman', 'Clark'))