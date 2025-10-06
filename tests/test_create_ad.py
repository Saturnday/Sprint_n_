import pytest
from methods.Ad_methods import AdMethods
from data.test_data import TestData

@pytest.mark.parametrize("category", TestData.CATEGORIES)
def test_create_ad_in_any_category(authorized_user, category):
    ad_methods = AdMethods()
    ad_data = TestData.DEFAULT_AD_DATA.copy()
    ad_data["category"] = category
    
    result = ad_methods.create_ad(authorized_user, ad_data)
    assert result["status_code"] == TestData.CREATE_AD_STATUS
    assert "id" in result["body"]
    assert result["body"]["name"] == ad_data["name"]
    assert result["body"]["category"] == category