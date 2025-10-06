import requests
from data.test_data import TestData
from helpers.helpers import GenerateData
import allure


class UserMethods:

    @allure.step("Регистрация пользователя")
    def register_user(self, user_data=None):
        data = user_data if user_data else GenerateData.generate_valid_user()
        response = requests.post(f"{TestData.BASE_URL}/api/signup", json=data)
        return GenerateData._format_response(response)
    
    @allure.step("Регистрация пользователя с указанным email")
    def register_user_with_email(self, email, password=None, name=None):
        data = {
            "email": email,
            "password": password if password else TestData.DEFAULT_PASSWORD,
            "name": name if name else "TestUser"
        }
        response = requests.post(f"{TestData.BASE_URL}/api/signup", json=data)
        return GenerateData._format_response(response)

    @allure.step("Проверка повторной регистрации пользователя")
    def is_duplicate_registration(self, email, password, name):
        result = self.register_user_with_email(email, password, name)
        return result["status_code"] == 400
    
    @allure.step('Буферизация пользователя')
    def buferize_user(self, user_data):
        return GenerateData.buferize_user(user_data)

    @allure.step("Логин")
    def login_user(self, user_data):
        response = requests.post(f"{TestData.BASE_URL}/api/signin", json=user_data)
        return GenerateData._format_response(response)

    @allure.step("Обновить информацию о пользователе")
    def update_user(self, token, update_data):
        headers = {"Authorization": token}
        response = requests.patch(f"{TestData.BASE_URL}/user", headers=headers, json=update_data)
        return {"status_code": response.status_code, "body": response.json()}
