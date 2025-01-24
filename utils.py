import json
import requests
from config import keys

class ConvertionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException('Невозможно конвертировать одинаковые валюты.')

        if quote not in keys:
            raise ConvertionException(f'Невозможно конвертировать валюту {quote}.')

        if base not in keys:
            raise ConvertionException(f'Невозможно конвертировать валюту {base}.')

        try:
            amount = int(amount)
        except:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base, amount
