from django.http import HttpResponse

from email_generator.services import users_generator


def emails_generator(request, amount: int = 100):
    user_as_list = users_generator(amount)
    new_users = ''.join(f'''<li>{user.name} {user.email}</li>''' for user in user_as_list)
    return HttpResponse(f'''<h1> New emails: {new_users.count('@')} </h1>
<ul>{new_users}</ul>''')
