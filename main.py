# pulls data from coingecko (BTC,ETH in USD/CAD) and outputs to pysimplegui display
import time
import requests
import json
import PySimpleGUI as sg


def btcusd():
    t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').text
    # print(type(t))#str
    t = json.loads(t)
    btc_price_usd = t['bitcoin']['usd']  # converts to int
    # print(type(t))#dict
    # print(btcprice)#int
    time.sleep(1)
    return btc_price_usd


def btccad():
    t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=cad').text
    # print(type(t))#str
    t = json.loads(t)
    btc_price_cad = t['bitcoin']['cad']  # converts to int
    # print(type(t))#dict
    # print(btcprice)#int
    time.sleep(1)
    return btc_price_cad


def ethusd():
    t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').text
    # print(type(t))#str
    t = json.loads(t)
    eth_price_usd = round(t['ethereum']['usd'])  # converts to int
    # print(type(t))#dict
    # print(btcprice)#int
    time.sleep(1)
    return eth_price_usd


def ethcad():
    t = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=cad').text
    # print(type(t))#str
    t = json.loads(t)
    eth_price_cad = round(t['ethereum']['cad'])  # converts to int
    # print(type(t))#dict
    # print(btcprice)#int
    time.sleep(1)
    return eth_price_cad


def ratio():
    btc_eth_ratio = btcusd() / ethusd()
    time.sleep(1)
    return round(btc_eth_ratio, 3)


sg.theme('black')
layout = [
    [sg.T('BITCOIN USD', text_color='yellow'), sg.T(key='-btcusd-', text_color='#ffff35')],
    [sg.T('BITCOIN CAD', text_color='yellow'), sg.T(key='-btccad-', text_color='#ffff35')],
    [sg.T('ETHEREUM USD', text_color='green'), sg.T(key='-ethusd-', text_color='#00AD1D')],
    [sg.T('ETHEREUM CAD', text_color='green'), sg.T(key='-ethcad-', text_color='#00AD1D')],
    [sg.T('BTC/ETH RATIO'), sg.T(key='-btcethratio-')],
]

window = sg.Window('CRYPTO PRICE', layout, finalize=True)

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    window['-btcethratio-'].update(ratio())
    window['-btcusd-'].update(btcusd())
    window['-btccad-'].update(btccad())
    window['-ethusd-'].update(ethusd())
    window['-ethcad-'].update(ethcad())
    time.sleep(1)
window.close()
