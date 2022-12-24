import json
import random
from faker import Faker
from conf import MODEL


faker = Faker("ru")


def get_title():
    """ Получаем случайную строку с названием книги """
    filename = "books.txt"
    with open(filename, encoding="utf-8") as f:
        data = f.readlines()
    return random.choice(data)


def get_year():
    """ Получаем случайный год написания книги"""
    year = random.randint(1979, 2020)
    return round(year)


def get_pages():
    """ Получаем случайное колицество страниц """
    page = random.randint(200, 658)
    return round(page)


def get_isbn13(faker):
    """
    Назначение функции: получить международный книжный номер
    :param faker: берем из библиотеки
    :return: случайный международный книжный номер
    """
    return faker.isbn13()


def get_rating():
    """
    Назначение функции: получить значение для параметра rating
    :return: число с плавающей запятой от 0 до 5
    """
    rating = random.uniform(0, 5)
    return round(rating, 3)


def get_price():
    """ Получаем случайную цену книги"""
    price = random.uniform(1, 10000)
    return round(price, 1)


def get_author():
    """ Получаем фамилию и имя случайного автора"""
    return [" ".join((faker.first_name_female(), faker.last_name())) for _ in range(random.randint(1, 3))]


def get_model():
    """ Извлекает данные для параметра model"""
    filename_ = "conf.py"
    with open(filename_) as f:
        data = MODEL
        return data


def fields() -> dict:
    """
    Назначение функции: получить значение для параметра field
    :return: словарь
    """
    return {
        "model": get_model(),
        "pk": 1, # не могу вспомнить как сделать так, чтоб с каждым разом увеличивалось на 1. Здесь вроде бы никак. а как вписать этот параметр в функцию генератор - не пойму
        "fields": {
        "title": get_title(),
        "year": get_year(),
        "pages": get_pages(),
        "isbn13": get_isbn13(faker),
        "rating": get_rating(),
        "price": get_price(),
        "author": [
            get_author()
        ]
        }
    }


def to_json_dict(field):
    """ Функция серилизует в Json строку"""
    json_dict = json.dumps(field)
    return json_dict


if __name__ == "__main__": # не пойму куда поставить \n, чтобы каждое значение было на отдельной строке
    json_dict = {
        "model": get_model(),
        "pk": 1,
        "fields": {
            "title": get_title(),
            "year": get_year(),
            "pages": get_pages(),
            "isbn13": get_isbn13(faker),
            "rating": get_rating(),
            "price": get_price(),
            "author": [
                get_author()
            ]
        }
    }
    print(json_dict)


# не пойму как во все это вписать функцию генератор




