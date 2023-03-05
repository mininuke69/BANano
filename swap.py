import requests as rq


endpoint = 'https://api.coingecko.com/api/v3'

print('connecting to CoinGecko...')
ping = rq.get(f'{endpoint}/ping').json()['gecko_says']
print(f'connected, gecko says: {ping}')

#price_list = rq.get(f'{endpoint}/simple/price?ids=banano%2Cnano&vs_currencies=usd&precision=18').json()
price_list = {'banano': {'usd': 0.004928284617909525}, 'nano': {'usd': 0.8635332214522783}} #temporary solution to reduce api calls


price_xno_usd = price_list['nano']['usd']
price_ban_usd = price_list['banano']['usd']

ban_to_xno = price_ban_usd / price_xno_usd
xno_to_ban = price_xno_usd / price_ban_usd
