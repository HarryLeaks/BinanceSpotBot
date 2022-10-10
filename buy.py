#api_key: YT8VGPjyScUAF56DmrFqfX5UGqhkaQ6jT2NIQ36I5LFRWWUZnBFnqsgQCLZND972
#Secret Key: 8eHOJhvt0sDIJjEZlFjWthPZen4AcEooSVTZpQELxWaOSkDAcKFWu9vGvQ7CR1Zk

'''
https://testnet.binance.vision/api
wss://testnet.binance.vision/ws
wss://testnet.binance.vision/stream
'''

from binance import Client

api_key ='mlbyYC18uW1Sdhz08BVZZ6HS0NMmMPTTJOZhjT4ydhsmBm9MkiYgsT4zpg37BN9x'
api_secret = 'osSYGdhFvUEd8qNIqpsLHXCBHf6zglNyxXHpSkVsQKEzasLw2y0pwrg5muk4jUEC'

client = Client(api_key, api_secret, testnet=True)

client.API_URL = 'https://testnet.binance.vision/api'

print(client.get_asset_balance(asset='USDT'))
print(client.get_asset_balance(asset='BTC'))

# Create test order
buy = client.order_market_buy(
        symbol='BTCUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quoteOrderQty=float(client.get_asset_balance(asset='USDT')['free'])
    )