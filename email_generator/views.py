from django.http import HttpResponse

from email_generator.services import emails_generator


def email_generator(amount: int = 5):
    email_list = emails_generator(amount)
    formatted_users_list = [f"""<li>{user} {str(user).lower()}@mail.com</li>""" for user in email_list]
    new_users = ''.join(formatted_users_list)
    return HttpResponse(f'''<h1> New emails: {len(formatted_users_list)}</h1>
<ul>{new_users}</ul>''')
