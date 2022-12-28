from tkinter import *
from tkinter import messagebox
from binance import Client
import binance
from functools import partial
import time

import logging.config
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

client = None

def nextWin():
	bought = False
	numberTrades = 0
	while True:
		btcusdt_trades = client.get_my_trades(symbol='BTCUSDT', limit=1)
		if btcusdt_trades[0]['symbol'] == 'BTCUSDT' and btcusdt_trades[0]['isBuyer'] == False and bought == True and float(client.get_asset_balance(asset='BTC')['locked']) == 0:
			print("SOLD")
			numberTrades += 1
			print("number of trades: ", numberTrades)
			bought = False
		if btcusdt_trades[0]['symbol'] == 'BTCUSDT' and bought == False and btcusdt_trades[0]['isBuyer'] == True and float(client.get_asset_balance(asset='USDT')['locked']) == 0 and float(client.get_asset_balance(asset='BTC')['free']) != 0 and float(client.get_asset_balance(asset='BTC')['locked']) == 0:
			bought = True
			print("")
			buy_price = btcusdt_trades[0]['price']
			print("buy price:", buy_price)
			sell_price = float(buy_price) + 1
			print("sell price:", sell_price)
			quantity = client.get_asset_balance(asset='BTC')['free']
			splited = quantity.split('.')
			decimal = splited[1][0:5]
			quantity = splited[0]+'.'+decimal
			print(quantity)
			client.create_order(symbol="BTCUSDT", side='SELL', type='LIMIT', quantity=quantity, price=sell_price, timeInForce='GTC')
		time.sleep(0.5)

def validate(apikey, apisecret):
	global tkWindow
	global client
	try:
		client = Client(apikey.get(), apisecret.get())
		client.get_account()
		client.ping()
		tkWindow.destroy()
	except binance.exceptions.BinanceAPIException as e:
		messagebox.showwarning(title='Connection error', message='Coud not connect to the server')
		client.close_connection()
		exit()
	nextWin()

#window
tkWindow = Tk()  
tkWindow.geometry('400x120')  
tkWindow.title('Bot v1.0')

Label(tkWindow, text="            ").grid(row=0,column=0)

ApiKeyLabel = Label(tkWindow, text="Api Key").grid(row=0, column=1)
ApiKey = StringVar()
ApiKeyEntry = Entry(tkWindow, textvariable=ApiKey).grid(row=0, column=2)  

ApiSecretLabel = Label(tkWindow,text="Api Secret").grid(row=1, column=1)  
ApiSecret = StringVar()
ApiSecretEntry = Entry(tkWindow, textvariable=ApiSecret).grid(row=1, column=2)  

validate = partial(validate, ApiKey, ApiSecret)

#login button
loginButton = Button(tkWindow, text="Login", command=validate).grid(row=3, column=2)  

tkWindow.mainloop()