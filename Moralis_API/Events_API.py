### https://docs.moralis.io/web3-data-api/reference/get-contract-events

from moralis import evm_api
import os
from dotenv import load_dotenv
from web3 import Web3
import json

load_dotenv()

api_key = os.environ.get('Moralis_API_key')
### topic?????
params = {
    "address": "0x6CC462bc49ceCFE943Bc4F477b23b92906e6074F", 
    "chain": "eth", 
    "topic": "0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31",
}

body= {"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Transfer","type":"event"}
print(type(body))
result = evm_api.events.get_contract_events(
    api_key=api_key,
    params=params,
    body=body
)

#print(Web3.fromWei(int(result["price"]), "ether"))
print(result["result"][0])