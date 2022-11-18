from pycoingecko import CoinGeckoAPI
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

# ------------------ coin gecko api ----------------- #
cg = CoinGeckoAPI()

btc = cg.get_price(ids="bitcoin, ethereum", vs_currencies="usd")
print(btc)
price_btc = btc['bitcoin']['usd']
price_eth = btc['ethereum']['usd']

# -------- get url from push ---------- #
url = "http://www.pushsafer.com/api"

# ------------ data for parameters  ----------------- #
k = "ZolWXW46gZqQQjru9Gj7"
d = 56169
t = "BTC and Eth Price"
m = f"BTC price: {price_btc}\nEth price: {price_eth}"
v = 3

# ---------- parameters ------------ #
data = {
    "k": k,
    "d": d,
    "t": t,
    "m": m,
    "v": v,
}

# ------------- request ---------------- #
r = Request(url, urlencode(data).encode())
json = urlopen(r).read().decode()
print(json)


