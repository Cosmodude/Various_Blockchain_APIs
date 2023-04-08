## https://docs.etherscan.io/
## https://web.postman.co/workspace/My-Workspace~57c562ac-672a-46a7-801b-e3c460375cc7/request/24552765-c566c2d6-91d0-4d28-8b41-435cf8fa4c33
from dotenv import load_dotenv
load_dotenv()
import os
import requests
from NFT_tx_by_block import get_transactions

API_KEY = os.environ.get('EtherScan_API_KEY')

supernormal='0x130bd65a7401c053015fbd143798b298874e3785'
## Bloor Bidding: 0x0000000000a39bb272e79075ade125fd351887ac
## Bloor Marketplace: 
## Bloor Pool Token: 0x0000000000a39bb272e79075ade125fd351887ac
DG_Token= '0x48Be0965618ED7B65E577487e1f74f12aca74ef7'
## ETH Token:
## multiple token transfers tx: 0xab9875572bd672c02a2d4ee00f6d9e20d3d4fffbc04e71ee72901ce8adf392f0



URL= f"https://api.etherscan.io/api\
?module=account\
&action=tokentx\
&contractaddress=0x0000000000a39bb272e79075ade125fd351887ac\
&address=0x130BD65a7401C053015fbd143798B298874E3785\
&page=1\
&offset=10000\
&startblock=0\
&endblock=27025780\
&sort=desc\
&to=0x130BD65a7401C053015fbd143798B298874E3785\
&apikey={API_KEY}"

##print(requests.get(URL).json()["result"][1])
resp_json=requests.get(URL).json()
to_transactions=[]
## get only to_tx
for i in range(len(resp_json["result"])):
    if(resp_json["result"][i]["to"]==supernormal.lower()):
        to_transactions.append(resp_json["result"][i])

hashes=[to_transactions[i]["hash"] for i in range(len(to_transactions))]
blocks=[to_transactions[i]["blockNumber"] for i in range(len(to_transactions))]
print(to_transactions[0]["value"])
print(len(blocks))
print(len(hashes))
print(hashes[11])
## find unique blocks
unique_blocks=[]
unique_hashes=[]
for block in blocks:
    if(block not in unique_blocks):
        unique_blocks.append(block)
print(len(unique_blocks))
for hash in hashes:
    if(hash not in unique_hashes):
        unique_hashes.append(hash)
print(len(unique_hashes))


## count earnings
earnings=0
txs_number=0
for ublock in unique_blocks:
    NFT_txs_from_block = get_transactions(ublock)["result"]
    for NFT_tx in NFT_txs_from_block:
        if(NFT_tx["transaction_hash"] in hashes):
            if (NFT_tx["token_address"]==DG_Token.lower()):
                i=hashes.index(NFT_tx["transaction_hash"])
                earnings+=(float(to_transactions[i]["value"])/10e18)
                del hashes[i]
                del to_transactions[i]
                txs_number+=1


print(earnings)
print(txs_number)


