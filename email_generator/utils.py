from faker import Faker

fake = Faker()


def generator_email(amount: int) -> list:
    return list({fake.unique.first_name() for _ in range(amount)})
