import random
import time
import uuid

class GenerateData:
        
    @staticmethod
    def generate_valid_user(prefix: str = "user") -> str:

        ts = int(time.time() * 1000)
        uid = uuid.uuid4().hex[:6]

        return {
            "email": f"{prefix}.{ts}.{uid}@example.test",
            "password": "password123",
            "name": "TestUser"
        }
    
    @staticmethod
    def buferize_user(user_data):
        return {
            "email": user_data["email"],
            "password": "password123",
            "name": "TestUser"
        }
    
    @staticmethod
    def non_exist_account():
        return {
            "email": f"nonexist{random.randint(1000, 9999)}@mail.ru",
            "password": "wrongpassword"
        }

    @staticmethod
    def _format_response(response):
        return {"status_code": response.status_code, "body": response.json()}