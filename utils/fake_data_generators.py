from faker import Faker


def get_fake_name():
    fake_name = Faker().first_name()
    return fake_name


def get_fake_description():
    fake_body = Faker().text()
    return fake_body
