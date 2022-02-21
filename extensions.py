import requests
import json

from config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = keys[base.lower()]
        except KeyError:
            return APIException(f'Валюта {base} не найдена!')
        try:
            sym_key = keys[sym.lower()]
        except KeyError:
            return APIException(f'Валюта {sym} не найдена!')
        if base_key == sym_key:
            return APIException(f'Невозможно перевести одинаковые валюты {base}!')
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            return APIException(f'Не удалось обработать количество {amount}!')

        query = "_".join([base_key, sym_key])
        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={query}&compact=ultra&apiKey=900e7d3d3bd73400b407')
        resp = json.loads(r.content)
        new_price = resp[query] * float(amount)
        return round(new_price, 2)
