from django.http import HttpResponse

<<<<<<< HEAD
from email_generator.utils import generator_email
=======
from email_generator.services import generator_email
>>>>>>> 0cf6499 (:dizzy: Add email-generator)


def email_generator(request, amount: int = 100):
    users_list = generator_email(amount=amount)
    formatted_users_list = [f"""<li>{user} {str(user).lower()}@mail.com</li>""" for user in users_list]
    new_users = ''.join(formatted_users_list)
    return HttpResponse(f'''<h1> New emails: {len(formatted_users_list)}</h1>
<ul>{new_users}</ul>''')
