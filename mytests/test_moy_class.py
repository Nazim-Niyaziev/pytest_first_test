# from api import auth, mc
# from settings import api_key
#
#
# # GETTOKEN
#
# def test_get_token_for_valid_user():
#     """Проверяем что запрос токена возвращает статус 200 и результат - уникальный токен"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.get_token(api_key)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert 'accessToken' in result
#
#
# # REFRESHTOKEN
#
# def test_refresh_token_for_valid_user():
#     """Проверяем что запрос возвращает статус 200 и результат - обновленный токен"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.refresh_token(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert 'accessToken' in result
#
#
# # DELETETOKEN
#
# def test_delete_token_for_valid_user():
#     """Проверяем что запрос возвращает статус 204"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
#     status = mc.delete_token(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 204
#
#
# # GETFILIALS
#
# def test_filials():
#     """Проверяем что запрос возвращает статус 200 и список филиалов в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.filials(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # GETROOMS
#
# def test_rooms():
#     """Проверяем что запрос возвращает статус 200 и список аудиторий в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.filials(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # GETMANAGERS
#
# def test_managers():
#     """Проверяем что запрос возвращает статус 200 и список сотрудников в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.managers(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # ADDMANAGER - ЭТОТ ТЕСТ-КЕЙС НЕ РАБОТАЕТ ИЗ-ЗА БАГА !
#
# def test_add_managers():
#     """Проверяем что запрос возвращает статус 200 и информацию о добавленном сотруднике в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.add_manager(auth, 'Смолин Петр Михайлович', '9001234567', 'ivanov@site.com', 0, 0, 0, True,
#                                     'qdbqkwjbd12',
#                                     'string', False, True, True, '2011-06-12T00:00:00.000Z', '2019-06-12T00:00:00.000Z',
#                                     '№12445 от 2019г', '2013-06-12T00:00:00.000Z',
#                                     '2014-06-12T00:00:00.000Z', 'ss', 'OK', '#222fff', 22, True)
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # GETROLES
#
#
# def test_roles():
#     """Проверяем что запрос возвращает статус 200 и список ролей сотрудников в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.roles(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # GETRATES
#
#
# def test_rates():
#     """Проверяем что запрос возвращает статус 200 и список ставок сотрудников в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.roles(auth)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # GETCOURSES
#
#
# def test_courses():
#     """Проверяем что запрос возвращает статус 200 и список программ обучения в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.courses(auth, True)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None
#
#
# # GETCLASSES
#
#
# def test_classes():
#     """Проверяем что запрос возвращает статус 200 и список групп (наборов) в формате json"""
#
#     # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
#     status, result = mc.classes(auth, True)
#
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 200
#     assert result is not None