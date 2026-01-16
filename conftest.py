import pytest
from methods.user_methods import UserMethods

@pytest.fixture
def new_user():
    user_data = UserMethods().register_user()
    yield user_data


@pytest.fixture
def authorized_user():
    user_methods = UserMethods()
    user_data = user_methods.register_user()

    login_data = {
        "email": user_data["body"]["user"]["email"],
        "password": user_data["body"]["user"].get("password", "password123")
    }
    login_result = user_methods.login_user(login_data)
    token = login_result["body"].get("access_token") or login_result["body"].get("token")
    return token