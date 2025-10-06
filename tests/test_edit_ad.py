import pytest
from methods.Ad_methods import AdMethods
from methods.user_methods import UserMethods
from data.test_data import TestData


def test_edit_ad_success(authorized_user):
    ad_methods = AdMethods()
    ad_data = TestData.DEFAULT_AD_DATA.copy()
    create_result = ad_methods.create_ad(authorized_user, ad_data)
    ad_id = create_result["body"]["id"]
    
    update_data = {
        "name": "Updated Ad Name",
        "price": 777,
        "description": "Updated description",
        "category": "Хобби",
        "condition": "Б/У",
        "city": "Санкт-Петербург"
    }
    edit_result = ad_methods.edit_ad(authorized_user, ad_id, update_data)
    
    assert edit_result["status_code"] == TestData.EDIT_AD_SUCCESS_STATUS
    assert edit_result["body"]["id"] == ad_id
    assert edit_result["body"]["name"] == update_data["name"]
    assert edit_result["body"]["price"] == update_data["price"]
    assert edit_result["body"]["description"] == update_data["description"]
    assert edit_result["body"]["category"] == update_data["category"]
    assert edit_result["body"]["city"] == update_data["city"]


def test_edit_ad_by_another_user(authorized_user):
    ad_methods = AdMethods()
    user_methods = UserMethods()
    
    ad_data = TestData.DEFAULT_AD_DATA.copy()
    create_result = ad_methods.create_ad(authorized_user, ad_data)
    ad_id = create_result["body"]["id"]
    
    second_user = user_methods.register_user()
    login_data = {
        "email": second_user["body"]["user"]["email"],
        "password": second_user["body"]["user"].get("password", "password123")
    }
    login_result = user_methods.login_user(login_data)
    second_token = login_result["body"].get("access_token") or login_result["body"].get("token")
    
    update_data = {
        "name": "Hacked Ad Name",
        "price": 1,
        "category": ad_data["category"],
        "condition": ad_data["condition"],
        "city": ad_data["city"],
        "description": "Hacked"
    }
    edit_result = ad_methods.edit_ad(second_token, ad_id, update_data)
    
    assert edit_result["status_code"] == TestData.EDIT_AD_FORBIDDEN_STATUS
