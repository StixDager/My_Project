import requests
import json
from config import CURRENCIES

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> float:
        if base == quote:
            raise APIException(f'Нельзя перевести одинаковые валюты: {base}')
        
        try:
            base_ticker = CURRENCIES[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        
        try:
            quote_ticker = CURRENCIES[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        
        url = f"https://open.er-api.com/v6/latest/{base_ticker}"
        response = requests.get(url)
        data = response.json()

        if data.get("result") != "success":
            raise APIException("Ошибка при получении данных от API.")
        
        try:
            rate = data["rates"][quote_ticker]  # 🟢 исправлено здесь
        except KeyError:
            raise APIException(f"Не удалось получить курс для валюты: {quote}")
        
        return rate * amount
