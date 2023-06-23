import http.client
import os
from dotenv import load_dotenv
from web3 import Web3
load_dotenv()

api_key= os.environ.get('CryptoAPIs_API_KEY')

connection = http.client.HTTPConnection("https://rest.cryptoapis.io")
querystring = {"context":"SampleTX","limit":50,"offset":0}
headers = {
  'Content-Type': "application/json",
  'X-API-Key': api_key
}

connection.request("GET",
"blockchain-data,\
ethereum,\
mainnet,\
transactions,\
0xab9875572bd672c02a2d4ee00f6d9e20d3d4fffbc04e71ee72901ce8adf392f0,\
tokens-transfers",
headers=headers, 
params=querystring 
)

result = connection.getresponse()
data = result.read()

print(data.decode("utf-8"))
