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


def fields(start):
    """
    Назначение функции: получить значение для параметра field
    :return: словарь
    """
    pk = start
    while True:
        field = {
        "fields": {
        "title": get_title(),
        "year": get_year(),
        "pages": get_pages(),
        "isbn13": get_isbn13(faker),
        "rating": get_rating(),
        "price": get_price(),
        "author": get_author()
        }
        }
        yield field
        pk += 1


def gen_dict(start):
    """Генератор для получение словарей"""
    while True:
        dict_ = {
            "model": MODEL,
            "pk": start,
            "fields": fields(start)
        }
        yield dict_


def to_json_dict(data: list):
    """ Функция серилизует в Json строку"""
    with open("book.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def main():
    """Запускает функцию-генератор"""
    gen = fields(3)
    data = [next(gen) for _ in range(100)]
    to_json_dict(data)


if __name__ == "__main__":
    main()







