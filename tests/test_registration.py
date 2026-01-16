from methods.user_methods import UserMethods
from data.test_data import TestData


def test_register_user():
    user_methods = UserMethods()
    result = user_methods.register_user()
    assert "id" in result["body"]["user"]
    assert result["status_code"] == TestData.REGISTRATION_SUCCESS_STATUS


def test_duplicate_registration():
    user_methods = UserMethods()
    first_result = user_methods.register_user()
    user_info = user_methods.buferize_user(first_result["body"]["user"])
    status_code = user_methods.register_user_with_email(user_info["email"], user_info["password"], user_info["name"])["status_code"]
    assert status_code == TestData.REGISTRATION_DUPLICATE_STATUS

