class TestData:

    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

    REGISTRATION_SUCCESS_STATUS = 201
    REGISTRATION_DUPLICATE_STATUS = 400

    LOGIN_SUCCESS_STATUS = 201

    CREATE_AD_STATUS = 201
    EDIT_AD_SUCCESS_STATUS = 200
    DELETE_AD_STATUS = 200

    EDIT_AD_FORBIDDEN_STATUS = 403

    DEFAULT_PASSWORD = "Password123!"

    CATEGORIES = ["Авто", "Книги", "Садоводство", "Хобби", "Технологии"]

    DEFAULT_AD_DATA = {
        "name": "Name of the ad",
        "category": "Авто",
        "condition": "Новый",
        "city": "Москва",
        "description": "Description of the ad",
        "price": 999
    }
