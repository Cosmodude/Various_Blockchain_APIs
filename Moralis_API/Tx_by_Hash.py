from moralis import evm_api
import os
from dotenv import load_dotenv
from web3 import Web3
load_dotenv()

api_key = os.environ.get('Moralis_API_KEY')

def transaction(hash):
    params = {
    "chain": "eth",
    "transaction_hash": hash
    }
    result = evm_api.transaction.get_transaction(
    api_key=api_key,
    params=params,
    )
    return result

print(transaction("0xc186cb645851409150ff12d467e03bdc749b2f834863bb1c414bbf24f481ea61"))