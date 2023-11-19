import re


def validate_name(name):
    if re.match(r'^\d+$', name):
        raise ValueError('В названии должны быть буквы')


def validate_price(price):
    try:
        float(price)
    except ValueError:
        raise ValueError('Цена дожна быть цифрами')


def validate_quantity(quantity):
    try:
        int(quantity)
    except ValueError:
        raise ValueError('Колличество дожно быть цифрами')
