from dotenv import load_dotenv
load_dotenv()
import os
import requests
axie_url = "https://api.opensea.io/api/v1/collection/axie"
ice_poker_url ="https://api.opensea.io/api/v1/collection/decentral-games-ice"
coinmarketcap_url ="https://pro-api.coinmarketcap.com/v2/tools/price-conversion"


def CoinMarketCap_API(url,symbol):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('X-CMC_PRO_API_KEY') ,
            }
    parameters = { "amount": 1, "symbol": symbol, "convert" : "USD"}
    json= requests.get(url,params=parameters, headers=headers).json()
    return json

def OpenSea_API(url):
    json= requests.get(url).json()
    return json

'''axie_json=OpenSea_API(axie_url)
print(axie_json["collection"]["stats"]["floor_price"])
print(axie_json["collection"]["primary_asset_contracts"][0]["address"])'''

Ice_poker_json=OpenSea_API(ice_poker_url)
print(CoinMarketCap_API(coinmarketcap_url, "ICE")["data"][0]["quote"]["USD"]["price"])
"""BTC_json= CoinMarketCap_API(coinmarketcap_url, "ICE")

print(BTC_json)
print(Ice_poker_json["collection"]["stats"]["floor_price"])
print(Ice_poker_json["collection"]["primary_asset_contracts"][0]["address"])
print(Ice_poker_json["collection"]["image_url"])
print(Ice_poker_json["collection"]["telegram_url"])
print("https://twitter.com/"+Ice_poker_json["collection"]["twitter_username"])
print(Ice_poker_json["collection"]["discord_url"])"""


