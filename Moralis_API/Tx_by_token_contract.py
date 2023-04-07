from moralis import evm_api
import os
from dotenv import load_dotenv
from web3 import Web3
load_dotenv()

api_key = os.environ.get('Moralis_API_KEY')
params = {
    "address": "0x0000000000a39bb272e79075ade125fd351887ac",
    "chain": "eth",
    "to_address": "0x130bd65a7401c053015fbd143798b298874e3785"  ## doesn't work
}

result = evm_api.token.get_token_transfers(
    api_key=api_key,
    params=params,
)

print(result)