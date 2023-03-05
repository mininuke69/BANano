import requests as rq
from json import load
import bananopie



gecko_endpoint = 'https://api.coingecko.com/api/v3'
ban_node_endpoint = 'https://kaliumapi.appditto.com/api'
xno_node_endpoint = 'https://mynano.ninja/api/node'

wallets_file = open('accounts.txt', 'r')
wallets = load(wallets_file)

ban_seed = wallets['ban']['seed']
ban_address = wallets['ban']['address']
xno_seed = wallets['xno']['seed']
xno_address = wallets['xno']['address']

bal_ban = None
bal_xno = None
receivable_ban = None
receivable_xno = None

def Update_Balance():
    global bal_ban
    global bal_xno
    global receivable_ban
    global receivable_xno

    ban_json = {
                "action": "account_balance",
                "account": ban_address,
                }
    bal_ban_request = rq.post(ban_node_endpoint, json=ban_json).json()
    bal_ban = bal_ban_request['balance_decimal']
    receivable_ban = bal_ban_request['receivable_decimal']


def Receive():
    if receivable_ban > 0:
        ban_json = None






print('connecting to CoinGecko...')
ping = rq.get(f'{gecko_endpoint}/ping').json()['gecko_says']
print(f'connected, gecko says: {ping}')

#price_list = rq.get(f'{gecko_endpoint}/simple/price?ids=banano%2Cnano&vs_currencies=usd&precision=18').json()
price_list = {'banano': {'usd': 0.004928284617909525}, 'nano': {'usd': 0.8635332214522783}} #temporary solution to reduce api calls


price_xno_usd = price_list['nano']['usd']
price_ban_usd = price_list['banano']['usd']

ban_to_xno = price_ban_usd / price_xno_usd
xno_to_ban = price_xno_usd / price_ban_usd

Update_Balance()
print(bal_ban)