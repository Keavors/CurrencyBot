import json
import requests
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException('Невозможно конвертировать одинаковые валюты.')

        if quote not in keys:
            raise APIException(f'Невозможно конвертировать валюту {quote}.')

        if base not in keys:
            raise APIException(f'Невозможно конвертировать валюту {base}.')

        try:
            amount = int(amount)
        except:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}')
        total_base = json.loads(r.content)[keys[quote]]
        return total_base, amount
