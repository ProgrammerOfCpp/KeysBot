import requests

digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BITCOIN_API_URL = 'https://blockchain.info/ticker'


def get_latest_bitcoin_price(currency):
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json[currency]['last'])


def validate(bc):
    try:
        all(digits58.index(x) for x in bc)
        return len(bc) > 15
    except:
        return False

def eur_to_btc(value):
    return value / get_latest_bitcoin_price('EUR')