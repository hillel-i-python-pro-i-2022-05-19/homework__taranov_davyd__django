from faker import Faker

fake = Faker()


def generator_name():
    return fake.unique.first_name()


def generator_email():
    return fake.unique.ascii_email()
