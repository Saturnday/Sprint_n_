import pytest
from methods.user_methods import UserMethods
from data.test_data import TestData


def test_successful_login():
    user_methods = UserMethods()
    reg_result = user_methods.register_user()
    user_info = user_methods.buferize_user(reg_result["body"]["user"])

    login_data = {
        "email": user_info["email"],
        "password": user_info["password"]
    }
    login_result = user_methods.login_user(login_data)

    assert login_result["status_code"] == TestData.LOGIN_SUCCESS_STATUS
    assert "access_token" in login_result["body"]["token"]
