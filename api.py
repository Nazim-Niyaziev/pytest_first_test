import json
import requests

from requests_toolbelt.multipart.encoder import MultipartEncoder
from settings import api_key

'''Мой класс'''


class MoyClass:
    """апи библиотека к веб приложению Мой класс"""

    def __init__(self):
        self.base_url = "https://api.moyklass.com/"

    def get_token(self, auth_key) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным токеном пользователя"""
        api_key_in = {'apiKey': auth_key}
        res = requests.post(self.base_url + 'v1/company/auth/getToken', json=api_key_in)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def refresh_token(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с обновленным токеном пользователя"""
        res = requests.post(self.base_url + 'v1/company/auth/refreshToken', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_token(self, authorize):
        """Метод делает запрос к API сервера и возвращает статус запроса"""
        res = requests.post(self.base_url + 'v1/company/auth/revokeToken', headers=authorize)
        status = res.status_code
        return status

    def filials(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком филиалов"""
        res = requests.get(self.base_url + 'v1/company/filials', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def rooms(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком аудиторий"""
        res = requests.get(self.base_url + 'v1/company/rooms', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def managers(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком сотрудников"""
        res = requests.get(self.base_url + 'v1/company/managers', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def roles(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со
        списком ролей сотрудников"""
        res = requests.get(self.base_url + 'v1/company/roles', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def rates(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком аудиторий"""
        res = requests.get(self.base_url + 'v1/company/rates', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_manager(self, authorize, name: str, phone: str, email: str, filials: int, salaryFilialId: int,
                    roles: int, enabled: bool, password: str, additionalContacts: str, isStaff: bool,
                    isWork: bool, sendNotifies: bool, startDate: str, endDate: str,
                    contractNumber: str, contractDate: str, birthDate: str,
                    passportData: str, comment: str, color: str, rateId: int,
                    isOwner: bool) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом сотруднике и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного сотрудника"""

        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'filials': filials,
            'salaryFilialId': salaryFilialId,
            'roles': roles,
            'enabled': enabled,
            'password': password,
            'additionalContacts': additionalContacts,
            'isStaff': isStaff,
            'isWork': isWork,
            'sendNotifies': sendNotifies,
            'startDate': startDate,
            'endDate': endDate,
            'contractNumber': contractNumber,
            'contractDate': contractDate,
            'birthDate': birthDate,
            'passportData': passportData,
            'comment': comment,
            'color': color,
            'rateId': rateId,
            'isOwner': isOwner
        }
        res = requests.post(self.base_url + 'v1/company/managers', headers=authorize, json=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def courses(self, authorize, includeClasses: bool) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком аудиторий"""
        data = {'/includeClasses' : includeClasses}
        res = requests.get(self.base_url + 'v1/company/courses', headers=authorize, params=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def classes(self, authorize) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком аудиторий"""
        res = requests.get(self.base_url + 'v1/company/classes', headers=authorize)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


mc = MoyClass()
a = mc.get_token(api_key)
b = a[1]
auth = {'x-access-token': b['accessToken']}

print(mc.courses(auth, True))

