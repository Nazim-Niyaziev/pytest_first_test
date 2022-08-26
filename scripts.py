# import requests
# import json
#
#
# # res = requests.get(url, headers=headers, params=params) #пример
#
#
# # latitude = '55'
# # longitude = '37'
# # res = requests.get( "http://api.open-notify.org/iss-pass.json?lat="+latitude+"&lon="+longitude)
# # print(res.text)
#
# def get_api_key(email: str, passwd: str):
#     headers = {
#         'sorvanezz@gmail.com': email,
#         'Raty567': passwd,
#     }
#     res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
#     status = res.status_code
#     try:
#         result = res.json()
#     except json.decoder.JSONDecodeError:
#         result = res.text
#     return status, result
#
#
# print(get_api_key('sorvanezz@gmail.com', 'Raty567'))
#
# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
#
#
# # parent()
#
#
# def parent1(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#


# print(first())
# print(second())


# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# # Эту функцию мы будем декорировать
# def my_first_decorator():
#     print("Это мой первый декоратор!")


# my_first_decorator = my_decorator(my_first_decorator)

# my_first_decorator()

# from datetime import datetime
#
#
# def working_hours(func):
#     def wrapper():
#         if 9 <= datetime.now().hour < 13:
#             func()
#         else:
#             pass  # Нерабочее время, выходим
#
#     return wrapper
#
#
# def writing_tests():
#     print("Я пишу тесты на python!")
#
#
# writing_tests = working_hours(writing_tests)


# writing_tests()

# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# @my_decorator
# def my_first_decorator():
#     print("Это мой первый декоратор!")

# my_first_decorator()

# from decorators import debug


# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))


# @do_twice
# def test_twice_without_params():
#     print("Этот вызов без параметров")
#
#
# @do_twice
# def test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))


# @debug
# def age_passed(name, age=None):
#     if age is None:
#         return "Необходимо передать значение age"
#     else:
#         return "Аргументы по умолчанию заданы!"


# age_passed("Роман")
# age_passed("Роман", age=21)

# test_twice_without_params()
# test_twice_2_params("1", "2")
# test_twice("single")
from _datetime import datetime
import requests
import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


@pytest.fixture()
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": "sorvanezz@gmail.com", "pass": "Raty5678!!"})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')


def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


@pytest.fixture(scope="class", autouse=True)
def session_fixture():
    print("\nclass fixture starts")


@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("\nfunction fixture starts")


class TestClass23:

    def test_first(self):
        pass

    def test_second(self):
        pass


@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


def test_name(request):
    print("\n"+request.scope)

class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)


@pytest.fixture(scope="class")
def get_key(request):
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": "sorvanezz@gmail.com", "pass": "Raty5678!!"})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


class TestClassPets:

    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    def test_anotherTest(self):
        pass