#!/usr/bin/env python3

import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "eur"
}

data = requests.get(url, params=params).json()

btc_price = data["bitcoin"]["eur"]
eth_price = data["ethereum"]["eur"]

print(f"BTC price: € {btc_price}")
print(f"ETH price: € {eth_price}")
