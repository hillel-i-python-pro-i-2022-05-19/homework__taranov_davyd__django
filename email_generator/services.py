from collections import namedtuple

from email_generator.utils import generator_name


def one_email_generator(amount: int = 1):
    users_list = generator_name(amount)
    Name = namedtuple("Name", "name")
    formatted_users_list = Name([f"""{user} {str(user).lower()}@mail.com """ for user in users_list])
    return formatted_users_list


def emails_generator(amount: int):
    email_list = generator_name(amount)
    formatted_users_list = yield [f"""<li>{user} {str(user).lower()}@mail.com</li>""" for user in email_list]
    new_users = ''.join(formatted_users_list)
