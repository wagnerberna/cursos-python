from string import Template
from datetime import datetime


class view:
    def welcome(self, login_user, name_user):
        with open('src/template/template_welcome.html', 'r') as file:
            template = Template(file.read())
            date_now = datetime.now().strftime('%d/%m/%y')
            body_template = template.substitute(login=login_user, name=name_user, date=date_now)
            # print(body_template)
            return body_template


# view().welcome('Superman', 'Clark')
