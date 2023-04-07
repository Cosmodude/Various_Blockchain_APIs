from moralis import evm_api
import os
from dotenv import load_dotenv
from web3 import Web3
load_dotenv()

api_key = os.environ.get('Moralis_API_KEY')

def get_transactions(block):
    params = {
        "block_number_or_hash": block,
        "chain": "eth",
        "limit": 100,
        #"cursor": "",
    }
    
    result = evm_api.nft.get_nft_transfers_by_block(
        api_key=api_key,
        params=params,
    )
    return result

##print(get_transactions("16985877")) 