import json
import requests
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

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

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base, amount
