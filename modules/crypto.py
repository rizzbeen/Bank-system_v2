import json
import requests
from modules.function import black, red, green, yellow, blue, magenta, cyan, white, create_pin, ask_pin, save_json, read_json, generate_userid
import time
import colorama


#coin
def top5_coin():
    url = "https://api.coinranking.com/v2"
    url_data = f"{url}/coins?limit=5"
    response = requests.get(url_data)
    data = response.json()

    coins = data["data"]["coins"]

    for i, coin in enumerate(coins, 1):
        price = f'${float(coin["price"]):.2f}'
        print(f'\n{red(i)}. {yellow(coin["name"])} ({coin["symbol"]}):  {green(price)}')

#search

def search_coin(name):
      url = "https://api.coinranking.com/v2"
      search_data = f'{url}/coins?search={name}'
      response = requests.get(search_data)
      data = response.json()
    
      coins = data["data"]["coins"]

      if not coins:
       print("COIN NOT FOUND")
      else:
        result = coins[0]
        price = f'${float(result["price"]):.2f}'
        print(f'\n{yellow(result["name"])} ({result["symbol"]}):  {green(price)}')



