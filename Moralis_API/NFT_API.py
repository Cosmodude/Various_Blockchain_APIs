### https://docs.moralis.io/web3-data-api/reference/get-nft-lowest-price

from moralis import evm_api
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

api_key = os.environ.get('Moralis_API_key')
params = {
    "address": "0x6CC462bc49ceCFE943Bc4F477b23b92906e6074F", 
    "chain": "eth", 
    "days": 25, 
    
}


result = evm_api.nft.get_nft_lowest_price(
    api_key=api_key,
    params=params,
)

print(Web3.fromWei(int(result["price"]), "ether"))
print(result)