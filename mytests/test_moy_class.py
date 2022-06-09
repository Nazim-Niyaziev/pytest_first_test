from api import MoyClass
from settings import api_key

pf = MoyClass()


def test_get_token_for_valid_user(apiKey=api_key):
    """ Проверяем что запрос токена возвращает статус 200 и результат валидный"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_token(apiKey)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'accessToken' in result
