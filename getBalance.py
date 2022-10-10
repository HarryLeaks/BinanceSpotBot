#api_key: YT8VGPjyScUAF56DmrFqfX5UGqhkaQ6jT2NIQ36I5LFRWWUZnBFnqsgQCLZND972
#Secret Key: 8eHOJhvt0sDIJjEZlFjWthPZen4AcEooSVTZpQELxWaOSkDAcKFWu9vGvQ7CR1Zk

'''
https://testnet.binance.vision/api
wss://testnet.binance.vision/ws
wss://testnet.binance.vision/stream
'''

from binance import Client

api_key ='AsDJhZrqP3TOcvyNTCH9dmik4KMtUJWFSbSdCbiTZU0e2vxYBp5LbyIu66hPAUIQ'
api_secret = 'pRrYJsugEU7QAY9X9iUlFzKGRHmnNvmIrfR9md8Fp1drUf06jQwp57hwFBULJNV4'

client = Client(api_key, api_secret)

print(client.get_asset_balance(asset='USDT'))
print(client.get_asset_balance(asset='BTC'))
