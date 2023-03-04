import requests as rq

print('connecting to CoinGecko')
ping = rq.get('https://api.coingecko.com/api/v3/ping').json()['gecko_says']
print(f'connected, gecko says: {ping}')