import requests
import json

from config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException(f"Невозможно перевести одинаковые валюты {quote} в {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")



        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={keys[base]}&symbols='
                         f'{keys[quote]}')
        rate='rates'
        total_base = json.loads(r.content)[rate][keys[quote]]*amount
        return total_base

