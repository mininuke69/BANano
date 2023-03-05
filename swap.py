import requests as rq


endpoint = 'https://api.coingecko.com/api/v3'

print('connecting to CoinGecko...')
ping = rq.get(f'{endpoint}/ping').json()['gecko_says']
print(f'connected, gecko says: {ping}')

price_list = rq.get(f'{endpoint}/simple/price?ids=banano%2Cnano&vs_currencies=sat%2C&precision=18').json()

print(price_list)

price_xno_usd = price_list['nano']['usd']
price_xno_sat = price_list['nano']['sat']
price_ban_usd = price_list['banano']['usd']
price_ban_sat = price_list['banano']['sat']


