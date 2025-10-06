import pytest
from methods.Ad_methods import AdMethods
from data.test_data import TestData


def test_delete_ad_success(authorized_user):
    ad_methods = AdMethods()
    ad_data = TestData.DEFAULT_AD_DATA.copy()
    create_result = ad_methods.create_ad(authorized_user, ad_data)
    ad_id = create_result["body"]["id"]
    
    delete_result = ad_methods.delete_ad(authorized_user, ad_id)
    
    assert delete_result["status_code"] == TestData.DELETE_AD_STATUS
