import requests
import allure
from requests_toolbelt.multipart.encoder import MultipartEncoder
from data.test_data import TestData

class AdMethods:
    CREATE_ENDPOINT = f"{TestData.BASE_URL}api/create-listing"
    UPDATE_ENDPOINT = f"{TestData.BASE_URL}api/update-offer"
    DELETE_ENDPOINT = f"{TestData.BASE_URL}api/listings"

    @allure.step("Создание объявления")
    def create_ad(self, token, ad_data, image_path=None):
        fields = {k: str(v) for k, v in ad_data.items()}
        if image_path:
            fields["img1"] = ("image.jpg", open(image_path, "rb"), "image/jpeg")
        
        m = MultipartEncoder(fields=fields)

        token_str = self._extract_token(token)
        headers = {
            "Authorization": f"Bearer {token_str}",
            "Content-Type": m.content_type
        }
        response = requests.post(
            self.CREATE_ENDPOINT,
            headers=headers,
            data=m
        )
        return {"status_code": response.status_code, "body": response.json()}

    @allure.step("Редактирование объявления")
    def edit_ad(self, token, ad_id, update_data, image_path=None):
        token_str = self._extract_token(token)
        
        # Always use multipart for this API
        fields = {k: str(v) for k, v in update_data.items()}
        if image_path:
            fields["img2"] = ("image.jpg", open(image_path, "rb"), "image/jpeg")
        
        m = MultipartEncoder(fields=fields)
        headers = {
            "Authorization": f"Bearer {token_str}",
            "Content-Type": m.content_type
        }
        response = requests.patch(
            f"{self.UPDATE_ENDPOINT}/{ad_id}",
            headers=headers,
            data=m
        )
        
        return {"status_code": response.status_code, "body": response.json()}

    @allure.step("Удаление объявления")
    def delete_ad(self, token, ad_id):
        token_str = self._extract_token(token)
        headers = {
            "Authorization": f"Bearer {token_str}"
        }
        response = requests.delete(
            f"{self.DELETE_ENDPOINT}/{ad_id}",
            headers=headers
        )
        return {"status_code": response.status_code}

    @staticmethod
    def _extract_token(token):
        if isinstance(token, dict):
            return token.get("access_token") or token.get("token")
        return token