import requests

def get_price(crypto_name):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_name,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        price = data[crypto_name]['usd']
        return f'[INFO] Текущий курс криптовалюты({crypto_name.upper()}) ${price}'
    else:
        return "[ERROR] Неверные данные криптовалюты"
    
if __name__ == "__main__":


    try:
        while True:
            crypto_name = input("Введите название криптовалюты:").lower()
            result = get_price(crypto_name)


            print(result)
    except KeyboardInterrupt:
        print("Вы отменили операцию!")
    except KeyError:
        print("Неверная криптовалюта!")

